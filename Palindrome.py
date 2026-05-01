n = int(input("Enter no:" ))

num = n
result = 0

if n < 0 or (n % 10 == 0 and n != 0 ):
    print ("false")

while num > 0:
    last_digit = num % 10
    result = (result * 10) + last_digit
    num = num // 10

print(n == result)