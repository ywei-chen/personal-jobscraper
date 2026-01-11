import time
from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

load_dotenv()
DB_URL = f"postgresql+psycopg://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}?client_encoding=utf8"
# Session是一個類別!
# 建立global讓engine、Session可在其他模組import共用
engine = create_engine(DB_URL, pool_pre_ping=True)
Session = sessionmaker(engine)

def test_connection():
    """
    測試建立連線
    """

    print("若連線失敗，將啟動重試機制，自動嘗試連線3次!")

    for i in range(3):
        try:
            print(f"[第{i+1}次 連線中]...")
            time.sleep(2)
            db = Session()
            print("連線成功")

            print("查詢測試中...")
            time.sleep(2)
            db.execute(text("SELECT 1"))
            print("查詢測試成功")

            print("關閉連線...")
            db.close()
            return True
        
        except Exception as e:
            print(f"第{i+1}次 失敗")

    print("連線失敗，已嘗試 3 次")
    return False

