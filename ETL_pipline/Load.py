from DB.models import Job
from DB.testconnection import Session


def load_to_db(transformed_jobData, clear_data =True):
    """
    將trasform.py轉成dist後的資料轉成DB Model的格式
    並存入PostgreSQL中
    """
    with Session() as db:
        try:
            if clear_data:
                delete_count = db.query(Job).delete()
                print(f"已刪除舊資料: 共{delete_count}筆")

            jobs = []
            for job_data in transformed_jobData:
                job = Job(**job_data)
                jobs.append(job)

            db.add_all(jobs)
            db.commit()
            print("資料存入成功")
            return True
        
        except Exception as e:
            db.rollback()
            print(f"資料存入失敗: {e}")
            return False