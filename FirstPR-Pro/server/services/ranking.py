from datetime import datetime

def rank_issues(issues, skills):
    user_skills = set(skills.lower().split())
    ranked_issues = []
    
    for issue in issues:
        score = 0
        title = issue.get("title", "").lower()
        
        if "good first issue" in title:
            score += 20
            
        for skill in user_skills:
            if skill in title:
                score += 30
            
        created_at_str = issue.get("created_at", "")
        if created_at_str:
            try:
                issue_date = datetime.strptime(created_at_str[:10], "%Y-%m-%d")
                delta_days = (datetime.now() - issue_date).days
                if delta_days <= 30:
                    score += 20
                    if delta_days <= 7:
                        score += 10
            except ValueError:
                pass
                
        comments = issue.get("comments", 0)
        if isinstance(comments, int):
            if comments == 0:
                score += 15
            elif comments < 5:
                score += 10
            
        issue_copy = issue.copy()
        issue_copy["_score"] = score
        ranked_issues.append(issue_copy)
        
    ranked_issues.sort(key=lambda x: x.get("_score", 0), reverse=True)
    
    for issue in ranked_issues:
        if "_score" in issue:
            del issue["_score"]
            
    return ranked_issues
