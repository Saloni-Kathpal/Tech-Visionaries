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
## 🔴 Problem 3: No Skill Suggestion While Typing

### Issue:
The system does not provide any suggestions while the user types skills. Users must manually guess the correct keywords.

### Impact:
- Poor user experience
- Incorrect or inconsistent skill input
- Reduced matching accuracy and relevance of results

### Cause:
- No autocomplete or suggestion mechanism implemented
- No predefined skill dataset used for guidance

### Suggested Fix:
- Implement dynamic skill suggestion (autocomplete) feature
- Provide a predefined list of common technical skills
- Allow multi-skill selection with guided input
## 🔴 Problem 4: No Skill-Level Based Filtering (Beginner vs Advanced)

### Issue:
The system does not differentiate between user experience levels. Beginners are shown high-complexity issues that may not be suitable for their skill level.

### Impact:
- Beginners may feel overwhelmed  
- Reduced chances of successful contribution  
- Poor onboarding experience for new users  

### Cause:
- No user proficiency level input (e.g., beginner, intermediate)  
- Ranking system does not consider difficulty of issues  

### Suggested Fix:
- Add user level selection (Beginner / Intermediate / Advanced)  
- Prioritize “good first issue” and low-complexity issues for beginners  
- Adjust scoring algorithm based on user experience level  