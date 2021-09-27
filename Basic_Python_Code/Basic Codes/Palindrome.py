# String Palindrome

str = 'nayan'
pal_str = str[::-1]

if str == pal_str:
    print("String is palindrome")
else:
    print("String is not palindrome")

# Number palindrome

number = 12321
rev = 0
num = number

while num != 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if number == rev:
    print("Palindrome")
else:
    print("Not Palindrome")