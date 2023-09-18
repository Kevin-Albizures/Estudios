error_L=list()

class Errores():
    
    def __init__(self, lexema, tipo, columna, fila):
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna
        self.fila = fila
    

    def toString(self):
        global error_L
        error_L.append({"Lexema":self.lexema, "Tipo": self.tipo,"Fila": self.columna ,"Columna": self.fila})
        return f"=======\nLexema: {self.lexema}\nTipo: {self.tipo}\nFila: {self.columna}\nColumna: {self.fila}\n======="