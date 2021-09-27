# fib series 0,1,1,2,3,5,8,13 .....

series = 10

a = 0
b = 1

print(a, end=",")
print(b, end=",")

for i in range(2, series):
    c = a + b
    print(c, end=",")
    a = b
    b = c