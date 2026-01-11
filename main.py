from ETL_pipline import Extract, Transform, Load
from DB import testconnection, operation

raw_data = Extract.fetch_jobData()
transed_data = Transform.transform_jobData(raw_data)
db_test = testconnection.test_connection()
operation.drop_table()
operation.create_table()
load_db = Load.load_to_db(transed_data)