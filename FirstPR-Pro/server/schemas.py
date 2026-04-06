from pydantic import BaseModel
from typing import List, Optional

# ---- USER SCHEMAS ----
class UserBase(BaseModel):
    name: str
    avatar_url: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    score: float
    totalSolved: int
    avgRating: float

    class Config:
        orm_mode = True

# ---- SUBMISSION SCHEMAS ----
class SubmissionBase(BaseModel):
    solution: str

class SubmissionCreate(SubmissionBase):
    pass

class Submission(SubmissionBase):
    id: int
    issue_id: int
    solved_by_id: int
    rating: Optional[int] = None
    solver: Optional[User] = None

    class Config:
        orm_mode = True

class RateSubmission(BaseModel):
    rating: int

# ---- ISSUE SCHEMAS ----
class MarketplaceIssueBase(BaseModel):
    title: str
    description: str
    repo_link: str
    difficulty: str

class MarketplaceIssueCreate(MarketplaceIssueBase):
    creator_name: str # The user creating the issue
    creator_avatar: Optional[str] = None

class MarketplaceIssue(MarketplaceIssueBase):
    id: int
    status: str
    created_by_id: int
    creator: Optional[User] = None
    submissions: List[Submission] = []

    class Config:
        orm_mode = True

# ---- SCANNER SCHEMAS ----
class RepoScanRequest(BaseModel):
    url: str

class BeginnerIssue(BaseModel):
    title: str
    description: str
    difficulty: str

class RepoAnalysisResult(BaseModel):
    health_score: int
    issues: List[str]
    code_smells: List[str]
    security_risks: List[str]
    improvements: List[str]
    beginner_friendly_issues: List[BeginnerIssue]
