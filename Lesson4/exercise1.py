import re

ipv4_pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

with open("show_ip_int_brief.txt", "r") as f:
    data = f.readlines()

ip_addresses = {}

for line in data:
    if re.match(ipv4_pattern, line.split()[1]):
        interface = line.split()[0]
        ip_address = line.split()[1]
        ip_addresses[interface] = ip_address

for k, v in ip_addresses.items():
    print(f"{k} --> {v}")