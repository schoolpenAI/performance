from fastapi import FastAPI
from schema import student_performance, Performance, PerformanceBySubject
import pandas as pd
import pyodbc
from datetime import datetime
from pydantic import BaseModel



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










# Create connection to SQL Server
driver = "{ODBC Driver 17 for SQL Server}"
server = "LAPTOP-DBB6O6KQ"
database = "performance_db"
username = "prathi"
password = "p@123"

conn = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}")

# Define model for incoming data
class ResultAnalysis(BaseModel):
    accuracy: int
    correct_percentage: int
    efficiency: int
    student_id: int
    subject_id: int
    test_id: int
    total_score: int
    subject_id: int
    test_date: str

# Define route to calculate monthly performance
@app.post("/calculate_monthly_performance")
async def calculate_monthly_performance():
    # Get current month and year
    current_month = datetime.now().month
    current_year = datetime.now().year

    # Fetch data from result_analysis table
    cursor = conn.cursor()
    cursor.execute("SELECT accuracy, correct_percentage, efficiency, student_id, test_id, total_score, subject_id, test_date FROM result_analysis")
    rows = cursor.fetchall()

    # Iterate through the rows and calculate monthly performance
    for row in rows:
        accuracy = row.accuracy
        correct_percentage = row.correct_percentage
        efficiency = row.efficiency
        student_id = row.student_id
        test_id = row.test_id
        total_score = row.total_score
        subject_id = row.subject_id
        test_date = row.test_date

         # Convert datetime.date object to string
        test_date_str = test_date.strftime("%Y-%m-%d")

        # Use the string version of test_date in strptime()
        test_date = datetime.strptime(test_date_str, "%Y-%m-%d")


        # Extract month and year from test_date
        month = test_date.month
        year = test_date.year

        # Check if the test_date is in the current month and year
        if month == current_month and year == current_year:
            # Insert calculated monthly performance into monthly_performance table
            cursor.execute("INSERT INTO monthly_performance (student_id, subject_id, month, year, accuracy, correct_percentage, efficiency, total_score) VALUES (?, ?, ?, ?, ?, ?,?,?)",
                           student_id, subject_id, month, year, accuracy, correct_percentage, efficiency, total_score)
            cursor.commit()

    return {"message": "Monthly performance calculated and stored successfully!"}


# Define model for incoming data
class MonthlyPerformance(BaseModel):
    student_id: int
    subject_id: int
    month:int

# Define route to get monthly performance
@app.post("/get_monthly_performance")
async def get_monthly_performance(data: MonthlyPerformance):
    student_id = data.student_id
    subject_id = data.subject_id
    month = data.month

    # Fetch data from monthly_performance table based on student_id, subject_id, and month
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, subject_id, month, year, accuracy, correct_percentage, efficiency, total_score FROM monthly_performance WHERE student_id = ? AND subject_id = ? AND month = ?",
                   (student_id, subject_id, month)) # corrected: added missing 'AND' in SQL query and passing parameters as tuple
    rows = cursor.fetchall()

    # Format retrieved data as a list of dictionaries
    monthly_performance = []
    for row in rows:
        monthly_performance.append({
            "student_id": row.student_id,
            "subject_id": row.subject_id,  # corrected: changed 'row.subject' to 'row.subject_id'
            "month": row.month,
            "year": row.year,
            "accuracy": row.accuracy,
            "correct_percentage": row.correct_percentage,
            "efficiency": row.efficiency,
            "total_score": row.total_score
        })

    return {"monthly_performance": monthly_performance}

