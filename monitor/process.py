import psutil

def get_processes():
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        processes.append(proc.info)

    return processes