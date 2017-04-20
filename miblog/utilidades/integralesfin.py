from math import*
import random


class Trap:
    def __init__(self):
        return
    def funcion_evaluada(self,x,funcion):
        return eval(funcion)

    def trapecios(self,funcion,a,b,n):
        m=Trap()
        h = (b-a)/n
        x0=a
        area=m.funcion_evaluada(x0,funcion)+m.funcion_evaluada(b,funcion)
        for i in range (0,int(n-1)):# de 1 a n-1
            xi=x0+h
            area= area + 2* m.funcion_evaluada(xi,funcion)
            x0=xi
        rest = area * (h/2)
        return(rest)


class monte:
    def __init__(self):
        return

    def funcion_evaluada(self,x,funcion):
        return eval(funcion)

    def montecarlo(self,cota,a,b,puntos):
        m=monte()
        puntosE = 0
        for i  in range (0,int(puntos)):
            x1 = (b-a)*random.random()+a
            y1 = float(cota)*random.random()
            fDeX1 = m.funcion_evaluadax(x1,funcion)
            if(float(y1)<float(fDeX1)):
                puntosE = puntosE + 1
            area = (puntosE/puntos)*(float(b)-float(a))*float(cota)
            return area
