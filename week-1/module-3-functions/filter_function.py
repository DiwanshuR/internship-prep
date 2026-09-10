my_list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

evens = list(filter(lambda x: x % 2 == 0, my_list))
print("Even numbers:", evens)