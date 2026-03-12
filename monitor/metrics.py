from prometheus_client import Gauge
import psutil

cpu_usage = Gauge("system_cpu_usage_percent", "CPU usage percent")
memory_usage = Gauge("system_memory_usage_percent", "Memory usage percent")

def update_metrics():
    cpu_usage.set(psutil.cpu_percent())
    memory_usage.set(psutil.virtual_memory().percent)