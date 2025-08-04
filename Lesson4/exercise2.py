with open("show_ip_int_brief.txt", "r") as f:
    data = f.readlines()

interfaces = {}

for line in data[1:]:
    parts = line.split()
    
    interface = parts.pop(0)
    ip_addr = parts.pop(0)
    protocol = parts.pop(-1)
    status = ' '.join(parts[2:])

    interfaces[interface] = {}
    interfaces[interface] = {
        "ip_addr": ip_addr,
        "line_status": status,
        "line_protocol": protocol
    }

for k, v in interfaces.items():
    print(f"Interface: {k}")
    for inner_key, inner_value in v.items():
        print(f"  {inner_key}: {inner_value}")

