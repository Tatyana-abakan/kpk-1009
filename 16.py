my_list = [(lambda x:(x*87+12)%16)(i) for i in range(20)]
print(my_list)

min = my_list.pop()
min_number = 1

while len(my_list) > 0:
    x = my_list.pop()

    if x < min:
        min = x
        min_number = 1
    elif x == min:
        min_number += 1
print(min)
print(min_number)
