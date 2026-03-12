def get_load_average():
    with open("/proc/loadavg") as f:
        data = f.read().split()

    return {
        "load_1min": data[0],
        "load_5min": data[1],
        "load_15min": data[2],
        "running_processes": data[3],
        "last_pid": data[4]
    }