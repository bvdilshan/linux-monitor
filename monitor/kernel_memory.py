def get_memory_info():
    meminfo = {}

    with open("/proc/meminfo") as f:
        for line in f:
            key, value = line.split(":")
            meminfo[key] = value.strip()

    return {
        "MemTotal": meminfo.get("MemTotal"),
        "MemFree": meminfo.get("MemFree"),
        "MemAvailable": meminfo.get("MemAvailable"),
        "Buffers": meminfo.get("Buffers"),
        "Cached": meminfo.get("Cached")
    }