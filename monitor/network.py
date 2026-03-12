def get_network_stats():
    interfaces = {}

    with open("/proc/net/dev") as f:
        lines = f.readlines()[2:]

    for line in lines:
        parts = line.split()
        interface = parts[0].replace(":", "")

        interfaces[interface] = {
            "bytes_received": parts[1],
            "packets_received": parts[2],
            "bytes_transmitted": parts[9],
            "packets_transmitted": parts[10]
        }

    return interfaces