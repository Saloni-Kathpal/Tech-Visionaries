from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    avatar_url = Column(String, nullable=True)
    score = Column(Float, default=0.0)
    totalSolved = Column(Integer, default=0)
    avgRating = Column(Float, default=0.0)

    # Relationships
    issues_created = relationship("MarketplaceIssue", back_populates="creator")
    submissions = relationship("Submission", back_populates="solver")

class MarketplaceIssue(Base):
    __tablename__ = "marketplace_issues"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    repo_link = Column(String)
    difficulty = Column(String) # Easy, Medium, Hard
    status = Column(String, default="open") # open, in-progress, closed

    created_by_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships
    creator = relationship("User", back_populates="issues_created")
    submissions = relationship("Submission", back_populates="issue")

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    issue_id = Column(Integer, ForeignKey("marketplace_issues.id"))
    solved_by_id = Column(Integer, ForeignKey("users.id"))
    solution = Column(Text)
    rating = Column(Integer, nullable=True) # 1-5

    # Relationships
    issue = relationship("MarketplaceIssue", back_populates="submissions")
    solver = relationship("User", back_populates="submissions")
