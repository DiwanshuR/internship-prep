my_list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]


for i in range(len(my_list)):
    
    for j in range(i + 1, len(my_list)):
        if my_list[i] > my_list[j]:
            
            my_list[i], my_list[j] = my_list[j], my_list[i]

print("Sorted list:", my_list)

