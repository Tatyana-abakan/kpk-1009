def pseudo_list():
    for i in range(N):
        yield (i*9876+1024)%1000
N = 10**6 + 1
A = pseudo_list()
print(pseudo_list)


# Элементы данной последовательности следует перебирать так:
#for x in A:
    #pass  # работа с очередным числом x
