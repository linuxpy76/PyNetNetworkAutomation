# PyNet Python for Network Engineers

## Lesson 1

### You can multiply strings

```py
var = "text" * 3
>>> texttexttext
```

### You can left, right and center align stuff using f-strings

```py
var = "Hello World!"

# Left align with 20 spacing
print(f"{'left align':<20} {var:<20}")

# Right align with 20 spacing
print(f"{'right align':>20} {var:>20}")

# Center align with 12 spacing
print(f"{'center align':^12} {var:^20}")
```

### Striping white space off of strings with strip()

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

### You can split strings with split()

```py
line = "Processor board ID FAL127990LA"

var1, var2, var3, var4 = line.split()
print(var4)

words = line.split()
print(words[3])
```

### Concatination with standard, f-strings, and format() methods

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

### You can round numbers

```py
round(my_var,2)
```

```py
i = 0
i = i + 1
i += 1
i -= 1
```

### Booleans

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

### Reading files

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

### Writing to files, this is destructive

```py
f = open("test_file.txt", "w")
f.write("Testing...\n")
f.write("Testing...\n")
f.flush()
f.close()
```

### Appending to a file

```py
f = open("test_file.txt", "a")
f.write("Hello again\n")
f.flush()
f.close()
```
### Context Managers

```py
with open("show_version.txt", mode="r") as f:
    data = f.read()
```

### Lists

Data types don't have to be the same

Zero based indices
```py
my_list = ['foo', 1, 'hello', [], None, 2.7]
my_list[0]
my_list[-1]
```

### Length and Range

```py
# Get length of list
len(my_list)
# Make a list with range 10 = 0-9
list(range(10))
# Change starting value
list(range(1,5))
```

### List methods

```py
append() # add to end of list
clear() # remove all elements
copy() # create another copy of a list to point to same list
count() # count number of occurences of element
extend() # add list to end of list
index() 
insert()
pop() # pop things off the list
remove()
reverse()
sort()
```

## Lesson 3

### Conditionals

Evaluates to True or False

```py
ip_addr = "10.1.1.1"

if "10.1" in ip_addr:
    print("Found Address")

# if, elif or else

if expression:
    print(1)
elif other_expression:
    print(2)
else:
    print(3)
```

```py
a == b
a != b
a < b
a <= b
a > b
a >= b

a and b
a or b
not a
a is b
a is not b
a in b
```

### For Loops

```py
for loop_var in iterator:
    # do something
    pass
```

```py
list = [
    1,
    2,
    3,
    4,
    5
]

for num in list:
    print(num)
```

#### Break

You can break out of for loops

```py
for i in range(10):
    print(i)
    if i == 5:
        break
print(f"Outside loop --> {i}")
```

#### Continue

When 'continue' is executed, immediately jump back to the top of the for loop

```py
for i in range(10):
    if i == 5:
        continue
    print(i)
print(f"Outside loop --> {i}")
```

#### Nesting loops

```py
# List of tuples
data_centers = [
    ("sf1", "10.1.1."),
    ("sf2", "10.1.2.")
]

# for loop w/ unpacking
for dc, base_addr in data_centers:
    # inner loop
    for net_addr in range(1,5):
        print(f"{dc} --> {base_addr}{net_addr}")
```

#### Enumerate

```py
data_centers = ["sf1", "sf2", "la1", "la2", "dallas"]

for i, dc in enumerate(data_centers):
    print(f"{i} --> {dc}")
```

#### Pass

```py
for i in range(10):
    pass
```

#### Else

Else executes if there is no break condition that is met

```py
for i in range(10):
    print(i)
    if i = 12:
        break
# no-break
else:
    print("No 'break' happened")
```

### While Loops

While loops enter and stay in the loop as long as the expression is True

```py
i = 0
while expression:
    print("A message")
    print("A second message")
    i += 1
    if i = 4:
        break
```

#### For vs While

For loops are for looping over collections of things (think "for each")

While loops are event based - a condition to enter the loop and a condition to exit the loop.

### List Comprehensions

An easy way to dymanically create a list

```py
# An existing list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# A list comprehension
[x**2 for x in my_list]

# Can include conditionals
[x for x in my_list if x % 2 == 0]

# Multiple loops
[f"172.16.{x}.{y}" for x in range(10) for y in range(3)]

# Make it more readable
[f"172.16.{x}.{y}"
    for x in range(10)
    for y in range(3)]

# One might question your sanity
# Conditionals w/ multiple for loops
[f"172.16.{x}.{y}"
    for x in range(10)
    for y in range(3)
    if x == 9]
```

### Generator Expressions

A generator in Python is a function constructed in a certain way such that each time that is called in a context of a loop it will return (yield) the next value.

```py
def gen(n):
    i = 0
    while i < n:
        yield i
        i += 1

for val in gen(4):
    print(val)
```

```py
my_generator = (x**2 for x in range(10))
type(my_generator)

for val in my_generator:
    print(val)
```

IP generator

```py
base_addr = "10.77"
ip_generator = (
    f"{base_addr}.{x}.{y}"
    for x in range(10,13)
    for y in range(2,11)
)

for ip_addr in ip_generator:
    print(ip_addr)
```

Once generators are used they will become exhausted and cannot be used again.

## Lesson 4

### Sets

There are no indices (sets are not ordered)

#### Adding elements to a list

```py
addresses = {"192.168.100.1", "192.168.100.2"}
addresses.add("10.1.1.1")
addresses
>>> {'10.1.1.1', '192.168.100.1', '192.168.100.2'}
```

#### Updating a list with another list

```py
addresses.update({'10.1.1.1', '10.1.1.2'})
addresses
{'10.1.1.1', '10.1.1.2', '192.168.100.1', '192.168.100.2'}
```

