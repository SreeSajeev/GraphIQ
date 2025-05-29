from fastapi import FastAPI
from py2neo import Graph

app = FastAPI()
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

@app.get("/")
def read_root():
    return {"message": "GraphIQ Backend Running"}
