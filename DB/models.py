from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Text

Base = declarative_base()
"""
Data Model(DB資料表的模型)
"""

class Job(Base):
    __tablename__ = "jobs"

    # PK主鍵
    id = Column(String(20), primary_key= True, comment= 'custNo')

    # 首頁基本資訊
    company = Column(String(50), comment='公司名稱')
    name = Column(String(50), comment='職位名稱')
    addr = Column(String(10), comment='地區')
    salary = Column(String(20), comment='薪資範圍')

    # 內部詳細資訊
    description = Column(Text, comment='工作內容')
    realAddr = Column(String(100), comment="完整地址")
    workingtime = Column(String(100), comment="上班時間")
    skill = Column(String(100), comment="所需技能")
    link = Column(String(500), comment="應徵連結")


