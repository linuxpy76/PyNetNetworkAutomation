header = "-" * 20
print(header)

with open("junos_show_arp.txt", "r") as f:
    show_arp = f.readlines()

show_arp = [s.rstrip() for s in show_arp]
mac_addr_list = []
ip_addr_list = []

show_arp.pop(0)
show_arp.pop()

for line in show_arp:
    output_line = line.split()
    mac_addr_list.append(output_line[0])
    ip_addr_list.append(output_line[1])

for mac in range(len(mac_addr_list)):
    mac_addr_list[mac] = mac_addr_list[mac].replace(":", "-")
    print(f"MAC address: {mac_addr_list[mac]}")
    print(f"IP address: {ip_addr_list[mac]}")
    print(header)