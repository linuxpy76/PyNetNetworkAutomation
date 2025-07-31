from rich import print

base = "192.168.254."
prefix = int(input("CIDR 25-30: "))
header = "-" * 40

prefix_binary = 32 - prefix
hosts = 2 ** prefix_binary
first_last = 2
network_address = 0
usable_hosts = hosts - first_last

base_prefix_binary = 8
base_hosts = 2 ** base_prefix_binary
number_of_subnets = base_hosts // hosts
print(f"Number of subnets: {number_of_subnets}")
print(header)

for subnet in range(number_of_subnets):
    print(f"Subnet: {subnet + 1}")
    print(f"Network Address: {base}{network_address}")
    print(f"First Address: {base}{network_address + 1}")
    print(f"Last Address: {base}{network_address + usable_hosts}")
    print(f"Broadcast Address: {base}{network_address + hosts - 1}")
    print(header)
    network_address = network_address + hosts