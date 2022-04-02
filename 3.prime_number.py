user = int(input(":"))

flag = False

for i in range(2,user):
    if user%i==0:
        flag=True
        break
if flag:
    print("Not a prime number")

else:
    print("Prime number")


