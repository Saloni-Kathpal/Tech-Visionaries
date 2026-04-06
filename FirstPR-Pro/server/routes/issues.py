from fastapi import APIRouter
from services import github
from services.ranking import rank_issues
from services import llm_recommender

router = APIRouter()

@router.get("/issues")
def get_issues(skills: str = "", level: str = "beginner"):
    """
    Fetches issues from GitHub based on skills, then applies AI recommendations.
    """
    # Fetch real issues from GitHub
    issues = github.fetch_github_issues(skills, level)

    # Apply ranking logic to calculate match scores
    if issues:
        issues = rank_issues(issues, skills, level)
        
        # Pass top issues through the LLM for smart recommendations
        try:
            ai_recommendations = llm_recommender.generate_ai_recommendations(skills, issues)
            if ai_recommendations:
                return ai_recommendations
        except Exception as e:
            print(f"Error in LLM recommendations: {e}")

    # Fallback to original issues if LLM failed or disabled
    return issues
