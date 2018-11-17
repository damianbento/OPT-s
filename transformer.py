#!/usr/bin/python
import math
P = input('ingresar la potencia W: ')
fmin = input('ingresar frecuencia minima hz: ')
ep = input('tension de placa en V: ')


print "Seccion del nucleo ", round(math.sqrt(float(P)/float(fmin))*10, 2), "cm2"

