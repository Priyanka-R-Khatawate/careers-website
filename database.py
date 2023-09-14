from sqlalchemy import create_engine,text
from decouple import config
import os
# Create a database connection
db_url = os.environ.get('db_url')
engine = create_engine(db_url)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM jobs '))
        result_all=result.all()
        # print(result_all.__dict__)
        jobs= []
        for job in result_all:
            jobs.append(job._asdict())
            
        return jobs
        
def load_job_from_db(id):
    with engine.connect() as conn:
        query = text('SELECT * FROM jobs where id = {}'.format(id))
        result = conn.execute(query)
        rows=result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()
        

def add_job_to_db(job_id,application):
    with engine.connect() as conn:
        query = text('INSERT INTO applications (job_id,full_name,email,linkedln_url,education,work_experience,resume_url) values (:job_id,:full_name,:email,:linkedln_url,:education,:work_experience,:resume_url)')
        params = {'job_id':job_id,"full_name":application['name'],"email":application['email'],"linkedln_url":application['linkedln'],"education":application['education'],"work_experience":application['experience'],"resume_url":application['resume']}
        conn.execute(query,params)
        conn.commit()
        
        
    