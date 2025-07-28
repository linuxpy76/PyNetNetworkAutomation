intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"
intf_fields = intf.split()

intf_name = intf_fields[0]
intf_ip_addr = intf_fields[1]
intf_status = intf_fields[4]
intf_protocol = intf_fields[5]

print(f"{intf_name} {intf_ip_addr} {intf_status} {intf_protocol}")

if intf_status == "up": intf_status_bool = True
print(f"Interface status is: {intf_status_bool}")
if intf_protocol == "up": intf_protocol_bool = True
print(f"Interface protocol is: {intf_protocol_bool}")

print(f"Interface status and protocol is: {intf_status_bool and intf_protocol_bool}")
