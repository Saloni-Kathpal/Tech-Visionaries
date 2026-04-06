from fastapi import APIRouter
from services import github

router = APIRouter()

@router.get("/issues")
def get_issues(skills: str = ""):
    """
    Fetches issues from GitHub based on skills.
    """
    # Fetch real issues from GitHub
    issues = github.fetch_github_issues(skills)

    # TODO: Apply ranking logic in utils/ranking.py later
    # This is where we will score issues based on difficulty and relevance.

    return issues
