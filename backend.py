# from pydantic import BaseModel
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

@dataclass
class DatasetInfo():
    data_name: str
    size: str
    _type_ : str
    nested_status: str

class marksobtained():
    tenth : float
    twelvth : float
    grad : float

    def __init__(self, tenth, twelvth, grad):
        self.tenth = tenth,
        self.twelvth = twelvth,
        self.grad = grad,
        




@app.get("/")
def greet():
    return  "Welcome to the NeuroScan Service!"


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

@app.get("/Marks Obtained")
def get_marks():
    return marksobtained(
        tenth = 85.71,
        twelvth= 73.16,
        grad=7.81
    )

@app.get("/Dataset Description")
def get_datadesc():
    return DatasetInfo(
        data_name= "Glioma",
        size= "3157",
        _type_= "List",
        nested_status= "False"
    )


    