# 🧪 Testing Report (Initial Findings) — FirstPR Pro

## 👤 Role

Security & Testing Team Member

---

## 🔴 Problem 1: Match Score Not Working Properly

### Issue:
The match score does not accurately reflect the relevance between user skills and GitHub issues. Many unrelated issues receive similar scores.

### Impact:
- Poor recommendation accuracy
- Users cannot trust ranking

### Cause:
- Weak keyword matching logic
- No weighting based on number of matched skills

### Suggested Fix:
- Implement weighted scoring system
- Match skills against both title and description
- Normalize score between 0–100%
## 🔴 Problem 2: Irrelevant Language Results (Chinese/Japanese)

### Issue:
Search results include issues written in non-English languages such as Chinese and Japanese, making them difficult to understand for most users.

### Impact:
- Poor user experience
- Reduced usability of recommendations
- Users may ignore relevant issues due to language barrier

### Cause:
- GitHub API returns global results without language filtering
- No validation for content language

### Suggested Fix:
- Add language filter in API query (e.g., language:javascript, language:python)
- Allow user to select preferred language
- Filter non-English text using validation logic