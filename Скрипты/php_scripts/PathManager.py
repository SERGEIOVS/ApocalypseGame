import math
from UnitManager import *
import logging

logfilename= 'logs/log.txt'

mylevel = logging.INFO

myformat = '%(asctime)s - %(levelname)s - %(message)s'

my1=logging.basicConfig(filename = logfilename ,level = mylevel , format= myformat)



class Paths():
    def __init__(self,x1,x2,y1,y2,lenght,need):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.lenght = lenght
        self.need = need

x1list = [112,100,315,216]
x2list = [223,200,211,219]
y1list = [114,140,119,228]
y2list = [221,300,420,400]

lenghts = []

for i in range(len(x1list)):
    i = Paths(x1list[i],x2list[i],y1list[i],y2list[i],math.sqrt( ((x2list[i]-x1list[i])**2) +  ((y2list[i]-y1list[i])**2)     ) , math.sqrt( ((x2list[i]-x1list[i])**2) +  ((y2list[i]-y1list[i])**2)     ) )
    lenghts.append(i.lenght)
    
"""    if i.lenght == i.need:
        print('len = ' , str(i.need))
    else:
        print('не равно!')"""
