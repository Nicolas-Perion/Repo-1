from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/surface")
def surface():
    return {"surface": 1}