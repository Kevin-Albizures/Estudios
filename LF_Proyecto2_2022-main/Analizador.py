from enum import Enum
from Controles import Controles
from Tokens import tokensControl,lexemasControl,TokensPropiedades,lexemasPropiedades,TokensColocacion, lexemasColocacion
from CreacionArchivos import reportes

ListaTokens=[]
cont=1
paso=0
recorrido=""
ListaControles=[]
contenido="no"
contadorErrores=0
class Analizador:
    def __init__(self):
        self.linea = 1
        self.columna = 1
        self.tmp_cadena = ""
        self.lista_cadena = []
        self.EstadoActual = 0
        self.IDs=[]

    def AppendListToken(self,No,Token,Lexema):
        global cont
        ListaTokens.append({"NO":No, "Token": Token, "Lexema":Lexema})
        cont+=1

    def aumentarLinea(self):
        _tmp = self.lista_cadena[self.linea-1]
        #print(_tmp + " == "+ self.tmp_cadena)
        #print(str(len(self.lista_cadena[self.linea])))
        #print(str(len(self.tmp_cadena)))
        if _tmp == self.tmp_cadena: 
            self.linea += 1
            self.tmp_cadena = ""
            self.columna = 1
            #print("salto zy que zy")
             
    def eliminarError(self):
        global recorrido
        #print(recorrido)
        if recorrido!="":
            #print(self.lista_cadena[self.linea])
            self.lista_cadena[self.linea]=self.lista_cadena[self.linea].replace(recorrido, '')
            recorrido=""
            #print(self.lista_cadena[self.linea])

    def verificarToken(self, entrada:str, token:str):
        global recorrido,ListaError, contadorErrores
        count = 0
        contadorErrores+=1

        #Cuenta cuantos espacios se debe correr la cadena
        #print(token)
        for i in range(0, len(token)):
            if count >= len(entrada):
                if count==0:
                    print("1")
                    subcadena2=entrada[count+1:]
                    recorrido+=entrada[count]
                    print("Error Léxico, "+"Fila: "+str(self.linea)+", Columna:"+str(self.columna+len(recorrido)+count)+", Token:"+token+", Descripción:"+" Error, token ingresado: "+entrada[count])
                    ListaError.append({"Tipo":"Error Léxico","Fila":self.linea,"Columna":(self.columna+len(recorrido)+count),"Token":entrada[count],"Descripción":"Caracter inválido."})
                    entrada+=subcadena2
                    count=-1
                    return {"result":None, "count":-1}
                else:
                    print("2")
                    subcadena=entrada[:count]
                    subcadena2=entrada[count+1:]
                    recorrido+=entrada[count]
                    print("Error Léxico, "+"Fila: "+str(self.linea)+", Columna:"+str(self.columna+len(recorrido)+count)+", Token:"+token+", Descripción:"+" Error, token ingresado: "+entrada[count])
                    ListaError.append({"Tipo":"Error Léxico","Fila":self.linea,"Columna":(self.columna+len(recorrido)+count),"Token":entrada[count],"Descripción":"Caracter inválido."})
                    entrada=subcadena
                    entrada+=subcadena2
                    count=-1
                    return {"result":None, "count":-1}
            if entrada[i] != token[i]:
                print("3")
                if count==0:
                    subcadena2=entrada[count+1:]
                    #print(entrada[count])
                    recorrido+=entrada[count]
                    print("Error Léxico, "+"Fila: "+str(self.linea)+", Columna:"+str(self.columna+len(recorrido)+count)+", Token:"+token+", Descripción:"+" Error, token ingresado: "+entrada[count])
                    ListaError.append({"Tipo":"Error Léxico","Fila":self.linea,"Columna":(self.columna+len(recorrido)+count),"Token":entrada[count],"Descripción":"Caracter inválido."})
                    entrada=subcadena2
                    count=-1
                    return {"result":None, "count":-1}
                else:
                    print("4")
                    subcadena=entrada[:count]
                    subcadena2=entrada[count+1:]
                    recorrido+=entrada[count]
                    print("Error Léxico, "+"Fila: "+str(self.linea)+", Columna:"+str(self.columna+len(recorrido)+count)+", Token:"+token+", Descripción:"+" Error, token ingresado: "+entrada[count])
                    ListaError.append({"Tipo":"Error Léxico","Fila":self.linea,"Columna":(self.columna+len(recorrido)+count),"Token":entrada[count],"Descripción":"Caracter inválido."})
                    entrada=subcadena
                    entrada+=subcadena2
                    count=-1
                    return {"result":None, "count":-1}

            count += 1

        nueva_cadena = ""
        count_1 = 0
        lista = entrada.split(token)
        for j in lista:
            if count_1 == len(lista) - 1:
                nueva_cadena += j
            elif count_1 > 0:
                nueva_cadena += j + token   

            count_1 += 1

        self.tmp_cadena += token

        return {"result":nueva_cadena, "count":count}

    def verificarToken2(self, entrada:str, token:str):
        count = 0

        for i in range(0, len(token)):
            if count >= len(entrada):
                #ListaError.append({"Tipo":"Error Léxico","Fila":self.linea,"Columna":(self.columna),"Token":token,"Descripción":"Caracter inválido."})
                #print("Error Léxico, "+"Fila: "+str(self.linea)+", Columna:"+str(self.columna)+", Token:"+token+", Descripción:"+" Error, token ingresado: "+entrada[i])
                        
                return {"result":None, "count":count}
            if entrada[i] != token[i]:
                #ListaError.append({"Tipo":"Error Léxico","Fila":self.linea,"Columna":(self.columna),"Token":token,"Descripción":"Caracter inválido."})
                #print("Error Léxico, "+"Fila: "+str(self.linea)+", Columna:"+str(self.columna)+", Token:"+token+", Descripción:"+" Error, token ingresado: "+entrada[i])
                return {"result":None, "count":count}
            count += 1

        nueva_cadena = ""
        count_1 = 0
        lista = entrada.split(token)
        for j in lista:
            if count_1 == len(lista) - 1:
                nueva_cadena += j
            elif count_1 > 0:
                nueva_cadena += j + token

            count_1 += 1

        self.tmp_cadena += token

        return {"result":nueva_cadena, "count":count}

    def quitar(self, entrada:str, token:str):
        nueva_cadena = ""
        count_1 = 0
        # fasdfasfadsfdfaadsf
        lista = entrada.split(token)
        for j in lista:
            if count_1 == len(lista) - 1:
                nueva_cadena += j
            elif count_1 > 0:
                nueva_cadena += j + token

            count_1 += 1
        return nueva_cadena

    def verificarID(self, entrada:str):
        count = 0
        llave = False
        alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n","ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_",","]
        for i in entrada:
            llave = False
            for j in alfabeto:
                if i == j:
                    llave = True
                    break
            if llave == False:
                return {"result":None, "count":count}

            count += 1

        return {"result":True, "count":count}

    def verificarColor(self, entrada:str):
        count = 0
        llave = False
        alfabeto = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",","]
        for i in entrada:
            llave = False
            for j in alfabeto:
                if i == j:
                    llave = True
                    break
            if llave == False:
                return {"result":None, "count":count}

            count += 1
        return {"result":True, "count":count}
    
    def verificarAlineacion(self, entrada:str):
        count = 0
        llave = False
        alfabeto = ["Centro","Izquierdo","Derecho"]
        if entrada=="Centro" or entrada=="Izquierdo" or entrada=="Derecho":
            llave=True
        if llave == False:
            return {"result":None, "count":count}

        return {"result":True, "count":count}

    def verificarMarcada(self, entrada:str):
        count = 0
        llave = False
        if entrada == "False" or entrada=="True":
            llave= True

        if llave == False:
            return {"result":None, "count":count}

        return {"result":True, "count":count}


    def comentarioSimple(self, cadena : str):
        ## //adsdadada
        if cadena[0] == "/" and cadena[1] == "/":
            pass

    def comentariomultilinea(self, cadena : str):
        global paso
        try:
            tmp = ""
            count = 0
            count2=0
            llave = False
            if cadena[0] == "/" and cadena[1] == "*":

                print( self.linea, " | ", self.columna," | COMENTARIO MULTILINEA")
                for i in cadena:
                    
                    if llave:
                        count2+=1
                        if count2==1:
                            self.tmp_cadena += cadena[count]               
                            self.aumentarLinea()
                        else:
                            tmp += i
                    else:
                        self.tmp_cadena += cadena[count]               
                        self.aumentarLinea()
                    
                    if cadena[count - 1] == "*" and cadena[count] == "/":
                        llave = True
                    
                    count += 1
                self.columna =0
                #print(tmp)
                paso=1
                return tmp
            return cadena
        except:
            return cadena 


    def lecturaporEstados(self, cadena):
        global cont, paso,ListaError, ListaTokens
        llave=0
        #ListaTokens.clear()
        self.EstadoActual = "E1"

        while cadena != "":
            
            #print(cadena)
            if (cadena != None):
                while(cadena[0] == " "):
                    self.tmp_cadena += " "
                    self.columna+=1
                    cadena = self.quitar(cadena, " ")

            if (cadena != None):
                while(cadena[0:1] == "\n"):
                    self.tmp_cadena += "\n"
                    self.linea+=1
                    self.columna=1
                    self.tmp_cadena=""
                    cadena = self.quitar(cadena, cadena[0:1])  

            if (cadena != None):
                while(cadena[0] == " "):
                    self.tmp_cadena += " "
                    self.columna+=1
                    cadena = self.quitar(cadena, " ")
                    
            cadena = self.comentariomultilinea(cadena)
            
            if paso==1:
                paso=0
                #print("salto wiii")
                continue

            if (cadena != None):
                
                # ESTADO 1 <
                if self.EstadoActual == "E1": #Listo modelo
                    token = tokensControl["LLAL"] # Se escoge el token a leer
                    res = self.verificarToken(cadena, token) # Se verifica el token
                    self.eliminarError() # Se eliminan los errores que se tengan
                    
                    if res["count"] == -1: # VERIFICAR ERROR 
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, tokensControl["LLAL"],lexemasControl["LLAL"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E2"
                        
                # ESTADO 2 !
                elif self.EstadoActual == "E2": #Listo
                    token = tokensControl["EXCLAMACION"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()

                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:    
                        self.AppendListToken(cont, tokensControl["EXCLAMACION"],lexemasControl["EXCLAMACION"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E3"
                        
                # ESTADO 3 --
                elif self.EstadoActual == "E3": #Listo
                    token =  tokensControl["MENORDOBLE"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, tokensControl["MENORDOBLE"],lexemasControl["MENORDOBLE"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E4"
                        
                # ESTADO 4 Controles
                elif self.EstadoActual == "E4": #Listo
                    llave=0
                    token = tokensControl["CONTROLES"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, tokensControl["CONTROLES"],lexemasControl["CONTROLES"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E5"
                        
                # ESTADO 5 Etiquetas
                elif self.EstadoActual == "E5":
                    
                    tokens = ["Etiqueta","Boton","Check","RadioBoton", "Texto","AreaTexto" ,"Clave","Contenedor",]
                    for i in tokens:
                        res = self.verificarToken2(cadena, i)
                        if res["result"] != None:
                            token = i
                            llave=1
                            self.EstadoActual = "E6"
                            break
                    
                    if res["result"] == None and llave==0:
                        print("Error sintáctico, "+"Fila: "+str(self.linea)+", Columna:"+str(self.columna)+", Token esperado:",end="")
                        ListaError.append({"Tipo":"Error Sintáctico","Fila":self.linea,"Columna":self.columna,"Token":tokens,"Descripción":"Fallo en lectura de control"})
                        print(tokens,end="")
                        print(", Descripción:"+" Error, caracter inválido. ")
                        break
                    elif res["result"] == None and llave==1:
                        self.EstadoActual="E7"
                        #print("hola")
                    else:
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                    
                # ESTADO 6 ID;
                elif self.EstadoActual == "E6": #Listo
                    tmp = cadena.split("\n", maxsplit=1)
                    id = tmp[0][:-1]
                    #print(id)
                    res=self.verificarID(id)
                    self.columna+=len(id)
                    
                    
                    #print(self.verificarID(id))
                    if res["result"] == None:
                        print("Error sintáctico, "+"Fila: "+str(self.linea)+", Columna:"+str(self.columna)+", Token esperado:"+"ID, Descripción:"+" Error, caracter inválido. ")
                        ListaError.append({"Tipo":"Error Sintáctico","Fila":self.linea,"Columna":self.columna,"Token":"ID","Descripción":"Problemas con la ID"})
                        break

                    self.IDs.append(id)
                    if token=="Etiqueta":
                        ListaControles.append(Controles(id,"Etiqueta"))
                        self.AppendListToken(cont, tokensControl["ETIQUETA"],lexemasControl["ETIQUETA"])
                        
                        #print("Etiqueta guardado.")
                    elif token=="Boton":
                        ListaControles.append(Controles(id,"Boton"))
                        self.AppendListToken(cont, tokensControl["BOTON"],lexemasControl["BOTON"])
                        
                        #print("Botón guardado.")
                    elif token=="Check":
                        ListaControles.append(Controles(id,"Check"))    
                        self.AppendListToken(cont, tokensControl["CHECK"],lexemasControl["CHECK"])
                        
                        #print("Check guardado.")
                    elif token=="RadioBoton":
                        ListaControles.append(Controles(id,"RadioBoton"))
                        self.AppendListToken(cont, tokensControl["RADIOBOTON"],lexemasControl["RADIOBOTON"])
                        
                        #print("RadioBoton guardado.")
                    elif token=="Texto":
                        ListaControles.append(Controles(id,"Texto"))
                        self.AppendListToken(cont, tokensControl["TEXTO"],lexemasControl["TEXTO"])
                        
                        #print("Texto guardado.")
                    elif token=="AreaTexto":
                        ListaControles.append(Controles(id,"AreaTexto"))
                        self.AppendListToken(cont, tokensControl["AREATEXTO"],lexemasControl["AREATEXTO"])
                        
                        #print("AreaTexto guardado.")
                    elif token=="Clave":
                        ListaControles.append(Controles(id,"Clave"))
                        self.AppendListToken(cont, tokensControl["CLAVE"],lexemasControl["CLAVE"])
                        
                        #print("Clave guardado.")
                    elif token=="Contenedor":
                        ListaControles.append(Controles(id,"Contenedor"))
                        self.AppendListToken(cont, tokensControl["CONTENEDOR"],lexemasControl["CONTENEDOR"])
                        
                        #print("Contenedor guardado.")
                    
                    
                    cadena = self.quitar(cadena, id)
                    token = tokensControl["PUNTOCOMA"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, tokensControl["PUNTOCOMA"],lexemasControl["PUNTOCOMA"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E5"

                # ESTADO 7 Controles x2
                elif self.EstadoActual == "E7": #Listo
                    token = tokensControl["CONTROLES"] 
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, tokensControl["CONTROLES"],lexemasControl["CONTROLES"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E8"
                
                # ESTADO 8 -- x2
                elif self.EstadoActual == "E8": #Listo
                    token =  tokensControl["MENORDOBLE"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, tokensControl["MENORDOBLE"],lexemasControl["MENORDOBLE"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E9"
                
                # ESTADO 9 >
                if self.EstadoActual == "E9": #Listo
                    token = tokensControl["LLAR"] 
                    res = self.verificarToken(cadena, token) 
                    self.eliminarError() 
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, tokensControl["LLAR"],lexemasControl["LLAR"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E10"
                
                # ESTADO 10 <
                elif self.EstadoActual == "E10": #Listo

                    #inicializar propiedades.
                    for item in ListaControles:
                        item.initPropiedades()

                    token = TokensPropiedades["LLAL"] 
                    res = self.verificarToken(cadena, token) 
                    self.eliminarError() 
                    if res["count"] == -1: # VERIFICAR ERROR 
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensPropiedades["LLAL"],lexemasPropiedades["LLAL"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E11"
                        
                # ESTADO 11 !
                elif self.EstadoActual == "E11": #Listo
                    token = TokensPropiedades["EXCLAMACION"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()

                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:    
                        self.AppendListToken(cont, TokensPropiedades["EXCLAMACION"],lexemasPropiedades["EXCLAMACION"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E12"
                        
                # ESTADO 12 --
                elif self.EstadoActual == "E12": #Listo
                    token =  TokensPropiedades["MENORDOBLE"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensPropiedades["MENORDOBLE"],lexemasPropiedades["MENORDOBLE"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E13"
                        
                # ESTADO 13 Propiedades
                elif self.EstadoActual == "E13": #Listo
                    llave=0
                    token = TokensPropiedades["PROPIEDADES"]
                    res = self.verificarToken2(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == None:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensPropiedades["PROPIEDADES"],lexemasPropiedades["PROPIEDADES"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E14"

                # ESTADO 14 ID's
                elif self.EstadoActual == "E14": #Listo
                    tokens = self.IDs
                    v=0
                    for i in tokens:
                        res = self.verificarToken2(cadena, i)
                        if res["result"] != None:
                            token = i
                            _Control=ListaControles[v]
                            llave=1
                            self.EstadoActual = "E15"
                            contenido="si"
                            break
                        v+=1

                    if res["result"] == None and llave==0:
                        print("Error sintáctico, "+"Fila: "+str(self.linea)+", Columna:"+str(self.columna)+", Token esperado:",end="")
                        ListaError.append({"Tipo":"Error Sintáctico","Fila":self.linea,"Columna":self.columna,"Token":tokens,"Descripción":"ID no registrada"})
                        print(tokens,end="")
                        print(", Descripción:"+" Error, caracter inválido. ")
                        break
                    elif res["result"] == None and llave==1:
                        self.EstadoActual="E20"
                        #print("hola")
                    else:
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"] 

                # ESTADO 15 Punto
                elif self.EstadoActual == "E15": #Listo
                    
                    token = TokensPropiedades["PUNTO"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensPropiedades["PUNTO"],lexemasPropiedades["PUNTO"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E16"
                
                # ESTADO 16 propiedad
                elif self.EstadoActual == "E16": #Listo
                    llave1=0
                    tokens = _Control.atributos
                    for i in tokens:
                        res = self.verificarToken2(cadena, i)
                        if res["result"] != None:
                            token = i
                            llave1=1
                            self.EstadoActual = "E17.1"
                            break

                    if res["result"] == None and llave1==0:
                        print("Error sintáctico, "+"Fila: "+str(self.linea)+", Columna:"+str(self.columna)+", Token esperado:",end="")
                        ListaError.append({"Tipo":"Error Sintáctico","Fila":self.linea,"Columna":self.columna,"Token":tokens,"Descripción":"Propiedad incorrecta."})
                        print(tokens,end="")
                        print(", Descripción:"+" Error, caracter inválido. ")
                        break
                    else:

                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"] 
                    
                # ESTADO 17.1
                elif self.EstadoActual=="E17.1":
                    token2 = TokensPropiedades["PARENTESISABRIR"]
                    res = self.verificarToken(cadena, token2)
                    self.eliminarError()
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensPropiedades["PARENTESISABRIR"],lexemasPropiedades["PARENTESISABRIR"])
                        
                        print( self.linea, " | ", self.columna," | ",  token2)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E17"

                # ESTADO 17 valor propiedad
                elif self.EstadoActual == "E17": #Listo
                    tmp = cadena.split("\n", maxsplit=1)
                    vPropiedad = tmp[0][:-2]
                    self.columna+=len(vPropiedad)
                    if token=="setColorLetra" or token=="setColorFondo" or token=="setAlto" or token=="setAncho":
                        res=self.verificarColor(vPropiedad)
                    elif token=="setTexto" or token=="setGrupo":
                        res=self.verificarID(vPropiedad)
                    elif token=="setAlineacion":
                        res=self.verificarAlineacion(vPropiedad)
                    elif token=="setMarcada":
                        res=self.verificarMarcada(vPropiedad)
                    if res["result"]==0:
                        ListaError.append({"Tipo":"Error Léxico","Fila":self.linea,"Columna":(self.columna),"Token":vPropiedad,"Descripción":"Valor de propiedad inválida."})
                        break
                    print(token)
                    print(vPropiedad)
                    _Control.insertarPropiedad(token,vPropiedad)

                    cadena = self.quitar(cadena, vPropiedad)
                    self.EstadoActual = "E18"
                    

                # ESTADO 18 )
                elif self.EstadoActual == "E18": #Listo
                    token = TokensPropiedades["PARENTESISCERRAR"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensPropiedades["PARENTESISCERRAR"],lexemasPropiedades["PARENTESISCERRAR"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E19"

                # ESTADO 19 ;
                elif self.EstadoActual == "E19": #Listo
                    
                    token = TokensPropiedades["PUNTOCOMA"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensPropiedades["PUNTOCOMA"],lexemasPropiedades["PUNTOCOMA"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E14"

                # ESTADO 20 Propiedades x2
                elif self.EstadoActual == "E20": #Listo
                    token = TokensPropiedades["PROPIEDADES"] 
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensPropiedades["PROPIEDADES"],lexemasPropiedades["PROPIEDADES"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E21"
                
                # ESTADO 21 -- x2
                elif self.EstadoActual == "E21": #Listo
                    token =   TokensPropiedades["MENORDOBLE"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont,  TokensPropiedades["MENORDOBLE"],lexemasPropiedades["MENORDOBLE"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E22"
                
                # ESTADO 22 >
                elif self.EstadoActual == "E22": #Listo
                    token = TokensPropiedades["LLAR"] 
                    res = self.verificarToken(cadena, token) 
                    self.eliminarError() 
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensPropiedades["LLAR"],lexemasPropiedades["LLAR"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E23"

                # ESTADO 23 <
                elif self.EstadoActual == "E23": #Listo

                    token = TokensColocacion["LLAL"] 
                    res = self.verificarToken(cadena, token) 
                    self.eliminarError() 
                    if res["count"] == -1: # VERIFICAR ERROR 
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["LLAL"],lexemasColocacion["LLAL"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E24"
                        
                # ESTADO 24 !
                elif self.EstadoActual == "E24": #Listo
                    token = TokensColocacion["EXCLAMACION"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()

                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:    
                        self.AppendListToken(cont, TokensColocacion["EXCLAMACION"],lexemasColocacion["EXCLAMACION"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E25"
                        
                # ESTADO 25 --
                elif self.EstadoActual == "E25": #Listo
                    token =  TokensColocacion["MENORDOBLE"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["MENORDOBLE"],lexemasColocacion["MENORDOBLE"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E26"
                        
                # ESTADO 26 Colocacion
                elif self.EstadoActual == "E26": #Listo
                    llave=0
                    token = TokensColocacion["COLOCACION"]
                    res = self.verificarToken2(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == None:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["COLOCACION"],lexemasColocacion["COLOCACION"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        llave10=0
                        self.EstadoActual = "E27"

                # ESTADO 27 ID's
                elif self.EstadoActual == "E27": #Listo
                    tokens = self.IDs
                    contenido="no"
                    token="this"
                    v=0
                    res = self.verificarToken2(cadena, token)
                    self.eliminarError()
                    if res["result"] != None:
                        self.EstadoActual = "E34"
                        llave10=1
                        self.AppendListToken(cont, TokensColocacion["THIS"],lexemasColocacion["THIS"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        contenido="si"

                    else:
                        for i in tokens:
                            res = self.verificarToken2(cadena, i)
                            if res["result"] != None:
                                token = i
                                _Control=ListaControles[v]
                                llave10=1
                                self.EstadoActual = "E28"
                                break
                            v+=1

                        if res["result"] == None and llave10==0:
                            print("Error sintáctico, "+"Fila: "+str(self.linea)+", Columna:"+str(self.columna)+", Token esperado:",end="")
                            ListaError.append({"Tipo":"Error Sintáctico","Fila":self.linea,"Columna":self.columna,"Token":tokens,"Descripción":"ID no registrada"})
                            print(tokens,end="")
                            print(", Descripción:"+" Error, caracter inválido. ")
                            break
                        elif res["result"] == None and llave10==1:
                            self.EstadoActual="E40"
                            #print("hola")
                        else:
                            print( self.linea, " | ", self.columna," | ",  token)
                            cadena = res["result"]
                            self.columna += res["count"] 

                # ESTADO 28 Punto
                elif self.EstadoActual == "E28": #Listo
                    
                    token = TokensColocacion["PUNTO"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["PUNTO"],lexemasColocacion["PUNTO"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E29"
                
                # ESTADO 29 setPosicion
                elif self.EstadoActual == "E29": #Listo
                    token = TokensColocacion["POSICION"]
                    #print(cadena)
                    res = self.verificarToken2(cadena, token)

                    if res["result"] == None:
                        self.EstadoActual="E35"

                    else:
                        self.AppendListToken(cont, TokensColocacion["POSICION"],lexemasColocacion["POSICION"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        #print(res["result"])
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E30"

                    
                # ESTADO 30 (
                elif self.EstadoActual=="E30":
                    token2 = TokensColocacion["PARENTESISABRIR"]
                    res = self.verificarToken(cadena, token2)
                    self.eliminarError()
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["PARENTESISABRIR"],lexemasColocacion["PARENTESISABRIR"])
                        
                        print( self.linea, " | ", self.columna," | ",  token2)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E31"

                # ESTADO 31 valor propiedad
                elif self.EstadoActual == "E31": #Listo
                    tmp = cadena.split("\n", maxsplit=1)
                    vPropiedad = tmp[0][:-2]
                    self.columna+=len(vPropiedad)
                    print(vPropiedad)
                    res=self.verificarColor(vPropiedad)
                    if res["result"]==0:
                        ListaError.append({"Tipo":"Error Léxico","Fila":self.linea,"Columna":(self.columna),"Token":vPropiedad,"Descripción":"Valor de propiedad inválida."})
                        break
                    _Control.insertarPropiedad(token,vPropiedad)

                    cadena = self.quitar(cadena, vPropiedad)
                    self.EstadoActual = "E32"
                    

                # ESTADO 32 )
                elif self.EstadoActual == "E32": #Listo
                    token = TokensColocacion["PARENTESISCERRAR"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["PARENTESISCERRAR"],lexemasColocacion["PARENTESISCERRAR"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E33"

                # ESTADO 33 ;
                elif self.EstadoActual == "E33": #Listo
                    
                    token = TokensColocacion["PUNTOCOMA"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["PUNTOCOMA"],lexemasColocacion["PUNTOCOMA"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E27"

                # ESTADO 34 Punto
                elif self.EstadoActual == "E34": #Listo
                    
                    token = TokensColocacion["PUNTO"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["PUNTO"],lexemasColocacion["PUNTO"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E35"

                # ESTADO 35 .add
                elif self.EstadoActual == "E35": #Listo
                    
                    token = TokensColocacion["ADD"]
                    res = self.verificarToken2(cadena, token)
                    self.eliminarError()

                    if res["result"] == None:
                        print(res["result"])
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["ADD"],lexemasColocacion["ADD"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E36"

                # ESTADO 36 (
                elif self.EstadoActual=="E36":
                    token = TokensColocacion["PARENTESISABRIR"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["PARENTESISABRIR"],lexemasColocacion["PARENTESISABRIR"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E37"

                # ESTADO 37 ID's
                elif self.EstadoActual == "E37": #Listo
                    tokens = self.IDs
                    for i in tokens:
                        res = self.verificarToken2(cadena, i)
                        if res["result"] != None:
                            token = i
                            if contenido=="si":
                                _Control.CONTENIDO=("si")
                            else:
                                _Control.CONTIENE.append(i)
                            self.EstadoActual = "E38"
                            break

                    if res["result"] == None:
                        print("Error sintáctico, "+"Fila: "+str(self.linea)+", Columna:"+str(self.columna)+", Token esperado:",end="")
                        ListaError.append({"Tipo":"Error Sintáctico","Fila":self.linea,"Columna":self.columna,"Token":tokens,"Descripción":"ID no registrada"})
                        print(tokens,end="")
                        print(", Descripción:"+" Error, caracter inválido. ")
                        break
                    else:
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"] 

                # ESTADO 38 )
                elif self.EstadoActual == "E38": #Listo
                    token = TokensColocacion["PARENTESISCERRAR"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["PARENTESISCERRAR"],lexemasColocacion["PARENTESISCERRAR"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E39"

                # ESTADO 39 ;
                elif self.EstadoActual == "E39": #Listo
                    
                    token = TokensColocacion["PUNTOCOMA"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["PUNTOCOMA"],lexemasColocacion["PUNTOCOMA"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E27"

                # ESTADCO 40 Colocacion x2
                elif self.EstadoActual == "E40": #Listo
                    llave=0
                    token = TokensColocacion["COLOCACION"]
                    res = self.verificarToken2(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == None:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["COLOCACION"],lexemasColocacion["COLOCACION"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E41"
                
                # ESTADO 41 --
                elif self.EstadoActual == "E41": #Listo
                    token =  TokensColocacion["MENORDOBLE"]
                    res = self.verificarToken(cadena, token)
                    self.eliminarError()
                    
                    if res["count"] == -1:
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["MENORDOBLE"],lexemasColocacion["MENORDOBLE"])
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E42"

                # ESTADO 42 <
                elif self.EstadoActual == "E42": #Listo

                    token = TokensColocacion["LLAR"] 
                    res = self.verificarToken(cadena, token) 
                    self.eliminarError() 
                    if res["count"] == -1: # VERIFICAR ERROR 
                        cadena=res["result"]
                        break
                    else:
                        self.AppendListToken(cont, TokensColocacion["LLAR"],lexemasColocacion["LLAR"])
                        
                        print( self.linea, " | ", self.columna," | ",  token)
                        cadena = res["result"]
                        self.columna += res["count"]
                        self.EstadoActual = "E43"

                if self.EstadoActual=="E43":
                    #print("fin jeje 456546")
                    break
            else:
                #print("fin jeje")
                break
        
        if len(ListaError)==0:
            """for item in ListaControles:
                print()
                print("---------------")
                print("ID: "+item.ID)
                print("Tipo: "+item.Tipo)
                print("Atributos: ",end="")
                print(item.atributos)
                print("Contiene: "+item.CONTENIDO)
                print("Contenido: ",end="")
                print(item.CONTIENE) """
            reportes(ListaControles)
                    

    def compile(self,ruta):
        global ListaError, contadorErrores, ListaControles, ListaTokens,cont
        # LEEMOS EL ARCHIVO DE ENTRADA
        archivo = open(ruta, "r", encoding="utf-8")
        contenido = archivo.readlines()
        archivo.close()

        # LIMPIAR MI ENTRADA
        cont=1
        nueva_cadena = ""
        lista_cadena = []
        ListaError=[]
        self.IDs=[]
        ListaControles=[]
        

        contadorErrores=0

        for i in contenido:
            if i != '':
                nueva_cadena += i
                lista_cadena.append(i)


        print("-------------------")
        print(nueva_cadena)
        print("-------------------")
        print(lista_cadena)

        self.lista_cadena = lista_cadena
        self.lecturaporEstados(nueva_cadena)
        return ListaError   