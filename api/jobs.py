from fastapi import FastAPI, Depends
from pydantic import BaseModel, ConfigDict
from typing import Optional
from DB.testconnection import Session
from DB.models import Job

"""
Jobs API
職缺資料相關的 API 端點
"""

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

    model_config = ConfigDict(from_attributes=True)

def get_db():
    with Session() as db:
        yield db

@app.get(
    "/jobs", 
    response_model= list[Job_response],
    summary="取得所有職缺",
    description="回傳目前資料庫中所有已整理完成的職缺資料"
    )
def get_all_jobs(db = Depends(get_db)):
    jobs = db.query(Job).all()
    return jobs
