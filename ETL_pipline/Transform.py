def transform_jobData(jobData):
    """
    將fetch的資料轉換為dist(key , value)
    後續透過load.py 轉換為Column存進DB
    """

    transformed_jobData = []

    for job in jobData:
        each_jobData ={
            # 改用自動遞增值作為PK
            #'id': job.get('custNo', None), 
            
            # 首頁呈現: 公司名稱、職稱、直轄市區、薪資
            'company': job.get('custName', None),
            'name': job.get('jobName', None),
            'addr': job.get('jobAddrNoDesc', None),
            'salary': (
                f"{job.get('salaryLow')}元以上"
                if job.get('salaryHigh') == 9999999 and job.get('salaryLow')
                else f"{job.get('salaryLow')}元 ~ {job.get('salaryHigh')}元"
                if job.get('salaryLow') and job.get('salaryHigh')
                else "待遇面議"
            ),
                          
            # 點擊詳情可顯示: 公司名稱、職稱、具體地址、薪資、工作內容、擅長工具、上班時間、應徵連結
            'description': job.get('description', None),
            'realAddr': (f"{job.get('jobAddrNoDesc')}{job.get('jobAddress')}"),
            'workingtime': job.get('d3'),
            'skill': ('、'.join([s['description'] for s in job.get('pcSkills')]) 
                     if job.get('pcSkills') 
                     else "不拘"),
            'link': (job.get('link', {}).get('job', None))
        }
        
        transformed_jobData.append(each_jobData)

    return transformed_jobData