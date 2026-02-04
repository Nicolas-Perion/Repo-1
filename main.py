from typing import Union
from fastapi import FastAPI
from surface_score import compute_surface

app = FastAPI()

@app.get("/surface")
def surface():
    return {"surface": compute_surface()}