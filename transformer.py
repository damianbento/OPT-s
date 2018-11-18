#!/usr/bin/python
import math
# Ingreso de variables 
P = input('ingresar la potencia W: ')
fmin = input('ingresar frecuencia minima hz: ')
ep = input('tension de placa en V: ')
Z = input('impedancia de placa ohm: ')
Zs = input('impedancia del parlante ohm: ')
ipmax = input('Corriente placa maxima mA: ')
iprep = input('Corriente de placa en reposo mA: ')
# seccion del nucleo



S = round(math.sqrt(float(P)/float(fmin))*15)
np = round((0.315*ep*100000000)/(fmin*8000*S))
print "seccion Nucleo : ",S
print "Numero de espiras primario : ",np
k = round(math.sqrt(Z/Zs))
print "Relacion de transformacion : ",k
ns = round(np/k)
print "Espiras del Secundario : ",ns
longmagnucle = 6.25*math.sqrt(S)
ipro = float((ipmax-iprep)/2)/1000
satn = (500*np*ipro)/longmagnucle
print "Corriente promedio Continua sat : ",ipro
print "Saturacion del Nucleo tiene que se menor a 4000 Gauss : ",satn
s1 = float(ipmax/2)/2/1000
print "Seccion del alambre primario mm2 : ",s1
Is = round(math.sqrt(P/Zs))
print "Corriente Max secundario A : ",Is
s2 = Is/2
print "Seccion del alambre Secundario mm2 : ",s2