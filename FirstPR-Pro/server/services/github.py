import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_SEARCH_URL = "https://api.github.com/search/issues"

def fetch_github_issues(skills: str):
    """
    Fetches real issues from GitHub Search API based on skills and labels.
    """
    query = f"{skills} \"good first issue\" \"help wanted\" is:issue is:open"
    params = {
        "q": query,
        "sort": "created",
        "order": "desc",
        "per_page": 10
    }
    
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    
    try:
        response = requests.get(GITHUB_SEARCH_URL, params=params, headers=headers)
        if response.status_code != 200:
            return []
        
        data = response.json()
        items = data.get("items", [])
        
        cleaned_issues = []
        for item in items:
            # Extract repo name from repository_url: https://api.github.com/repos/owner/name
            repo_url = item.get("repository_url", "")
            repo_name = "/".join(repo_url.split("/")[-2:]) if repo_url else "unknown"
            
            cleaned_issues.append({
                "title": item.get("title"),
                "repo": repo_name,
                "url": item.get("html_url"),
                "comments": item.get("comments"),
                "created_at": item.get("created_at")
            })
            
        return cleaned_issues
        
    except Exception as e:
        print(f"Error fetching GitHub issues: {e}")
        return []
