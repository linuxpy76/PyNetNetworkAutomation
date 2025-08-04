import re

ipv4_pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

header = "-" * 20

with open("show_ip_int_brief.txt", "r") as f:
    show_ip = f.readlines()

show_ip = [s.rstrip() for s in show_ip]
intf_name_list = []
ip_addr_list = []

for line in show_ip:
    if re.match(ipv4_pattern, line.split()[1]):
        intf_name_list.append(line.split()[0])
        ip_addr_list.append(line.split()[1])

print("Interface and IP address lists:")
print(intf_name_list)
print(ip_addr_list)
print(header)

for intf in range(len(intf_name_list)):
    print(f"Interface: {intf_name_list[intf]}")
    print(f"IP address: {ip_addr_list[intf]}")
    print(header)