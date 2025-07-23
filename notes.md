# PyNet Python for Network Engineers

## Lesson 1

You can multiply strings

```py
var = "text" * 3
>>> texttexttext
```

You can left, right and center align stuff using f-strings

```py
var = "Hello World!"

# Left align with 20 spacing
print(f"{'left align':<20} {var:<20}")

# Right align with 20 spacing
print(f"{'right align':>20} {var:>20}")

# Center align with 12 spacing
print(f"{'center align':^12} {var:^20}")
```

Striping white space off of strings with strip()

```py
" Hello World! ".strip()
>>> 'Hello World!'

" Hello World! ".rstrip()
>>> ' Hello World!'

" Hello World! ".lstrip()
>>> 'Hello World! '

# printing with repr() shows white space
print(repr(" Hello World! ")).rstrip()
>>> ' Hello World!'
```

You can split strings with split()

```py
line = "Processor board ID FAL127990LA"

var1, var2, var3, var4 = line.split()
print(var4)

words = line.split()
print(words[3])
```

Concatination with standard, f-strings, and format() methods

```py
ip_addr = "10.12.17.1"
mac_addr = "0024.c4e9.48ae"
print()
print("String concatenation")
print(ip_addr + " --> " + mac_addr)
print()
print("f-strings")
print(f"{ip_addr} --> {mac_addr}")
print()
print("format() method")
print("{} --> {}".format(ip_addr, mac_addr))
print()
```

## Lesson 2

You can round numbers

```py
round(my_var,2)
```

```py
i = 0
i = i + 1
i += 1
i -= 1
```

Booleans

```py
my_value = None

val1 = True
val2 = False

if val1 and val2:
    print("Hello")

if val1 or val2:
    print("World")

if my_value is None:
    print("Whatever")

# Get opposite value
not val1
not val2

bool(val1)

```

Reading files

```py
f = open(r"..\requirements.txt", mode="r")
data = f.read()


f.readline()
data = f.readlines()
len(data)
type(data)
f.seek(0)

f.close()
```

Writing to files, this is destructive

```py
f = open("test_file.txt", "w")
f.write("Testing...\n")
f.write("Testing...\n")
f.flush()
f.close()
```