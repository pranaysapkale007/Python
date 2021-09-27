# number that is equal to sum of its digit
# 0, 1, 153, 370, 371, 407

num = 370
n = num
arm = 0
while n != 0:
    rem = n % 10
    arm = arm + rem**3
    n = n // 10

if num == arm:
    print("This is armstrong")
else:
    print("This is not armstrong number")