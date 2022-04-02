user = str(input(":"))

copy = user

act = copy[::-1]

if user == act:
    print("Palindrome")

else:
    print("not a palindrome")
