import re

with open("show_version.txt", mode="r") as f:
    data = f.read()

model_number = r"(?P<model>\S+)"
serial_number = r"(?P<serial>\S+)"

m = re.search(rf"^cisco\s{model_number}", data, flags=re.MULTILINE)
s = re.search(rf"^Processor.+?{serial_number}$", data, flags=re.MULTILINE)

print(f"Cisco model number: " + m.group("model"))
print(f"Cisco serial number: " + s.group("serial"))