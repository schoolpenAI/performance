from fastapi import FastAPI
from schema import student_performance, Performance

app = FastAPI()


@app.post("/api/v1/evaluate", response_model=Performance)
def create_student_performance(student: student_performance):
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

    
