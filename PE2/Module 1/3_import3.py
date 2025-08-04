from math import*

r = 5
area = pi * (r ** 2)
circ = 2 * pi * r
print('Area is',area)
print('Circumference is',circ)

###################################
import math as m

F = 100
Fx = F * m.cos(m.pi/6)
Fy = F * m.sin(m.pi/6)
print('For a force of magnitude',str(F)+'N')
print('its x and y components at 30 deg are :',Fx,Fy, sep='\n')

#########################################
from math import tan as tg

print('tangent of 45 deg is ',tg(m.pi/4))       # from module import n as a, m as b, o as c
