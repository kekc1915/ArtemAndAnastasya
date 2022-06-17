from ast import Compare
from logging import exception

while True:
        Number = input("Введите число или стоп для выхода:" )
        if Number == 'стоп':
            print('Пока!')
            break
        else:
            try:
                Number = float(Number)
            except:
                print('Введено некоректное значение!')
                continue
            if Number <= 3 and Number >= -5:
                print(Number, 'принадлежит заданному интервалу')
            else:
                print(Number, 'не принадлжеит заданному промежутку')

