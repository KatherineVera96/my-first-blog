def simpson13(funcion, a, b, n, variable = 'x'):
    """integra utilizando el método de simpson 1/3"""
    from sympy import diff
    area = 0
    a = float(a)
    b = float(b)
    n = float(n)    
    if n%2 == 1:
        n += 1
    h = (b-a)/n
    i = float(0)
    while i < n:
        x0 = a + h*i
        x1 = x0 + h
        x2 = x0 + 2*h
        area += (h/3)*(diff(funcion, variable, 0).subs(variable, x0).evalf()+(4*diff(funcion, variable, 0).subs(variable, x1).evalf()+diff(funcion, variable, 0).subs(variable, x2).evalf()))
        i += 2
    return area

##print(simpson13('x^2', 1, 7, 6))

def simpson38(funcion, a, b, n, variable = 'x'):
    """integra utilizando el método de simpson 3/8"""
    area = 0
    from sympy import diff
    if n%3 != 0:
        n += 3 - n%3

    h = (b-a)/n
    i = 0
    while i < n:
        x0 = a + h*i
        x1 = x0 +h
        x2 = x0 + 2*h
        x3 = x0 + 3*h
        area += ((3*h)/8)*(diff(funcion, variable, 0).subs(variable, x0).evalf()+3*diff(funcion, variable, 0).subs(variable, x1).evalf()+3*diff(funcion, variable, 0).subs(variable, x2).evalf() + diff(funcion, variable, 0).subs(variable, x3).evalf())
        i += 3

    return area

#print(simpson38('x^2', 1, 5, 6))

def montecarlo (funcion, a, b, n, m, variable = 'x'):
    """integra segun el metodo de montecarlo"""
    from sympy import diff
    import random as r

    a = float(a)
    b = float(b)
    n = float(n)
    m = float(m)

    i = 0
    nExitos = 0
    while i < n:
        xi = (b-a)*r.random()
        yi = m*r.random()
        if yi <= diff(funcion, variable, 0).subs(variable, xi).evalf():
            nExitos += 1
        i += 1

    return(b-a)*m*(nExitos/n)
    
#print(montecarlo('x^2', 1, 5, 8000, 25))

def rectangulosIzq(funcion, a, b, n, variable = 'x'):
    """integra utilizando el método de rectangulos con extremo izquierdo"""
    from sympy import diff
    area = 0
    a = float(a)
    b = float(b)
    n = float(n)    
    h = (b-a)/n
    i = float(0)
    while i < n:
        x = a + h*i
        area += h*(diff(funcion, variable, 0).subs(variable, x).evalf())
        i += 1
    return area

#print(rectangulosIzq('-x^2 + 9', 0, 3, 6))

def rectangulosMed(funcion, a, b, n, variable = 'x'):
    """integra utilizando el método de rectangulos con punto medio"""
    from sympy import diff
    area = 0
    a = float(a)
    b = float(b)
    n = float(n)    
    h = (b-a)/n
    i = float(1)
    while i <= n:
        x = (a + h*i) -(h/2)
        area += h*(diff(funcion, variable, 0).subs(variable, x).evalf())
        i += 1
    return area

#print(rectangulosMed('-x^2 + 9', 0, 3, 6))

def rectangulosDer(funcion, a, b, n, variable = 'x'):
    """integra utilizando el método de rectangulos con extremo derecho """
    from sympy import diff
    area = 0
    a = float(a)
    b = float(b)
    n = float(n)    
    h = (b-a)/n
    i = float(1)
    while i <= n:
        x = a + h*i
        area += h*(diff(funcion, variable, 0).subs(variable, x).evalf())
        i += 1
    return area

#print(rectangulosDer('-x^2 + 9', 0, 3, 6))

def trapecios(funcion, a, b, n, variable = 'x'):
    """integra utilizando el método de trapecios"""
    from sympy import diff
    
    a = float(a)
    b = float(b)
    n = float(n)    
    h = (b-a)/n
    i = float(1)
    area = (diff(funcion, variable, 0).subs(variable, a).evalf())+(diff(funcion, variable, 0).subs(variable, b).evalf())
    while i < n:
        x = a + h*i
        area += 2*(diff(funcion, variable, 0).subs(variable, x).evalf())
        i += 1
    area=area*(h/2)
    return area

print(trapecios('-x^2 + 9', 0, 3, 6))

#print(trapecios('x^2', 1, 7, 6))
