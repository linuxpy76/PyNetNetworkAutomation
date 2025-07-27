header = "-" * 40

# Standard read method
f = open("show_version.txt", mode="r")
data = f.read()
f.seek(0)
print("Read first line")
print(header)
print(f.readline())
print("Read entire file")
print(header)
print(data)
f.close()

print(header)
# Context manager method
with open("show_version.txt", mode="r") as f:
    data = f.read()
    f.seek(0)
    print("Read first line")
    print(header)
    print(f.readline())
    print("Read entire file")
    print(header)
    print(data)