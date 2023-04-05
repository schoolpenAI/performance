from pydantic import BaseModel
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
                           
class student_performance(BaseModel):
    student_id: str = Field(..., title="Student ID", max_length=50, example="ABC123")
    school_id: int = Field(..., title="School ID", ge=0, example=123)
    class_id: int = Field(..., title="Class ID", ge=0, example=456)
    datetime: Optional[datetime] = Field(None, title="Date and Time", example="2022-12-31T23:59:59")
    test_type: str = Field(..., title="Test Type", max_length=50, example="Midterm Exam")
    test_subject: str = Field(..., title="Test Subject", max_length=50, example="Math")
    total_question: int = Field(..., title="Total Questions", ge=1, example=20)
    attempted_question: int = Field(..., title="Attempted Questions", ge=0, example=15)
    correct_answer: int = Field(..., title="Correct Answers", ge=0, example=12)
    time_given: Optional[int] = Field(None, title="Time Given (Minutes)", ge=1, example=60)
    time_taken: Optional[int] = Field(None, title="Time Taken (Minutes)", ge=1, example=45)
"""
class student_performance(BaseModel):
    student_id=str
    schoolid: int
    classid: int
    datetime: str
    test_type:str
    test_subject:str
    total_quetion:int
    attempted_quetion:int
    correct_answer:int
    time_given:int
    time_taken:int

class Performance(BaseModel):
    efficiency:float
    accuracy:float
    percentage:float
    performance:float

