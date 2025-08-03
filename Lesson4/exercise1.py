with open("show_ip_int_brief.txt", "r") as f:
    data = f.readlines()

ip_addresses = {}

for line in data:
    if "10." in line:
        line_split = line.split()
        interface = line_split[0]
        ip_address = line_split[1]
        ip_addresses.update({interface: ip_address})

for k, v in ip_addresses.items():
    print(f"{k} --> {v}")