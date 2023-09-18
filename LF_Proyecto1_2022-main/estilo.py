from expression import Expression
conjuntos=list()
class Estilo(Expression):
    
        def __init__(self, instruccion, color, tamanio, line, column):
            self.instruccion = instruccion
            self.color = color
            self.tamanio = tamanio
            self.line = line
            self.column = column
    
        def ejecutar(self, getER):
            global conjuntos
            conjuntos.append({"Instrucción": self.instruccion,"Color": self.color ,"Tamaño": self.tamanio})
            return {self.instruccion, self.color, self.tamanio}