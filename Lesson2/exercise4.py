with open("show_arp.txt") as f:
    show_arp = f.readlines()

print(f"The ARP list is a {type(show_arp)} data type and it has {len(show_arp)} elements\n")
print(f"Here are the headers:\n{show_arp[0]}")
print(f"This is the first entry in the ARP list:\n{show_arp[1]}")
print(f"This is the last entry in the ARP list:\n{show_arp[-1]}")
# Define fields in ARP list
fields = show_arp[0].split()
print(f"Here are the fields in a list:\n{fields}\n")
print(f"The fields variable is a {type(fields)} and has a length of {len(fields)}\n")
print(f"Here is the first header: {fields[0]}")
print(f"Here is the last header: {fields[-1]}")
print()

# Cleaning up fields
fields.pop(5)
fields[4] = "Hardware_Addr"
fields.pop(3)
print(f"Fields list is cleaned up:\n{fields}")
print()