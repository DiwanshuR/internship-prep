num = int(input("Enter a number: "))
is_prime = True
if num < 2:
    is_prime = False
elif num == 2:
    is_prime = True 
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

print(f"Is it prime? {is_prime}")