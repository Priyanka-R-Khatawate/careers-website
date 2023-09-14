from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_job_to_db
app = Flask(__name__)


@app.route("/")
def hello_Juniper():
    jobs = load_jobs_from_db()
    return render_template('home.html', 
                           jobs=jobs, 
                           company_name='Juniper')

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if job:
    return render_template('jobpage.html',job=job,company_name='Juniper')
  return "Not found",404


@app.route("/job/<id>/apply",methods=[ "POST"])
def apply_job(id):
  application=request.form
  job=load_job_from_db(id)
  add_job_to_db(id,application)
  return render_template('application_submitted.html',application=application,job=job)

  
if __name__ == '__main__':
  app.run(debug=True)
