def validarHexa(cadena):
    cadena = str(cadena).lower()
    if cadena.isdigit():
        return True
    i = 0
    while i < len(cadena):        
        if cadena[i:i+1].isalpha() and not(cadena[i:i+1] == 'a' or cadena[i:i+1] == 'b' or cadena[i:i+1] == 'c' or cadena[i:i+1] == 'd' or cadena[i:i+1] == 'e' or cadena[i:i+1] == 'f'):
            if i == 0 and not(cadena[i:i+1] == '+' or cadena[i:i+1] == '-'):
                return False
            if i != 0:
                return False
        i += 1
    return True

#print(validarHexa('+a2h'))

def decimalABinario (decimal, precision):
    """Convierte un número decimal (base 10) a binario (base 2)."""

    if not str(decimal).isdigit():
        if (not (str(decimal)[0:1] == '+' or str(decimal)[0:1] == '-')) or (not (str(decimal)[1:].isdigit())):
            auxDec = str(decimal)
            if str(decimal)[0:1] == '+' or str(decimal)[0:1] == '-':
                auxDec = str(decimal)[1:]            
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():                
                print("Ingrese un valor numérico");
                return False
    
    if not str(precision).isdigit():
        if (not (str(precision)[0:1] == '+')) or (not (str(precision)[1:].isdigit())):
            print("Ingrese un valor correcto");
            return False
    precision = float(precision)
    decimal = float(decimal)
    partes = str(decimal).split('.')    
    parteEntera = partes[0]
    if len(partes) == 2:
        parteFraccionaria = partes[1]
    else:
        if decimal >= 0:
            return "+" + bin(int(parteEntera))[2:]
        else:
            return bin(int(parteEntera))[0:1] + bin(int(parteEntera))[3:]
    parteBinariaEntera = bin(int(parteEntera))
    numeroFraccionario = float("0." + parteFraccionaria)
    parteBinariaFraccionaria = ""
    i = 0
    while i < precision:        
        numeroFraccionario = numeroFraccionario*2
        if numeroFraccionario > 1:
            numeroFraccionario -= 1
            parteBinariaFraccionaria += "1"
            continue
        if numeroFraccionario < 1:
            parteBinariaFraccionaria += "0"
        if numeroFraccionario == 1:
            parteBinariaFraccionaria += "1"
            break
        i += 1
    if decimal >= 0:
        signo = "+"
        subIndice = 2
    else:
        signo = "-"
        subIndice = 3
        
    return signo + parteBinariaEntera[subIndice:] + "." + parteBinariaFraccionaria

#print(decimalABinario('268', '20'))

def binarioADecimal (binario):
    """""Convierte un número binario (base 2) a decimal (base 10)."""

    if not str(binario).isdigit():
        if (not (str(binario)[0:1] == '+' or str(binario)[0:1] == '-')) or (not (str(binario)[1:].isdigit())):
            auxDec = str(binario)
            if str(binario)[0:1] == '+' or str(binario)[0:1] == '-':
                auxDec = str(binario)[1:]            
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():                
                print("Ingrese un valor numérico");
                return False            
    
    partes = str(binario).split(".")
    parteEntera = partes[0]
    i = 0
    j = len(parteEntera)-1
    decimalEntero = int(parteEntera, 2)
    if not len(partes) == 2:
        return decimalEntero
    parteFraccionaria = partes[1]
    decimalFraccionario = 0
    k = 0
    while k < len(parteFraccionaria):
        decimalFraccionario = decimalFraccionario + int(parteFraccionaria[k])*(2**(-(k+1)))
        k += 1
    if decimalEntero >= 0:
        return float(decimalEntero) + float(decimalFraccionario)
    else:
        return float(decimalEntero) - float(decimalFraccionario)

#print(binarioADecimal('10010110d111.101011'))

def decimalAOctal (decimal, precision):
    """Convierte un número decimal (base 10) a octal (base 8)."""
    
    if not str(decimal).isdigit():
        if (not (str(decimal)[0:1] == '+' or str(decimal)[0:1] == '-')) or (not (str(decimal)[1:].isdigit())):
            auxDec = str(decimal)
            if str(decimal)[0:1] == '+' or str(decimal)[0:1] == '-':
                auxDec = str(decimal)[1:]            
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():                
                print("Ingrese un valor numérico");
                return False
    if not str(precision).isdigit():
        if (not (str(precision)[0:1] == '+')) or (not (str(precision)[1:].isdigit())):
            print("Ingrese un valor correcto");
            return False
        
    decimal = float(decimal)
    precision = float(precision)
    partes = str(decimal).split('.')    
    parteEntera = partes[0]
    if len(partes) == 2:
        parteFraccionaria = partes[1]
    else:
        if decimal >= 0:
            return "+" + oct(int(parteEntera))[2:]
        else:
            return oct(int(parteEntera))[0:1] + oct(int(parteEntera))[3:]
    parteOctalEntera = oct(int(parteEntera))
    numeroFraccionario = float("0." + parteFraccionaria)
    parteOctalFraccionaria = ""
    i = 0
    while i < precision:        
        numeroFraccionario = numeroFraccionario*8
        parteOctalFraccionaria += str(numeroFraccionario)[0]
        numeroFraccionario -= float(str(numeroFraccionario)[0])
        if numeroFraccionario == 0:
            break;
        i += 1
    if decimal >= 0:
        signo = "+"
        subIndice = 2
    else:
        signo = "-"
        subIndice = 3
        
    return signo + parteOctalEntera[subIndice:] + "." + parteOctalFraccionaria

#print(decimalAOctal('1207.67s1875','10'))

def octalADecimal (octal):
    """""Convierte un número octal (base 8) a decimal (base 10)."""

    if not str(octal).isdigit():
        if (not (str(octal)[0:1] == '+' or str(octal)[0:1] == '-')) or (not (str(octal)[1:].isdigit())):
            auxDec = str(octal)
            if str(octal)[0:1] == '+' or str(octal)[0:1] == '-':
                auxDec = str(octal)[1:]            
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():                
                print("Ingrese un valor numérico");
                return False
    
    partes = str(octal).split(".")
    parteEntera = partes[0]
    i = 0
    j = len(parteEntera)-1
    decimalEntero = int(parteEntera, 8)
    if not len(partes) == 2:
        return decimalEntero
    parteFraccionaria = partes[1]
    decimalFraccionario = 0
    k = 0
    while k < len(parteFraccionaria):
        decimalFraccionario = decimalFraccionario + int(parteFraccionaria[k])*(8**(-(k+1)))
        k += 1
    if decimalEntero >= 0:
        return float(decimalEntero) + float(decimalFraccionario)
    else:
        return float(decimalEntero) - float(decimalFraccionario)

#print(octalADecimal('226s7.53'))

def decimalAHexa (decimal, precision):
    """Convierte un número decimal (base 10) a hexadecimal (base 16)."""
    
    if not str(decimal).isdigit():
        if (not (str(decimal)[0:1] == '+' or str(decimal)[0:1] == '-')) or (not (str(decimal)[1:].isdigit())):
            auxDec = str(decimal)
            if str(decimal)[0:1] == '+' or str(decimal)[0:1] == '-':
                auxDec = str(decimal)[1:]            
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():                
                print("Ingrese un valor numérico");
                return False        
    if not str(precision).isdigit():
        if (not (str(precision)[0:1] == '+')) or (not (str(precision)[1:].isdigit())):
            print("Ingrese un valor correcto");
            return False
    
    decimal = float(decimal)
    precision = float(precision)
    
    partes = str(decimal).split('.')    
    parteEntera = partes[0]
    if len(partes) == 2:
        parteFraccionaria = partes[1]
    else:
        if decimal >= 0:
            return "+" + hex(int(parteEntera))[2:]
        else:
            return hex(int(parteEntera))[0:1] + hex(int(parteEntera))[3:]
    parteHexaEntera = hex(int(parteEntera))
    numeroFraccionario = float(str("0." + parteFraccionaria))
    parteHexaFraccionaria = ""
    numeroTemporal = ""
    i = 0
    while i < precision:        
        numeroFraccionario = float(numeroFraccionario)*16
        numeroTemporal = str(numeroFraccionario).split('.')[0]
        if int(numeroTemporal) == 10:
            numeroTemporal = 'A'
        if str(numeroTemporal).isdigit() and int(numeroTemporal) == 11:
            numeroTemporal = 'B'
        if str(numeroTemporal).isdigit() and int(numeroTemporal) == 12:
            numeroTemporal = 'C'
        if str(numeroTemporal).isdigit() and int(numeroTemporal) == 13:
            numeroTemporal = 'D'
        if str(numeroTemporal).isdigit() and int(numeroTemporal) == 14:
            numeroTemporal = 'E'
        if str(numeroTemporal).isdigit() and int(numeroTemporal) == 15:
            numeroTemporal = 'F'
        parteHexaFraccionaria += str(numeroTemporal)
        numeroFraccionario = '0.' + str(numeroFraccionario).split('.')[1]
        if numeroFraccionario == 0:
            break;
        i += 1
    if decimal >= 0:
        signo = "+"
        subIndice = 2
    else:
        signo = "-"
        subIndice = 3
        
    return signo + parteHexaEntera[subIndice:] + "." + parteHexaFraccionaria

#print(decimalAHexa('1207.67s1875',10))

def hexaADecimal (hexa):
    """""Convierte un número hexadecimal (base 16) a decimal (base 10)."""

    if not validarHexa(hexa):
        print("Ingrese un valor numérico")
        return False
    
    partes = str(hexa).split(".")
    parteEntera = partes[0]
    i = 0
    j = len(parteEntera)-1
    decimalEntero = int(parteEntera, 16)
    if not len(partes) == 2:
        return decimalEntero
    parteFraccionaria = partes[1]
    decimalFraccionario = 0
    k = 0
    while k < len(parteFraccionaria):
        auxDecimal = int(parteFraccionaria[k], 16)
        decimalFraccionario = decimalFraccionario + auxDecimal*(16**(-(k+1)))        
        k += 1
    if decimalEntero >= 0:
        return float(decimalEntero) + float(decimalFraccionario)
    else:
        return float(decimalEntero) - float(decimalFraccionario)

#print(hexaADecimal('4b7.AC000s00000'))

def binarioAPuntoFlotante32(binario):
    """Convierte un numero binario (en base 2) a la representacion
    punto flotante de 32 bits regida por la IEEE 754"""

    if not str(binario).isdigit():
        if (not (str(binario)[0:1] == '+' or str(binario)[0:1] == '-')) or (not (str(binario)[1:].isdigit())):
            auxDec = str(binario)
            if str(binario)[0:1] == '+' or str(binario)[0:1] == '-':
                auxDec = str(binario)[1:]
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():
                print("Ingrese un valor numérico");
                return False
    binario = str(binario)
    puntoFlotante = ""
    partes = binario.split(".")
    binarioEntero = partes[0]
    binarioFraccionario = "0"
    if len(partes) > 1:
           binarioFraccionario = partes[1]

    if int(binarioEntero) == 0 and int(binarioFraccionario) == 0:
        return "0-00000000-00000000000000000000000"
    if int(binarioEntero) < 0:
        puntoFlotante += "1"
    if int(binarioEntero) >= 0:
        puntoFlotante += "0"

    if(binarioEntero[0] == '-' or binarioEntero[0] == '+'):
        binarioEntero = binarioEntero[1:]
        
    exponente = 0
    if int(binarioEntero) > 0:
        exponente = len(binarioEntero)-1
    else:
        i = 0
        while i < len(binarioFraccionario):
            if binarioFraccionario[i:i+1] == "1":
                exponente = (-i)-1
                break
            i += 1
    exponente = bin(exponente+127)[2:]
    while len(exponente) < 8:
        exponente ="0" + exponente         
    puntoFlotante += "-" + exponente

    binarioJunto = binarioEntero + binarioFraccionario
    binarioJunto = binarioJunto.split("1", 1)
    mantisa = binarioJunto[1]
    if len(mantisa) >23:
        mantisa = mantisa[0:23]
    while len(mantisa) < 23:
        mantisa += "0"
    puntoFlotante += "-" + mantisa
    
    return puntoFlotante

#print(binarioAPuntoFlotante32('-100001100.00000000000000000000'))

def binarioAPuntoFlotante64(binario):
    """Convierte un numero binario (en base 2) a la representacion
    punto flotante de 64 bits regida por la IEEE 754"""

    if not str(binario).isdigit():
        if (not (str(binario)[0:1] == '+' or str(binario)[0:1] == '-')) or (not (str(binario)[1:].isdigit())):
            auxDec = str(binario)
            if str(binario)[0:1] == '+' or str(binario)[0:1] == '-':
                auxDec = str(binario)[1:]
            if (len(str(auxDec).split('.')) != 2) or not str(auxDec).split('.')[0].isdigit() or not str(auxDec).split('.')[1].isdigit():
                print("Ingrese un valor numérico");
                return False

    puntoFlotante = ""
    partes = binario.split(".")
    binarioEntero = partes[0]
    binarioFraccionario = "0"
    if len(partes) > 1:
           binarioFraccionario = partes[1]

    if int(binarioEntero) == 0 and int(binarioFraccionario) == 0:
        return "0-00000000000-0000000000000000000000000000000000000000000000000000"
    if int(binarioEntero) < 0:
        puntoFlotante += "1"
    if int(binarioEntero) >= 0:
        puntoFlotante += "0"
        
    if(binarioEntero[0] == '-' or binarioEntero[0] == '+'):
        binarioEntero = binarioEntero[1:]
        
    exponente = 0
    if int(binarioEntero) > 0:
        exponente = len(binarioEntero)-1
    else:
        i = 0
        while i < len(binarioFraccionario):
            if binarioFraccionario[i:i+1] == "1":
                exponente = (-i)-1
                break
            i += 1
    exponente = bin(exponente+1023)[2:]
    while len(exponente) < 11:
        exponente = "0" + exponente
    
    puntoFlotante += "-" + exponente

    binarioJunto = binarioEntero + binarioFraccionario
    binarioJunto = binarioJunto.split("1", 1)
    mantisa = binarioJunto[1]
    if len(mantisa) > 52:
        mantisa = mantisa[0:52]
    while len(mantisa) < 52:
        mantisa += "0"
    puntoFlotante += "-" + mantisa
    
    return puntoFlotante

#print(binarioAPuntoFlotante64('1111011001.0101'))

def puntoFlotanteABinario32(signo, exponente, mantisa):
    """Convierte un numero representado como punto
    flotante de 32 bits regida por la IEEE 754 a un numero en base 2"""

    signo = str(signo)
    exponente = str(exponente)
    mantisa = str(mantisa)

    if not str(signo).isdigit() or not(signo == '0' or signo =='1') or len(signo)!=1:
        print("Ingrese un valor correcto")
        return False
    if not str(exponente).isdigit() or len(exponente)!=8:
        print("Ingrese un valor numérico")
        return False
    if not str(mantisa).isdigit() or len(mantisa)!=23:
        print("Ingrese un valor numérico")
        return False
    i = 0
    while i < len(exponente):
        if not(exponente[i] == '0' or exponente[i] == '1'):
            print("Ingrese un valor correcto en el exponente")
            return False
        i += 1
    i = 0
    while i < len(mantisa):
        if not(mantisa[i] == '0' or mantisa[i] == '1'):
            print("Ingrese un valor correcto en el mantisa")
            return False
        i += 1

    resultadoBinario = ''    

    exponente2 = int(str(exponente), 2) - 127
    numeroBinario = '1' + str(mantisa)[0:exponente2] + '.' + str(mantisa)[exponente2:]
    if signo == '0':
        resultadoBinario = '+' + numeroBinario
    if signo == '1':
        resultadoBinario = '-' + numeroBinario
    
    return resultadoBinario

#print(puntoFlotanteABinario32(0,10000111, '00001100000000000000000'))

def puntoFlotanteABinario64(signo, exponente, mantisa):
    """Convierte un numero representado como punto
    flotante de 64 bits regida por la IEEE 754 a un numero en base 2"""

    signo = str(signo)
    exponente = str(exponente)
    mantisa = str(mantisa)

    if not str(signo).isdigit() or not (signo == '0' or signo == '1') or len(signo) != 1:
        print("Ingrese un valor correcto")
        return False
    if not str(exponente).isdigit() or len(exponente) != 11:
        print("Ingrese un valor numérico")
        return False
    if not str(mantisa).isdigit() or len(mantisa) != 52:
        print("Ingrese un valor numérico")
        return False
    i = 0
    while i < len(exponente):
        if not (exponente[i] == '0' or exponente[i] == '1'):
            print("Ingrese un valor correcto en el exponente")
            return False
        i += 1
    i = 0
    while i < len(mantisa):
        if not (mantisa[i] == '0' or mantisa[i] == '1'):
            print("Ingrese un valor correcto en el mantisa")
            return False
        i += 1

    resultadoBinario = ''    

    exponente2 = int(str(exponente), 2) - 1023
    numeroBinario = '1' + str(mantisa)[0:exponente2] + '.' + str(mantisa)[exponente2:]
    if signo == '0':
        resultadoBinario = '+' + numeroBinario
    if signo == '1':
        resultadoBinario = '-' + numeroBinario
    
    return resultadoBinario

#print(puntoFlotanteABinario64(0,10000001000,'1010000110010000111101011100001010001111010111000011'))
#print(binarioAPuntoFlotante32(decimalABinario(268 , 20)))
