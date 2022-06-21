from ast import If


print ('Введите три вещественных числа')
CompareOne = float(input('Первое число: ' ))
CompareTwo = float(input('Второе число: ' ))
Comparethree = float(input('Третье число: ' ))
if CompareOne < CompareTwo < Comparethree:
    print ('Неравенство' + CompareOne < CompareTwo < Comparethree + 'выполняется!')
else:
    print ('Неравенство не выполняется(')