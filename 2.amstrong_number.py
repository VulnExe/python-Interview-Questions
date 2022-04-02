user = int(input(":"))

sum = 0

test = user

while test>0:
    a = test %10
    sum = sum + a ** 3
    test = test//10
if user == sum:
    print("amstrong")

else:
    print("not")