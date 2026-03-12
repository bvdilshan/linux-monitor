from fastapi import FastAPI
from monitor.cpu import get_cpu_usage
from monitor.memory import get_memory_usage
from monitor.disk import get_disk_usage
from monitor.process import get_processes
from monitor.kernel_cpu import get_cpu_stat
from monitor.kernel_memory import get_memory_info
from monitor.load import get_load_average

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

@app.get("/kernel/cpu")
def kernel_cpu():
    return get_cpu_stat()

@app.get("/kernel/memory")
def kernel_memory():
    return get_memory_info()

@app.get("/kernel/load")
def kernel_load():
    return get_load_average()
