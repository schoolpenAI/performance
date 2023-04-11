
from fastapi import FastAPI
from schema import student_performance, Performance, PerformanceBySubject

app = FastAPI()


@app.post("/api/v1/evaluate", response_model=Performance)
def evaluate(student: student_performance):
    total_score = (student.correct_answer / student.total_quetion) * 100
    correct_percentage = (student.attempted_quetion/ student.total_quetion) * 100
    accuracy = (student.correct_answer / student.attempted_quetion) * 100
    efficiency = (student.attempted_quetion*60 / student.time_taken)
    return {
            "correct_percentage": correct_percentage,
            "total_score":total_score,
            "accuracy": accuracy,
            "efficiency": efficiency,
        }


    
"""
@app.post("/api/v1/getPerformanceBySubject", response_model=Performance)
def getAvgPerformanceByStudentWeekly(student: student_performance):
    performance = (student.correct_answer / student.total_quetion) * 100
    percentage = (student.attempted_quetion/ student.total_quetion) * 100
    accuracy = (student.correct_answer / student.attempted_quetion) * 100
    efficiency = (student.attempted_quetion*60 / student.time_taken)
    return {
            "performance": performance,
            "percentage": percentage,
            "accuracy": accuracy,
            "efficiency": efficiency,
        }


@app.post("/api/v1/getPerformanceBySubject/{subject_id}/{student_id}", response_model=Performance)
def getPerformanceBySubject(student: PerformanceBySubject):
    performance = (student.correct_answer / student.total_quetion) * 100
    percentage = (student.attempted_quetion/ student.total_quetion) * 100
    accuracy = (student.correct_answer / student.attempted_quetion) * 100
    efficiency = (student.time_taken / student.time_given)
    return {
            "performance": performance,
            "percentage": percentage,
            "accuracy": accuracy,
            "efficiency": efficiency,
        }


@app.post("/api/v1/getAvgPerformanceByStudentWeekly", response_model=Performance)
def getAvgPerformanceByStudentWeekly(student: student_performance):
    performance = (student.correct_answer / student.total_quetion) * 100
    percentage = (student.attempted_quetion/ student.total_quetion) * 100
    accuracy = (student.correct_answer / student.attempted_quetion) * 100
    efficiency = (student.time_taken / student.time_given)
    return {
            "performance": performance,
            "percentage": percentage,
            "accuracy": accuracy,
            "efficiency": efficiency,
        }


@app.post("/api/v1/getAvgPerformanceByStudentMonthly", response_model=Performance)
def getAvgPerformanceByStudentMonthly(student: student_performance):
    performance = (student.correct_answer / student.total_quetion) * 100
    percentage = (student.attempted_quetion/ student.total_quetion) * 100
    accuracy = (student.correct_answer / student.attempted_quetion) * 100
    efficiency = (student.time_taken / student.time_given)
    return {
            "performance": performance,
            "percentage": percentage,
            "accuracy": accuracy,
            "efficiency": efficiency,
        }

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import pyodbc
import datetime

app = FastAPI()

# Function to get the week number for a given date
def get_week_number_by_date(date_str: str) -> int:
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.isocalendar()[1]

# Model for the request payload
class StudentWeeklyRequest(BaseModel):
    student_id: int
    week_number: int
    date: str

# Model for the response payload
class StudentWeeklyResponse(BaseModel):
    accuracy: float
    correct_percentage: float
    efficiency: float
    student_id: int
    test_id: int
    total_score: float

# Function to calculate the average performance by student weekly
def calculate_average_performance_by_student_weekly(student_id: int, week_number: int) -> List[StudentWeeklyResponse]:
    # Connect to the database
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-DBB6O6KQ;DATABASE=performance_db;UID=prathi;PWD=p@123')

    cursor = conn.cursor()

    # Execute the SQL query to get the data for the given student and week number
    query = f"SELECT accuracy, correct_percentage, efficiency, student_id, test_id, total_score FROM result_analysis WHERE student_id = {student_id} and WEEK(date_taken) = {week_number}"
    cursor.execute(query, (student_id, week_number))

    # Fetch the results and calculate the averages
    results = cursor.fetchall()
    num_results = len(results)
    accuracy_sum = sum([result[0] for result in results])
    correct_percentage_sum = sum([result[1] for result in results])
    efficiency_sum = sum([result[2] for result in results])
    total_score_sum = sum([result[5] for result in results])
    averages = {
        "accuracy": accuracy_sum / num_results,
        "correct_percentage": correct_percentage_sum / num_results,
        "efficiency": efficiency_sum / num_results,
        "student_id": student_id,
        "test_id": results[0][4],
        "total_score": total_score_sum / num_results
    }

    # Close the database connection and return the averages
    conn.close()
    return [StudentWeeklyResponse(**averages)]

# Define the API endpoint for the getAvgPerformanceByStudentWeekly API
@app.post("/getAvgPerformanceByStudentWeekly")
async def get_avg_performance_by_student_weekly(request: StudentWeeklyRequest):
    week_number = request.week_number
    if week_number == -1:
        week_number = get_week_number_by_date(request.date)
    return calculate_average_performance_by_student_weekly(request.student_id, week_number)


"""
import pandas as pd
import pyodbc
from fastapi import FastAPI

app = FastAPI()

# Database configuration details
driver = "{ODBC Driver 17 for SQL Server}"
server = "LAPTOP-DBB6O6KQ"
database = "performance_db"
username = "prathi"
password = "p@123"

# Function to get the database connection
def get_db_conn():
    conn = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}")
    return conn

# Endpoint to calculate EWMA for a particular student and subject
@app.get("/ewma")
def calculate_ewma(student_id: int, subject_id: int):
    try:
        # Get the database connection
        conn = get_db_conn()
        
        # Query the database to get the required data
        query = f"SELECT * FROM result_analysis WHERE student_id={student_id} AND subject_id={subject_id}"
        df = pd.read_sql(query, conn)
        
        # Calculate the EWMA with span=30 and adjust=True
        ewma = df['total_score'].ewm(span=30, adjust=True).mean()
        
        # Format the result
        result = {'student_id': student_id, 'subject_id': subject_id, 'ewma': ewma.tolist()}
        
        # Return the result
        return result
        
    except Exception as e:
        # Handle any exceptions
        return {'error': str(e)}







