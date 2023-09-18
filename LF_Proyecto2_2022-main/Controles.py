
class Controles:

    def __init__(self,ID,Tipo):
        self.ID=ID
        self.Tipo=Tipo
        self.Llave="No"
        self.atributos=None
        self.CONTIENE=[]
        self.CONTENIDO="no"

    def propiedadesEtiqueta(self):
        self.atributos={"setColorLetra": "", "setTexto": "","setAlineacion":"izquierdo", "setColorFondo":"","setPosicion": "","setAncho":"","setAlto":""}

    def propiedadesBoton(self):
        self.atributos={"setColorLetra": "", "setTexto": "","setAlineacion":"izquierdo", "setColorFondo":"","setPosicion": "","setAncho":"","setAlto":""}

    def propiedadesCheck(self):
        self.atributos={"setColorLetra": "", "setTexto": "","setAlineacion":"izquierdo", "setColorFondo":"","setPosicion": "","setAncho":"","setAlto":"","setMarcada":"" }

    def propiedadesRadioBoton(self):
        self.atributos={"setColorLetra": "", "setTexto": "","setAlineacion":"izquierdo", "setColorFondo":"","setPosicion": "","setAncho":"","setAlto":"","setMarcada":"","setGrupo":""}

    def propiedadesTexto(self):
        self.atributos={"setColorLetra": "", "setTexto": "","setAlineacion":"izquierdo", "setColorFondo":"","setPosicion": "","setAncho":"","setAlto":""}

    def propiedadesAreaTexto(self):
        self.atributos={"setColorLetra": "", "setTexto": "","setAlineacion":"izquierdo", "setColorFondo":"","setPosicion": "","setAncho":"150","setAlto":"150"}

    def propiedadesClave(self):
        self.atributos={"setColorLetra": "", "setTexto": "","setAlineacion":"izquierdo", "setColorFondo":"","setPosicion": "","setAncho":"","setAlto":""}

    def propiedadesContenedor(self):
        self.atributos={"setColorLetra": "", "setTexto": "","setAlineacion":"izquierdo", "setColorFondo":"","setPosicion": "","setAncho":"","setAlto":""}

    def initPropiedades(self):
        Tipo=self.Tipo
        if Tipo=="Etiqueta":
            self.propiedadesEtiqueta()
        elif Tipo=="Boton":
            self.propiedadesBoton()
        elif Tipo=="Check":
            self.propiedadesCheck()
        elif Tipo=="RadioBoton":
            self.propiedadesRadioBoton()
        elif Tipo=="Texto":
            self.propiedadesTexto()
        elif Tipo=="AreaTexto":
            self.propiedadesAreaTexto()
        elif Tipo=="Clave":
            self.propiedadesClave()
        elif Tipo=="Contenedor":
            self.propiedadesContenedor()

    def insertarPropiedad(self, Tipo,valor):
        self.atributos[Tipo]=valor   