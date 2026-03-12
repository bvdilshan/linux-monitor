def get_cpu_stat():
    with open("/proc/stat", "r") as f:
        line = f.readline()

    values = line.split()

    return {
        "user": values[1],
        "nice": values[2],
        "system": values[3],
        "idle": values[4],
        "iowait": values[5]
    }