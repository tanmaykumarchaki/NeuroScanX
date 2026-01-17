from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class DeveloperInfo(BaseModel):
    name: str 
    date_of_birth: str 
    product_name: str 
    product_type : str 
    domain : str 




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

