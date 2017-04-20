from math import*
import random

class Rectangulos:

    def __init__(self):
        return
    def funcion_evaluada(self,x,funcion):
        return eval(funcion)
    def recIzquierda(self,funcion,a,b,n):
        m=Rectangulos()
        h = (b-a)/n
        x0=a
        area =  m.funcion_evaluada(x0,funcion)
        for i in range (0,int(n-1)):
            xi=x0+h
            area= area +  m.funcion_evaluada(xi,funcion)
            x0=xi
        rest = area * h
        return(rest)
    def recDerecha(self,funcion,a,b,n):
        m=Rectangulos()
        h = (b-a)/n
        x0=a
        area =0
        for i in range (1,int(n+1)):
            xi=x0+h
            area= area +  m.funcion_evaluada(xi,funcion)
            x0=xi
        rest = area * h
        return (rest)
    def recMedios(self,funcion,a,b,n):
        m=Rectangulos()
        h = (b-a)/n
        x0=a
        area=0
        for i in range (1,int(n+1)):
            xi=x0+h
            xj=(xi+x0)/2
            area= area +  m.funcion_evaluada(xj,funcion)
            x0=xi
        rest = area * h
        return (rest)
