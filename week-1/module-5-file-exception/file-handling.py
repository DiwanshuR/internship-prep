try:
    with open('temp.txt', 'r') as file:
        content = file.read()
        print(content)  

except FileNotFoundError:
    print("File not found. Please check the file path and try again.")

with open('temp.txt', 'w') as file:
    file.write("This is a sample text written to the file.")    

with open('temp.txt', 'r') as file:
    content = file.read()
    print(content)




    