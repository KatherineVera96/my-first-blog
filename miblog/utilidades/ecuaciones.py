def biseccion (funcion, a, b, tolerancia):
    from decimal import Decimal
    from sympy import diff
    tolerancia = Decimal(tolerancia)
    if not str(tolerancia).isdigit():
        if (not (str(tolerancia)[0:1] == '+' or str(tolerancia)[0:1] == '-')) or (not (str(tolerancia)[1:].isdigit())):
            auxDec = str(tolerancia)
            if str(tolerancia)[0:1] == '+' or str(tolerancia)[0:1] == '-':
                auxDec = str(tolerancia)[1:]
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():
                print("Ingrese un valor numérico");
                return False
    if not str(a).isdigit():
        if (not (str(a)[0:1] == '+' or str(a)[0:1] == '-')) or (not (str(a)[1:].isdigit())):
            auxDec = str(a)
            if str(a)[0:1] == '+' or str(a)[0:1] == '-':
                auxDec = str(a)[1:]
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():
                print("Ingrese un valor numérico");
                return False
    if not str(b).isdigit():
        if (not (str(b)[0:1] == '+' or str(b)[0:1] == '-')) or (not (str(b)[1:].isdigit())):
            auxDec = str(b)
            if str(b)[0:1] == '+' or str(b)[0:1] == '-':
                auxDec = str(b)[1:]
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():
                print("Ingrese un valor numérico");
                return False
    if a >= b:
        print('a debe ser el límite inferior, es decir, menor que b.')
        return False
    try:
        funcion = str(funcion)
        a = float(a)
        b = float(b)
        tolerancia = float(tolerancia)

        if (diff(funcion, 'x', 0).subs('x', a).evalf()*diff(funcion, 'x', 0).subs('x', b).evalf()) > 0:
            print("La funcion no tiene raices en el intervalo dado")
            return None
        rAnt = 0
        rAct = (b+a)/2
        er = tolerancia + 1
        numeroIteraciones = 100
        resultado = []
        i = 1
        if diff(funcion, 'x', 0).subs('x', rAct).evalf() == 0 and i == 1:
            rIteracion = [str(i), str(rAct), str(a), str(b), str(0)]
            resultado.append(rIteracion)
        while diff(funcion, 'x', 0).subs('x', rAct).evalf() != 0 and tolerancia < er and i <= numeroIteraciones:

            if (diff(funcion, 'x', 0).subs('x', a).evalf()*diff(funcion, 'x', 0).subs('x', rAct).evalf()) < 0:
                b = rAct
            else:
                a = rAct

            rAnt = rAct
            rAct = (b+a)/2

            if rAct == 0:
                if rAnt > a:
                    rAct += 0.00000000000000000000000000000000000000001
                else:
                    rAct -= 0.00000000000000000000000000000000000000001

            er = (rAnt - rAct)/rAct
            if er < 0:
                er = -er
            i += 1
            rIteracion = [str(i-1), str(rAct), str(a), str(b), str(er)]
            resultado.append(rIteracion)
            #print('I= ' + str(i-1) + ' Raiz= ' + str(rAct) + ' [' + str(a) +'-'+str(b)+']' + 'error: ' + str(er))
    except Exception as e:
        print('Hubo un error, probablemente en la ecuacion')
        print(e.args)
        return False



    return resultado

#print(biseccion('x-2',1,4,0.01))

def reglaFalsa (funcion, a, b, tolerancia):
    from decimal import Decimal
    from sympy import diff
    tolerancia = Decimal(tolerancia)
    if not str(tolerancia).isdigit():
        if (not (str(tolerancia)[0:1] == '+' or str(tolerancia)[0:1] == '-')) or (not (str(tolerancia)[1:].isdigit())):
            auxDec = str(tolerancia)
            if str(tolerancia)[0:1] == '+' or str(tolerancia)[0:1] == '-':
                auxDec = str(tolerancia)[1:]
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():
                print("Ingrese un valor numérico");
                return False
    if not str(a).isdigit():
        if (not (str(a)[0:1] == '+' or str(a)[0:1] == '-')) or (not (str(a)[1:].isdigit())):
            auxDec = str(a)
            if str(a)[0:1] == '+' or str(a)[0:1] == '-':
                auxDec = str(a)[1:]
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():
                print("Ingrese un valor numérico");
                return False
    if not str(b).isdigit():
        if (not (str(b)[0:1] == '+' or str(b)[0:1] == '-')) or (not (str(b)[1:].isdigit())):
            auxDec = str(b)
            if str(b)[0:1] == '+' or str(b)[0:1] == '-':
                auxDec = str(b)[1:]
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():
                print("Ingrese un valor numérico")
                return False
    if a>b:
        print('Ingrese bien los limites')
        return False
    try:
        funcion = str(funcion)
        a = float(a)
        b = float(b)
        tolerancia = float(tolerancia)
        funcion = str(funcion)
        if (diff(funcion, 'x', 0).subs('x', a).evalf()*diff(funcion, 'x', 0).subs('x', b).evalf()) > 0:
            print("La funcion no tiene raices en el intervalo dado")
            return None

        rAnt = 0
        rAct = ((a*diff(funcion, 'x', 0).subs('x', b).evalf())-(b*diff(funcion, 'x', 0).subs('x', a).evalf()))/(diff(funcion, 'x', 0).subs('x', b).evalf()-diff(funcion, 'x', 0).subs('x', a).evalf())
        er = tolerancia + 1
        numeroIteraciones = 100
        print(rAct)
        resultado = []
        print(diff(funcion, 'x', 0).subs('x', rAct).evalf())
        i = 1
        if diff(funcion, 'x', 0).subs('x', rAct).evalf() == 0 and i == 1:
            rIteracion = [str(i), str(rAct), str(a), str(b), str(0)]
            resultado.append(rIteracion)

        while diff(funcion, 'x', 0).subs('x', rAct).evalf() != 0 and tolerancia < er and i <= numeroIteraciones:
            print('CHECKPOINT 1')
            print(i-1)
            if (diff(funcion, 'x', 0).subs('x', a).evalf()*diff(funcion, 'x', 0).subs('x', b).evalf()) < 0:
                b = rAct
            else:
                a = rAct

            rAnt = rAct
            rAct = ((a*diff(funcion, 'x', 0).subs('x', b).evalf())-(b*diff(funcion, 'x', 0).subs('x', a).evalf()))/(diff(funcion, 'x', 0).subs('x', b).evalf()-diff(funcion, 'x', 0).subs('x', a).evalf())
            if rAct == 0:
                if rAnt > a:
                    rAct += 0.00000000000000000000000000000000000000001
                else:
                    rAct -= 0.00000000000000000000000000000000000000001
            er = (rAnt - rAct)/rAct
            if er < 0:
                er = -er
            i += 1
            rIteracion = [str(i-1), str(rAct), str(a), str(b), str(er)]
            resultado.append(rIteracion)
            print('Raiz: ' + str(rAct) + ' Error: ' + str(er) + ' Iteracion: ' + str(i))
    except Exception as e:
        print('Hubo un error, probablemente en la ecuacion')
        print(e.args)
        return False
    return resultado

#print(reglaFalsa("sin(x)", -2, 3, 0.01))
#print(reglaFalsa("sin(x)", -2, 3, 0.01))

def newtonRaphson(funcion, x0, tolerancia, radianes = False, variable = 'x'):
    from decimal import Decimal
    tolerancia = Decimal(tolerancia)
    x0 = int(x0)
    if not str(tolerancia).isdigit():
        if (not (str(tolerancia)[0:1] == '+' or str(tolerancia)[0:1] == '-')) or (not (str(tolerancia)[1:].isdigit())):
            auxDec = str(tolerancia)
            if str(tolerancia)[0:1] == '+' or str(tolerancia)[0:1] == '-':
                auxDec = str(tolerancia)[1:]
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():
                print("Ingrese un valor numérico");
                return False
    if not str(x0).isdigit():
        if (not (str(x0)[0:1] == '+' or str(x0)[0:1] == '-')) or (not (str(x0)[1:].isdigit())):
            auxDec = str(x0)
            if str(x0)[0:1] == '+' or str(x0)[0:1] == '-':
                auxDec = str(x0)[1:]
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():
                print("Ingrese un valor numérico");
                return False
    if not(radianes == True or radianes == False):
        print('Radianes es una variable booleana para decidir si se utilizaran radianes o grados')
        return False
    if variable.lower() != ('x' or 'y' or 'z'):
        print('La variable debe ser x, y, o z')
        return False

    try:
        from sympy import diff
        import math
        iteraciones = 100
        errorRelativo = tolerancia+1
        i = 0
        xi = x0
        xAnt = x0
        resultado = []
        while errorRelativo >= tolerancia and i < iteraciones:
            print(diff(funcion, variable, 0).subs(variable, xAnt).evalf()/diff(funcion, variable, 1).subs(variable, xAnt).evalf())
            xi = xAnt - (diff(funcion, variable, 0).subs(variable, xAnt).evalf()/diff(funcion, variable, 1).subs(variable, xAnt).evalf())
            if xi == 0:
                xi += 0.00000000000000000000000000001
            errorRelativo = math.fabs((xAnt-xi)/(xi))
            i += 1
            xAnt = xi
            print('Raiz= '+ str(xi) + ' error= ' + str(errorRelativo) + ' iteracion= ' + str(i))
            rIteracion = [str(i), str(xi), str(errorRelativo)]
            resultado.append(rIteracion)
        return resultado
    except Exception as e:
        print('Hubo un error, probablemente en la ecuacion')
        print(e.args)



#print(newtonRaphson('sin(x)', '1', '0.01', True, 'x'))

def secante(funcion, x0, x1, tolerancia, radianes = False, variable = 'x'):
    from decimal import Decimal
    tolerancia = Decimal(tolerancia)
    x0 = int(x0)
    x1 = int(x1)
    if not str(tolerancia).isdigit():
        if (not (str(tolerancia)[0:1] == '+' or str(tolerancia)[0:1] == '-')) or (not (str(tolerancia)[1:].isdigit())):
            auxDec = str(tolerancia)
            if str(tolerancia)[0:1] == '+' or str(tolerancia)[0:1] == '-':
                auxDec = str(tolerancia)[1:]
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():
                print("Ingrese un valor numérico");
                return False
    if not str(x0).isdigit():
        if (not (str(x0)[0:1] == '+' or str(x0)[0:1] == '-')) or (not (str(x0)[1:].isdigit())):
            auxDec = str(x0)
            if str(x0)[0:1] == '+' or str(x0)[0:1] == '-':
                auxDec = str(x0)[1:]
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():
                print("Ingrese un valor numérico");
                return False
    if not str(x1).isdigit():
        if (not (str(x1)[0:1] == '+' or str(x1)[0:1] == '-')) or (not (str(x1)[1:].isdigit())):
            auxDec = str(x1)
            if str(x1)[0:1] == '+' or str(x1)[0:1] == '-':
                auxDec = str(x1)[1:]
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():
                print("Ingrese un valor numérico");
                return False
    if not(radianes == True or radianes == False):
        print('Radianes es una variable booleana para decidir si se utilizaran radianes o grados')
        return False
    if variable.lower() != ('x' or 'y' or 'z'):
        print('La variable debe ser x, y, o z')
        return False

    try:

        from sympy import diff
        import math
        iteraciones = 100
        errorRelativo = tolerancia+1
        i = 0
        xa = x0
        xb = x1
        xi=x1
        resultado = []

        while errorRelativo >= tolerancia and i < iteraciones:
            xi = xb - ((xb-xa)*(diff(funcion, variable, 0).subs(variable, xb).evalf()))/((diff(funcion, variable, 0).subs(variable, xb).evalf())-(diff(funcion, variable, 0).subs(variable, xa).evalf()))
            if xi == 0:
                xi += 0.00000000000000000000000000001
            errorRelativo = math.fabs((xb-xi)/(xi))
            i += 1
            xa = xb
            xb =xi
            print('Raiz= '+ str(xi) + ' error= ' + str(errorRelativo) + ' iteracion= ' + str(i))
            rIteracion = [str(i), str(xi), str(errorRelativo)]
            resultado.append(rIteracion)
        return resultado
    except Exception as e:
        print('Hubo un error, probablemente en la ecuacion')
        print(e.args)



#print(secante('(-x^2)+9', '2', '4', '0.01', 'x'))


def raicesPolinomicas(coeficientes, variable = 'x'):
    from scipy import roots
    return roots(coeficientes)

#print(raicesPolinomicas([1, 1, -2, -8]))
