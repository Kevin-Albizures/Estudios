import math
from expression import *
from operador import Operador
from generador import Generador
from math   import sin, cos, tan, pow

class Aritmeticas(Expression):
    
    def __init__(self, left, right, tipo, fila, column):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, column)
    
    def ejecutar(self, getER):
        genAux = Generador()
        generador = genAux.getInstance()
        
        izq = self.left.ejecutar(getER)
        if self.right != None:
            der = self.right.ejecutar(getER)
            if self.tipo == Operador.SUMA:
                return generador.addExpresion(izq, der, '+') if getER else izq+der
            elif self.tipo == Operador.RESTA:
                return generador.addExpresion(izq, der, '-') if getER else izq-der
                # return izq - der
            elif self.tipo == Operador.MULTIPLICACION:
                return generador.addExpresion(izq, der, '*') if getER else izq*der
                # return izq * der
            elif self.tipo == Operador.DIVISION:
                if der != 0:
                    return generador.addExpresion(izq, der, '/') if getER else izq/der
                    # return izq / der
                else:
                    print("Error: Division por cero")
                    return None
            elif self.tipo == Operador.POTENCIA:
                return generador.addExpresion(der, izq, '^') if getER else pow(der,izq)
                # return izq ** der
            elif self.tipo == Operador.MOD:
                return generador.addExpresion(izq, der, '%') if getER else  izq%der 
                # return izq % der
            elif self.tipo == Operador.RAIZ:
                if der>0:
                    return generador.addExpresion(izq, der, 'RAIZ') if getER else der**(1/izq)
                    # return izq % der
                else:
                    print("Error: no se permiten números negativos dentro de la raiz")
                    return None
            else:
                return 0
        else:
            if self.tipo == Operador.INVERSO:
                return generador.addExpresion(1, izq, '/') if getER else round(1/izq,10)
            elif self.tipo == Operador.COSENO:
                return generador.addExpresion("",izq, 'COSENO') if getER else round(cos(((izq*math.pi)/180)),10)
                # return coseno(izq)
            elif self.tipo == Operador.SENO:
                return generador.addExpresion("",izq, 'SENO') if getER else round(sin(((izq*math.pi)/180)),10)
                # return seno(izq)
            elif self.tipo == Operador.TANGENTE:
                return generador.addExpresion("",izq, 'TANGENTE') if getER else round(tan(((izq*math.pi)/180)),10)
                # return tangente(izq)
                
