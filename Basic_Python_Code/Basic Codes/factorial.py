# Normal way

number = 5
fact = 1

if number == 1:
    fact = 1
else:
    while number > 0:
        fact = fact * number
        number = (number - 1)

print(fact)


# Recursive function

def fact(n):
    f = 1
    if n == 1:
        return f
    else:
        while n > 0:
            return n * (fact(n - 1))


print(fact(5))

# fast way

n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(fact)
