#Иморт модуля
import math
print(math.pi)

def circle_length(radius):
    import math
    return math.pi * radius * 2

print(circle_length(3))

#Импорт атрибутов
from math import pi, sqrt
print(pi)
print(sqrt(4))

from math import *
print(floor(3.8))
print(ceil(3.2))

#Импорт под псевдонимом
import math as m
print(m.e)

from math import floor as f, ceil as c
print(f(3.5))
print(c(3.5))

#Выполнение кода при импорте
#Example 1

#Пакеты
#Example 2

#Относительный и абсолютный импорт
#Example 3
import sys
print(sys.path) #увидеть корневые директории



