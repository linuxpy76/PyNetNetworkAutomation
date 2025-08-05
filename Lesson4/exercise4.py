from rich import print

# Read in file
with open("arubacx_show_vlan.txt") as f:
    data = f.read()

# Initialize blank directory
vlan_map = {}

for line in data.splitlines():
    if "-----" in line:
        continue
    if "Name" and "Type" in line:
        continue

    vlan_id, vlan_name, status, reason, vlan_type, interfaces = line.split()
    intf_groups = interfaces.split(",")

    intf_list = []

    # Construct list of interfaces associated with given VLAN ID
    for intf in intf_groups:
        # Check for ranges
        if "-" in intf:
            intf_start, intf_end = intf.split("-")
            # Drop last character for base interface
            base_intf = intf_start[:-1]

            # Interfaces with x/x/x notation
            if "/" in intf_start and "/" in intf_end:
                intf_fields = intf_start.split("/")
                start_idx = int(intf_fields[-1])

                intf_fields = intf_end.split("/")
                end_idx = int(intf_fields[-1])
            
            # lag interfaces
            if "lag" in intf_start and "lag" in intf_end:
                start_idx = int(intf_start.split("lag")[-1])
                end_idx = int(intf_end.split("lag")[-1])

            # Deconstruct the ranges
            new_intf = [f"{base_intf}{idx}" for idx in range(start_idx, end_idx + 1)]
            intf_list = intf_list + new_intf

        else:
            # not an interface range, just add the intf to the list
            intf_list.append(intf)

    # Add intf_list to VLAN map
    vlan_map[int(vlan_id)] = intf_list

print()
print("VLAN Table:")
print("-" * 25)
print(vlan_map)
print()