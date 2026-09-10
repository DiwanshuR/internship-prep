my_list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
squared_list = list(map(lambda x: x**2, my_list))
print("Squared list:", squared_list)