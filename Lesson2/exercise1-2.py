from rich import print

base = "192.168.254."
prefix = int(input("CIDR 25-30: "))

prefix_binary = 32 - prefix
hosts = 2 ** prefix_binary
first_last = 2
usable_hosts = hosts - first_last

header = "-" * 40

print(header)
print(f"Network Address: {base}{hosts - hosts}")
print(f"First Address: {base}1")
print(f"Last Address: {base}{usable_hosts}")
print(f"Broadcast Address: {base}{hosts - 1}")
print(f"Second Subnet: {base}{hosts}")
print(header)

