from ast import While


# = float(input('Введите переменную для вычисления:'  ))
n = 10


for i in range(1, n + 1):
    Result = (i / (i + 1)) * ((i + 2) / (i + 3))
    print (Result)
print ('Конец цикла')    