#генерируем список из 2000 элементов
my_list = [(lambda x:(x*296+2410)%4096)(i) for i in range(2000)]

# начальное значение для временного минимума
min1_value = min2_value = 10000
min1_number = min2_number = 0

while my_list:
    x = my_list.pop()
    if x < min1_value:
        min2_value = min1_value
        min2_number = min1_number
        min1_value = x
        min1_number = 1
    elif x == min1_value:
        min1_number += 1
    elif x < min2_value:
        min2_value = x
        min2_number = 1
    elif x == min2_value:
        min2_number += 1

print(min2_number)
