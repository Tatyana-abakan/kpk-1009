my_list = [(lambda x:(x*87+12)%100)(i) for i in range(20)]
s = 0
s_2 = 0
k = 0
while len(my_list) != 0:
    x = my_list.pop()
    #print(float(round(x, 5)))
    #print(len(my_list))
    s += x
    s_2 += x*x
    k += 1
print(s)
print(s_2)
print(k)

srednee = s/k
srednee_2 = s_2/k
otklonenie = (srednee_2 - srednee**2)**0.5
print('Среднее значение:', srednee, '+-', round(otklonenie, 5))

