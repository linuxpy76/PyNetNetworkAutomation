with open("show_ip_int_brief.txt", "r") as f:
    show_ip = f.readlines()

show_ip = [s.rstrip() for s in show_ip]

for line in show_ip:
    if "10.220." in line:
        # print(line)
        ip_line = line.split()
        # print(ip_line)

intf_name = ip_line[0]
ip_addr = ip_line[1]

print(f"Interface: {intf_name}")
print(f"IP address: {ip_addr}")