my_list = [(lambda x:(x*87+12)%16)(i) for i in range(20)]

k = 0
min = int(input())
while len(my_list) != 0:
    x = my_list.pop()
    print(x)
    if x < min:
        min = x
        k += 1
#print(min)
#print(k)

