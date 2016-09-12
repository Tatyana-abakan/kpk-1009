my_list = [(lambda x:(x*296+2410)%4096)(i) for i in range(2000)] #генерируем список из 30 элементов
print(my_list)

min1 = my_list.pop()
min2 = my_list.pop()
k = 0
m = 0

if min2 < min1:
    min1, min2 = min2, min1

while len(my_list) > 0:
    num = my_list.pop()

    if num < min1:
        min2 = min1
        min1 = num
        print(min2)
        print(min1)

    elif num < min2:
        min2 = num
        print(min2)

print(min1, min2)

print('Минимум', min1, 'достигается', k, 'раз-а.')
print('Минимум', min2, 'достигается', m, 'раз-а.')
