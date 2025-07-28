ip_addresses = ["10.10.10.1", "10.10.10.2", "10.10.10.3", "10.10.10.4", "10.10.10.5"]
ip_addresses.append("10.10.10.6")
ip_addresses.extend(["10.10.10.7", "10.10.10.8"])
print(ip_addresses)
print(ip_addresses[0])
print(ip_addresses[-1])
ip_addresses.pop(0)
ip_addresses.pop()
print(ip_addresses[0])
print(ip_addresses[-1])
ip_addresses = ["2.2.2.2"] + ip_addresses
print(ip_addresses[0])
print(ip_addresses)