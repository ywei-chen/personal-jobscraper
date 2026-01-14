# Pydantic Schema - 定義 API 回傳的資料格式
# dependency injection
# get method


from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from DB.testconnection import Session
from DB.models import Job
from fastapi.responses import JSONResponse

app = FastAPI(title="Job_API", description="Job_DATA")

class Job_response(BaseModel):
    id: int
    company: Optional[str] = None
    name: Optional[str] = None
    addr: Optional[str] = None
    salary: Optional[str] = None
    description: Optional[str] = None
    realAddr: Optional[str] = None
    workingtime: Optional[str] = None
    skill: Optional[str] = None
    link: Optional[str] = None

    class Config:
        from_attributes = True

def get_db():
    with Session() as db:
        yield db

@app.get("/jobs", response_model= list[Job_response])
def get_all_jobs(db = Depends(get_db)):
    jobs = db.query(Job).all()
    return jobs
