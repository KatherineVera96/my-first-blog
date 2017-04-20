from math import*
class Simp13:

    def __init__(self):
        return

    def fx(self,x, f):
        return eval(f)

    def simpin13(self,n, a, b, f):
        m=Simp13()
        h = (b - a) / n
        suma = 0.0
        for i in range(1, n):
            x = a + i * h
            if(i % 2 == 0):
                suma = suma + 2 * m.fx(x, f)
            else:
                suma = suma + 4 * m.fx(x, f)
        suma = suma + m.fx(a, f) + m.fx(b, f)
        rest = suma * (h / 3)
        return (rest)
