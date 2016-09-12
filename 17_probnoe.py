my_list = [(lambda x:(x*73+51)%100)(i) for i in range(30)] #генерируем список из 30 элементов
print(my_list)

max1 = my_list.pop()
max2 = my_list.pop()
k = 1

if max2 > max1:
    max1, max2 = max2, max1

while len(my_list) > 0:
    num = my_list.pop()
    if num > max1:
        max2 = max1
        max1 = num
        k = 1
    elif num > max2:
        max2 = num
        k += 1
print(max1, max2)
#print(k)
print('Максимум', max2, 'достигается', k, 'раз.')
