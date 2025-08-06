from rich import print

filename = "arubacx_show_vlan.txt"
with open(filename) as f:
    data = f.read()

# Initialize dictionary outside of main for-loop.
vlan_map = {}
for line in data.splitlines():
    # Skip header lines
    if "----" in line:
        continue
    if "Status" in line and "Reason" in line:
        continue

    vlan_id, vlan_name, status, reason, vlan_type, interfaces = line.split()
    intf_groups = interfaces.split(",")

    # Construct list of interfaces associated with given VLAN-ID
    intf_list = []
    for intf in intf_groups:
        # Check for ranges
        if "-" in intf:
            intf_start, intf_end = intf.split("-")

            # Dropping the last character will give us the base interface
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

            # Deconstruct the ranges i.e. each individual interface listed
            new_intf = [f"{base_intf}{idx}" for idx in range(start_idx, end_idx + 1)]
            intf_list = intf_list + new_intf

        else:
            # not an interface range, just add the intf to the list
            intf_list.append(intf)

    # intf_list is now fully constructed, add it to the VLAN map.
    # convert the list to a set.
    vlan_map[int(vlan_id)] = set(intf_list)

print()
print("Section a.")
print("-" * 25)
shared_intf = vlan_map[1] & vlan_map[2] & vlan_map[3]
print(f"Common interfaces VLAN1, VLAN2, VLAN3: {sorted(shared_intf)}")
print()

# Different ways you can do this, but here I use a set comprehension
all_intf = {intf for intf_set in vlan_map.values() for intf in intf_set}
print()
print("Section b.")
print("-" * 25)
print(f"All interfaces that belong to a VLAN:\n{sorted(all_intf)}")
print()

# All the interfaces associated with VLAN12 and VLAN13
vlan_12_13 = vlan_map[12] | vlan_map[13]
print()
print("Section c.")
print("-" * 25)
print(f"All interfaces associated with VLAN12 or VLAN13 (in either):\n{sorted(vlan_12_13)}")
print()