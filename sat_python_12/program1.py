x = 10
t = 1030
# первый способ
print(x)
print('Деньги', x)
print('Деньги', x, '$')
# второй способ
print('Деньги ' + str(x) + '$')
# третий способ
print('Деньги %a$' % x)
# четвертый способ
print(f'Деньги {x}$, время {t}, ')

a = [1, 2, 3, 4, 5]

def timeAlg(len_list, speed_algoritm):
    time = len_list / speed_algoritm 
    return time
    
x=timeAlg(len(a), 3)
print(f'алгоритм Арефьефа {x} млсек')

def angle(x):
    a = 90 - x
    return a, x
    
angle1, angle2 = angle(20)
print(angle1, angle2)
