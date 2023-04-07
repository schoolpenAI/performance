from fastapi import FastAPI
from typing import List
import mysql.connector

app = FastAPI()

@app.get("/performance/{subject_id}/{student_id}")
async def get_performance(subject_id: int, student_id: int):
    # Connect to the database
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="root@performance",
      database="performance_db"
    )

    # Execute a query to get the performance for the subject and student
    mycursor = result_analysis.cursor()
    query = f"SELECT result_analysis FROM  WHERE subject_id={4} AND student_id={5}"
    mycursor.execute(query)

    # Fetch the results
    performance_list = []
    for row in mycursor:
        performance_list.append(row[0])
        
    return performance_list
"""
from sqlalchemy.orm import Session

def get_student_performance_by_id(db: Session, student_id: str, subject_id: str):
    query = db.query(StudentPerformanceDB).filter(
        StudentPerformanceDB.student_id == student_id,
        StudentPerformanceDB.subject_id == subject_id
    ).all()

    student_performance = [StudentPerformance.from_orm(item) for item in query]
    return student_performance


from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/performance")
async def get_performance_data(student_id: str, subject_id: str, db: Session = Depends(get_db)):
    student_performance = get_student_performance_by_id(db, student_id, subject_id)
    return student_performance


@app.get("/api/v1/getPerformanceBySubject/{subject_id}/{student_id}", response_model=Performance)
def getPerformanceBySubject(student: PerformanceBySubject):
    return {
            "performance": performance,
            "percentage": percentage,
            "accuracy": accuracy,
            "efficiency": efficiency,
        }
"""