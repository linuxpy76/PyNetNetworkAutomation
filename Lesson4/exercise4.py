with open("arubacx_show_vlan.txt") as f:
    data = f.readlines()

vlans = {}

for line in data:
    if "-----" in line:
        continue
    if "Name" and "Type" in line:
        continue

    line_elements = line.split()
    vlan_id = line_elements[0]
    interfaces_whole = line_elements[5]
    interface_groups = interfaces_whole.split(",")

    for interface_group in interface_groups:
        numbers = []
        if "-" not in interface_group:
            interface = interface_group
            vlans[vlan_id] = interface
        elif "-" in interface_group:
            interfaces = interface_group.split("-")
            for i in interfaces:
                number = i.split("/")
                numbers.append(number[2])
                number.pop()
            for i in range(int(numbers[0], (int(numbers[1] + 1)))):
                
                interface = str('/'.join(i))
                vlans[vlan_id] = 
                if "lag" in i:
                  number = int(''.join(filter(str.isdigit, i)))
        else:
            print("error")
