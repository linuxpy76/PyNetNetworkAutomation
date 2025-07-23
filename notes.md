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