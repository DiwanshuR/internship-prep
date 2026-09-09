evens = 0
odds = 0
numbers = [1,2,3,4,5,6,7,8,9,10, 11, 12, 13,14]

for num in numbers:
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

print(f"Even numbers: {evens}")
print(f"Odd numbers: {odds}")