from pydantic import BaseModel
from fastapi import FastAPI
from dataclasses import dataclass

app = FastAPI()
@dataclass
class DeveloperInfo():
    name: str 
    date_of_birth: str 
    product_name: str 
    product_type : str 
    domain : str 


class DatasetInfo():
    data_name: str
    size: int
    _type_ : str
    nested_status: bool

    def __init__(self, data_name, size, _type_, nested_status):
        self.data_name = data_name,
        self.size = size,
        self._type_ = _type_,
        self.nested_status = nested_status


        

class marksobtained():
    id : int
    standard: str
    marks : float

    def __init__(self, id, standard, marks):
        self.id = id,
        self.standard = standard,
        self.marks = marks
        
marks = [
    marksobtained(id =1, standard="tenth", marks=85.71),
    marksobtained(id =2, standard="twelveth",marks=73.13),
    marksobtained(id =3, standard="grads(CGPA)",marks =7.81)
]



@app.get("/")
def greet():
    return  "Welcome to the NeuroScan Service!"

@app.post("/User Input")
class user_input:
    name : str
    email : str
    password: int

    def __init__(self, name,email, password):
        self.name = name
        self.email = email
        self.password = password
        
def user():
    return user_input()

@app.get("/Developer Info")
def get_details():
    return  DeveloperInfo(
        name = "Tanmay Kumar Chaki",
        date_of_birth= "29-Dec-2003",
        product_name="NeuroScan",
        product_type="Project",
        domain="Machine Leanring and Data Science"

    )


@app.get("/Developer Description")
def get_devdesc():
    return """Data Analyst with a strong academic foundation in Mathematics (B.Sc. Honours) and a rigorous, structured approach to data-driven problem solving. My background enables a deep understanding of statistical reasoning, analytical models, and quantitative methods, rather than surface-level tool usage.

I work across data analysis, pattern discovery, and machine learning, transforming raw datasets into actionable insights and decision-ready outputs. Mathematics anchors my approach to modeling, validation, and interpretation, ensuring results are accurate, explainable, and reliable.

I am focused on continuous skill development in analytics, data science, and applied machine learning, and I seek opportunities to contribute to impact-driven teams where data directly informs intelligent, measurable decisions."""

@app.get("/Marks-Obtained")
def get_marks():
    return marks

@app.get("/marks/{id}")
def get_marks_by_id(id: int):
    for mark in marks:
        if mark.id == id:
            return marks

    return marks[id-1]
    # return marks[id -1]

nested_dataset = [
    DatasetInfo(
        data_name = "Medical Training",
        size = 8745,
        _type_ = "PIP.image // Nested",
        nested_status = True
    ),
    DatasetInfo(
        data_name = "Medical Testing",
        size = 512,
        _type_ = "PIP.image // Nested",
        nested_status = True
    )
]
sub_dataset = [
    DatasetInfo(
        data_name = "Glioma",
        size = 3157,
        _type_ = "PIP.image // Training // Testing",
        nested_status = False
    ),
    DatasetInfo(
        data_name = "Meningioma",
        size = 3453,
        _type_ = "PIP.image // Training // Testing",
        nested_status = False

    ),
    DatasetInfo(
        data_name = "non_tumor",
        size = 711,
        _type_ = "PIP.image // Training // Testing",
        nested_status = False
        
    ),
    DatasetInfo(
        data_name = "pituitary",
        size = 1424,
        _type_ = "PIP.image // Training // Testing",
        nested_status = False
        
    )
]

@app.get("/Dataset Description")
def get_datadesc():
    return nested_dataset, sub_dataset

    