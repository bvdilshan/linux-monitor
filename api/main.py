from fastapi import FastAPI
from monitor.cpu import get_cpu_usage
from monitor.memory import get_memory_usage
from monitor.disk import get_disk_usage
from monitor.process import get_processes


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Linux Monitor Running"}

@app.get("/cpu")
def cpu():
    return get_cpu_usage()

@app.get("/memory")
def memory():
    return get_memory_usage()

@app.get("/disk")
def disk():
    return get_disk_usage()

@app.get("/processes")
def processes():
    return get_processes()