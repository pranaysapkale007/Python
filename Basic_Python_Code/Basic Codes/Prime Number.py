# number which is only divisible to itself
# 2, 3, 5, 7, 15, 29

number = 3
flag = False

for i in range(2, number):
    if number % i == 0:
        flag = True

if flag:
    print("Number is not prime")
else:
    print("Number is prime")
