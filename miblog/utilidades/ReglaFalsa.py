def metodoReglaFalsa (funcion, a, b, tolerancia):
    
    from py_expression_eval import Parser
    funcion = str(funcion)
    parser = Parser()
    ecuacion = parser.parse(funcion)

    if (ecuacion.evaluate({"x":a})*ecuacion.evaluate({"x":b})) > 0:
        print("La funcion no tiene raices en el intervalo dado")
        return None
        
    rAnt = 0
    rAct = ((a*ecuacion.evaluate({"x":b}))-(b*ecuacion.evaluate({"x":a})))/(ecuacion.evaluate({"x":b})-ecuacion.evaluate({"x":a}))
    er = tolerancia + 1
    numeroIteraciones = 100
    i = 1
    while ecuacion.evaluate({"x":rAct}) != 0 and tolerancia < er and i <= numeroIteraciones:
        print(i-1)
        if (ecuacion.evaluate({"x":a})*ecuacion.evaluate({"x":rAct})) < 0:
            b = rAct
        else:
            a = rAct
        
        rAnt = rAct
        rAct = ((a*ecuacion.evaluate({"x":b}))-(b*ecuacion.evaluate({"x":a})))/(ecuacion.evaluate({"x":b})-ecuacion.evaluate({"x":a}))
        er = (rAnt - rAct)/rAct
        if er < 0:
            er = -er
        i += 1
    print(i-1)
    return rAct

print(metodoReglaFalsa('', -10, 10, 0.00001))
