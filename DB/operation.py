from DB.models import Base
from DB.testconnection import engine, Session, DB_URL
from sqlalchemy import text

"""
CRUD與操作DB的各項函式
"""

def create_table():
    Base.metadata.create_all(engine)
    print("創建table成功")

def drop_table():
    Base.metadata.drop_table(engine)
    print("刪除table成功")

replace_view_sql = """
    CREATE OR REPLACE VIEW jobs_list AS
    SELECT id, company, name, addr, salary
    FROM jobs;
"""
def replace_view():
    with Session() as db:
        db.execute(text(replace_view_sql))
        print("創建View成功")

drop_view_sql = """
    DROP job_list
"""
def drop_view():
    with Session() as db:
        db.execute(text(drop_view_sql))
        print("刪除View成功")