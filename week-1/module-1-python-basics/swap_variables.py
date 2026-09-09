a = 4
b = "Hello"

print(f"Before swap : a = {a} , b = {b}")

# temporary variable
c = a
a = b

print(f"After swap : a = {a} , b = {c}")

# another way -> tuple unpacking
x = "Hello"
y = 20

print(f"Before swap : x = {x} , y = {y}")
x,y = y,x
print(f"After swap : x = {x} , y = {y}")