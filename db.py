import pyodbc
from fastapi import FastAPI

# creating a FastAPI instance
app = FastAPI()

# creating the connection to the SQL Server database
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-DBB6O6KQ;DATABASE=performance_db;UID=prathi;PWD=p@123')

# define a FastAPI endpoint to extract the result analysis data
@app.get("/getPerformanceBySubject/{subject_id}/{student_id}")
async def getPerformanceBySubject(subject_id: int, student_id:int):
    # create a cursor to execute SQL queries
    cursor = cnxn.cursor()

    # execute a SQL query to extract the desired data based on the provided subject_id
    query = f"SELECT accuracy, correct_percentage, total_score, efficiency FROM result_analysis WHERE subject_id = {subject_id} and student_id = {student_id}"
    cursor.execute(query)

    # extract the results and format them as a dictionary
    results = cursor.fetchone()
    data = {
        "accuracy": results[0],
        "correct_percentage": results[1],
        "total_score": results[2],
        "efficiency": results[3]
    }

    # return the data as a JSON response
    return data



