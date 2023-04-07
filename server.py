from fastapi import FastAPI
from schema import student_performance, Performance, PerformanceBySubject

app = FastAPI()


@app.post("/api/v1/evaluate", response_model=Performance)
def evaluate(student: student_performance):
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