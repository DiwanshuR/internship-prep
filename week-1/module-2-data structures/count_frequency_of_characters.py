str = input("Enter a string: ")
freq = {}
for char in str:
    freq[char] = freq.get(char, 0) + 1
for char, cnt in freq.items():
    print(f"{char}: {cnt}")
    