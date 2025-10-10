import re

with open("arista_show_ip_arp.txt", mode="r") as f:
    data = f.read()

ip_address = r"(\d+\.\d+\.\d+\.\d+)"
mac_address = r"(\w+\.\w+\.\w+)"

arp_table = re.findall(rf"^{ip_address}.+?{mac_address}.+?$", data, flags=re.MULTILINE)

# print(arp_table)
# print(dict(arp_table))
arp_table = dict(arp_table)

for k, v in arp_table.items():
    print(f"{k} --> {v}")