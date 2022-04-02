a =int(input("Enter the num to reverse: "))
rem = 0

while a!=0:
    rem = rem *10 + a%10
    a = a//10
print(rem)