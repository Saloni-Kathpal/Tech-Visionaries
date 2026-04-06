from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import issues

app = FastAPI(title="FirstPR Pro API")

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(issues.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FirstPR Pro API"}
