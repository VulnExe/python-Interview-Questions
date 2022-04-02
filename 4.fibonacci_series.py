user = int(input(":"))

a= 0
b = 1

if user < 0:
    print("Invalid input")

elif user == 0:
    print(1)

elif user ==1:
    print(b)

else:
    for i in range(1,user):
        c = a+b
        a=b
        b=c
        print(b)

