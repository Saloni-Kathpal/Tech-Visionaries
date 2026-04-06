from fastapi import APIRouter
from services import github
from utils import ranking

router = APIRouter()

@router.get("/issues")
def get_issues(skills: str = ""):
    # TODO: Integrate with GitHub API in services/github.py
    # TODO: Apply ranking logic in utils/ranking.py
    
    # Dummy data for now
    dummy_issues = [
        {
            "title": f"Fix documentation for {skills if skills else 'general'} project",
            "repo": "example/repo",
            "url": "https://github.com/example/repo/issues/1",
            "score": 85
        },
        {
            "title": "Add simple unit tests",
            "repo": "test/repo",
            "url": "https://github.com/test/repo/issues/42",
            "score": 60
        }
    ]
    return dummy_issues
