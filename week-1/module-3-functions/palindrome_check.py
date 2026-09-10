str = input("Enter a string : ")

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(f"The string '{str}' is a palindrome: {is_palindrome(str)}")
