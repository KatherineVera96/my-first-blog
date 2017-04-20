def graficar(funcion, rango):
    """Grafica una función representada por una ecuación de una incógnita, la cual es X"""
    import matplotlib.pyplot as pplot
    from py_expression_eval import Parser

    parser = Parser()
    funcion = str(funcion)
    pFuncion = parser.parse(funcion)
    x = rango
    i = x[0]
    y = []
    step = rango[1]-rango[0]
    if step < 0:
        step = -step
    while i <= x[len(x) - 1]:
        y.append(pFuncion.evaluate({"x": i}))
        i += step

    pplot.plot(x, y)
    pplot.show()

def frange(start, stop, step):
    i = start
    floats = []
    while i < stop:
        floats.append(i)
        i += step
    return floats


"""import math
a = math.degrees(0)
b = math.degrees(180)
rango = frange(a, b, 0.1)
#print(rango)
graficar('tan(x)', rango)"""
#print(evaluar(funcion='x^4', valor=1, variable='x'))


def derivada(funcion,variable = 'x', veces = 1, evaluar = None, radian=False):
    """deriva la funcion dada el número de veces especificada"""
    from sympy import diff
    from decimal import Decimal
    import math

    i = 0
    dx = funcion

    dx = diff(dx, variable, veces)
    if evaluar != None:
        if(not radian):
            evaluar = math.radians(evaluar)
        return dx.subs(variable, evaluar).evalf()
    return Decimal(dx)

#print(derivada(funcion = 'sin(x)', veces = 1, variable='x', evaluar=90))




