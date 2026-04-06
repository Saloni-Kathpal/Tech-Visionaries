from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db
from services import github, analyzer

router = APIRouter(prefix="/scanner", tags=["Scanner"])

@router.post("/analyze", response_model=schemas.RepoAnalysisResult)
def analyze_repository(request: schemas.RepoScanRequest):
    """
    Fetches repo data and uses AI to generate insights.
    """
    owner, repo = github.parse_github_url(request.url)
    if not owner or not repo:
        raise HTTPException(status_code=400, detail="Invalid GitHub URL")
        
    repo_data = github.get_repo_data(owner, repo)
    if not repo_data.get("readme") and not repo_data.get("file_tree"):
        raise HTTPException(status_code=404, detail="Could not retrieve repository data")
        
    analysis = analyzer.analyze_repo(repo_data)
    if "error" in analysis:
        raise HTTPException(status_code=500, detail=analysis["error"])
        
    return analysis

@router.post("/convert")
def convert_to_marketplace(
    repo_url: str, 
    issue: schemas.BeginnerIssue, 
    creator_name: str = "AI Scanner", 
    db: Session = Depends(get_db)
):
    """
    Pushes an AI-generated issue into the Marketplace.
    """
    try:
        # Get or create AI user
        user = db.query(models.User).filter(models.User.name == creator_name).first()
        if not user:
            user = models.User(name=creator_name, avatar_url="https://api.dicebear.com/7.x/bottts/svg?seed=AI")
            db.add(user)
            db.commit()
            db.refresh(user)

        db_issue = models.MarketplaceIssue(
            title=issue.title,
            description=issue.description,
            repo_link=repo_url,
            difficulty=issue.difficulty,
            status="open",
            created_by_id=user.id
        )
        db.add(db_issue)
        db.commit()
        db.refresh(db_issue)
        return {"message": "Success", "issue_id": db_issue.id}
    except Exception as e:
        print(f"CONVERT_ERROR: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")
