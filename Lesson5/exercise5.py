import re

with open("aruba_cx_show_ipv6_intf.txt", mode="r") as f:
    data = f.read()

match_string = r"^Interface (\S+) \S+ (up|down)\s.*(up|down)\s\S+ \S+\s+(\S+).*$"

results = re.search(match_string, data, flags=re.M)

if results:
    interface = results.group(1)
if results:
    int_status = results.group(2)
if results:
    admin_status = results.group(3)
if results:
    ipv6_addr = results.group(4)

print()
print("-" * 25)
print(f"Interface: {interface}")
print(f"  Status: {int_status}")
print(f"  Admin state: {admin_status}")
print(f"  IPv6 address: {ipv6_addr}")
print("-" * 25)
print()