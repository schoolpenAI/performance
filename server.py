from fastapi import FastAPI
import pandas as pd
import matplotlib.pyplot as plt
from schema import student_performance, Performance

app = FastAPI()


@app.post("/api/v1/evaluate", response_model=Performance)
def evaluate(student: student_performance):
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

    


@app.post("/api/v1/getPerformanceBySubject", response_model=Performance)
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


@app.post("/api/v1/getPerformanceBySubject", response_model=Performance)
def getPerformanceBySubject(student: student_performance):
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

Data=pd.DataFrame({"test_number":[1,2,3,4,5,6,7],"perf":[75,89,90,76,60,78,85]})# here we need to fetch all past test performence with test number

def EWMA(Data):
    #lets calculate Exponentially moving average
    X1=Data["perf"].ewm(alpha=0.1).mean()
    plt.plot([1,2,3,4,5,6,7],Data["EWMA"],color="g")This can be shown on app page
    plt.title("Exponentially weighted moving average")
    return X1# it will give list which shows exponentially weighted moving average of student
