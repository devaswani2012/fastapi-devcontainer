#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

from fastapi import Request, FastAPI
from typing import Optional
from pydantic import BaseModel
import pandas as pd
import json
import os

api = FastAPI()

@api.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API"}

@api.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@api.get("/customer/{idx}")
def get_customer(idx:int):
    # read data from csv file
    df = pd.read_csv("../customers.csv")
    # filter the data based on the index
    customer = df.iloc[idx]
    return customer.to_dict()

@api.post("/get_payload")
async def get_payload(request: Request):
    response = await request.json()
    geo = response.get("geo")
    url = "https://maps.google.com/?q=(geo)".format(geo=geo)
    # return await request.json()