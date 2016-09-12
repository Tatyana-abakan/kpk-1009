def generate_number():
    return lambda random_seed: (random_seed*693 + 5)%100
number = generate_number()

s = 0
n = 0
i = 1

while number(i) != 0:
    if number(i)%4 ==0:
        n += 1
        s += number(i)
    i += 1
print('Среднее арифметическое равно=', s/n)
