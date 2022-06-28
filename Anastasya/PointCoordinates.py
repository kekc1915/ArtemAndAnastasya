print ('Определите принадлежит ли точка с координатами x,y заштрихованной части плоскости.\n'
'Введите координаты точки x, y:')

horizontal = float (input('Координата x:' ))
vertical = float (input('Координата y:' ))

if (2 <= horizontal <= 4 or -4 <= horizontal <= -2) and -4 <= vertical <= -2:
    print ('Точка с координатами', horizontal, vertical, 'принадлежит заштрихованному промежутку.')
else:
    print ('Точка с координатами', horizontal, vertical, 'не принадлежит заштрихованному промежутку.')
