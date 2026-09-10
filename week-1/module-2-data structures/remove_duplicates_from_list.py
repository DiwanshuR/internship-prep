my_list = []
while True:
    ele = input("Enter element: ")
    if ele == "done":
        break
    my_list.append(ele)

my_set = set(my_list)
print(my_set)

# by list complrehension 
# my_list = [int(x) for x in input("Enter elemenets seperated nby space").split()]