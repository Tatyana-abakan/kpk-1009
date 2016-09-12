x = int(input())
n = 0
s = 0
p = 1

while x:
    digit = x%10
    n += 1
    s += digit
    p *= digit
    x //= 10
print('Количество цифр числа', n)
print('Сумма цифр числа', s)
print('Произведение цифр числа', p)
print('Среднее арифметическое', s/n)
