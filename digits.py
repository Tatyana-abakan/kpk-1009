x = int(input())
while x:
    digit = x%10
    print(digit, x)
    x //= 10
