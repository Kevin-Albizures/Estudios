from asyncio.windows_events import NULL
import os
from NodoCelda import  NodoPaciente
from colorama import Fore
sanas=list()
contagiadas=list()
N=list()
N1=list()
columnas=list()
filas=list()
valorNuevo=list()
class ListaNodosDoble():
    def __init__(self):
        self.primero=None
        self.Ultimo=None
        self.abajo=None
        self.arriba=None

    def estaVacia(self):
        if self.primero==None:
            return True
        else:
            return False 
    
    def agregarAListaAbajo(self,Contenido):
        nuevo= NodoPaciente(Contenido)
        if self.estaVacia():
            self.primero=self.Ultimo=self.abajo=self.arriba=nuevo
        else:
            temp2=self.Ultimo
            temp=nuevo
            temp.bajar=self.arriba
            self.arriba.subir=temp
            self.arriba=self.Ultimo=temp2.siguiente=nuevo
            self.Ultimo.anterior=temp2
            self.UnirNodos2()

    def agregarAListaUltimo(self,Contenido):
        nuevo= NodoPaciente(Contenido)
        if self.estaVacia():
            self.primero=self.Ultimo=self.abajo=self.arriba=nuevo
        else:
            temp=self.Ultimo
            self.Ultimo=temp.siguiente=nuevo
            self.Ultimo.anterior=temp
        self.UnirNodos()

    def UnirNodos(self):
        if self.primero!=None:
            self.primero.anterior=NULL
            self.Ultimo.siguiente=NULL
    
    def UnirNodos2(self):
        if self.primero!=None:
            self.Ultimo.siguiente=self.abajo
    
    def remplazar(self,Multiplo,fila,columna):
        temp=self.primero
        i=0
        j=0
        for Numero in range(0,int(Multiplo)):
            i=0
            if str(j)==fila and str(i)==columna:
                temp.Contenido="1"
                break
            else:
                temp=temp.siguiente
            i+=1
            for Numero2 in range(0,int(Multiplo)-1):
                if str(j)==fila and str(i)==columna:
                    temp.Contenido="1"
                    break
                else:
                    temp=temp.siguiente
                i+=1
            j+=1
    
    def recorrerInicio_Fin(self,multiplo):
        temp57=self.primero
        temp58=self.primero
    
        i=0
        while temp57:
            if temp57.Contenido=="1":
                print(Fore.GREEN+temp57.Contenido,end=" ")
            else:
                print(Fore.BLUE+temp57.Contenido,end=" ")
            temp57=temp57.siguiente
            i+=1
            if i==0:
                if temp58.Contenido=="1":
                    print(Fore.GREEN+temp58.Contenido,end=" ")
                else:
                    print(Fore.BLUE+temp58.Contenido,end=" ")
                temp58=temp58.bajar
            if i==int(multiplo):
                print("")
                i=0
            if temp57==NULL:
                print("")
                break      
    
    def recorrerIteracion(self,multiplo):
        temp123=self.primero
        for v1 in range(0,int(multiplo)):
            print("")
            for v2 in range(0,int(multiplo)):
                if temp123.Contenido=="1":
                    print(Fore.GREEN+temp123.Contenido,end=" ")
                else:
                    print(Fore.BLUE+temp123.Contenido,end=" ")
                temp123=temp123.siguiente

    def reemplazarItera(self,Multiplo,fila,columna,valor):
        temp10=self.primero
        i=0
        j=0
        for Numero in range(0,int(Multiplo)):
            for Numero2 in range(0,int(Multiplo)):
                
                if j==fila and i==columna:
                    temp10.Contenido=valor
                    break
                else:
                    temp10=temp10.siguiente
                i+=1
            j+=1
            i=0
    
    def Iterar(self,multiplo,Indice):
        global valorNuevo,columnas,filas,sanas,contagiadas
        valorNuevo.clear()
        filas.clear()
        columnas.clear()
        temp=self.primero
        temp2=self.primero ## este irá guardando la información
        temp3=self.primero
        c=0
        f=0
        conteo=0
        i=0
        ## Primer apuntador
        for iteTemp in range(0,int(multiplo)):
            temp=temp.siguiente
        ## Primera fila 
        for iteTemp2 in range(0,int(multiplo)):
            conteo=0
            if iteTemp2==0:
                if temp2.siguiente.Contenido=="1":
                    conteo+=1
                if temp.Contenido=="1":
                    conteo+=1
                if temp.siguiente.Contenido=="1":
                    conteo+=1 
            elif iteTemp2==int(multiplo)-1:
                if temp2.anterior.Contenido=="1":
                    conteo+=1
                if temp.anterior.Contenido=="1":
                    conteo+=1
                if temp.Contenido=="1":
                    conteo+=1
            else:
                if temp2.anterior.Contenido=="1":
                    conteo+=1
                if temp2.siguiente.Contenido=="1":
                    conteo+=1
                if temp.anterior.Contenido=="1":
                    conteo+=1
                if temp.Contenido=="1":
                    conteo+=1
                if temp.siguiente.Contenido=="1":
                    conteo+=1
            
            if temp2.Contenido=="1":
                if conteo!=3 and conteo!=2:
                    valorNuevo.append("0")
                    columnas.append(c)
                    filas.append(f)
                    sanas[Indice]+=1
                    contagiadas[Indice]-=1

            if temp2.Contenido=="0":
                if conteo==3:
                    valorNuevo.append("1")            
                    columnas.append(c)
                    filas.append(f)
                    sanas[Indice]-=1
                    contagiadas[Indice]+=1

            temp=temp.siguiente
            temp2=temp2.siguiente
            c+=1
        
        ## Iterando las demás filas 
        for v1 in range(0,int(multiplo)-2):
            f+=1
            c=0
            for v2 in range(0,int(multiplo)):
                conteo=0
                if v2==0:
                    if temp3.Contenido=="1":
                        conteo+=1
                    if temp3.siguiente.Contenido=="1":
                        conteo+=1
                    if temp2.siguiente.Contenido=="1":
                        conteo+=1
                    if temp.Contenido=="1":
                        conteo+=1
                    if temp.siguiente.Contenido=="1":
                        conteo+=1 
                elif v2==int(multiplo)-1:
                    if temp3.anterior.Contenido=="1":
                        conteo+=1
                    if temp3.Contenido=="1":
                        conteo+=1
                    if temp2.anterior.Contenido=="1":
                        conteo+=1
                    if temp.anterior.Contenido=="1":
                        conteo+=1
                    if temp.Contenido=="1":
                        conteo+=1
                else:
                    if temp3.anterior.Contenido=="1":
                        conteo+=1
                    if temp3.Contenido=="1":
                        conteo+=1
                    if temp3.siguiente.Contenido=="1":
                        conteo+=1
                    if temp2.anterior.Contenido=="1":
                        conteo+=1
                    if temp2.siguiente.Contenido=="1":
                        conteo+=1
                    if temp.anterior.Contenido=="1":
                        conteo+=1
                    if temp.Contenido=="1":
                        conteo+=1
                    if temp.siguiente.Contenido=="1":
                        conteo+=1
                
                if temp2.Contenido=="1":
                    if conteo!=3 and conteo!=2:
                        valorNuevo.append("0")
                        columnas.append(c)
                        filas.append(f)
                        sanas[Indice]+=1
                        contagiadas[Indice]-=1

                if temp2.Contenido=="0":
                    if conteo==3:
                        valorNuevo.append("1")            
                        columnas.append(c)
                        filas.append(f)
                        sanas[Indice]-=1
                        contagiadas[Indice]+=1
                temp=temp.siguiente
                temp2=temp2.siguiente
                temp3=temp3.siguiente
                c+=1

        ## Ultima fila
        c=0
        f+=1
        for iteTemp3 in range(0,int(multiplo)):
            conteo=0
            if iteTemp3==0:
                if temp3.Contenido=="1":
                    conteo+=1
                if temp3.siguiente.Contenido=="1":
                    conteo+=1
                if temp2.siguiente.Contenido=="1":
                    conteo+=1 
            elif iteTemp3==int(multiplo)-1:
                if temp3.anterior.Contenido=="1":
                    conteo+=1
                if temp3.Contenido=="1":
                    conteo+=1
                if temp2.anterior.Contenido=="1":
                    conteo+=1
            else:
                if temp3.anterior.Contenido=="1":
                    conteo+=1
                if temp3.Contenido=="1":
                    conteo+=1
                if temp3.siguiente.Contenido=="1":
                    conteo+=1
                if temp2.anterior.Contenido=="1":
                    conteo+=1
                if temp2.siguiente.Contenido=="1":
                    conteo+=1
            
            if temp2.Contenido=="1":
                if conteo!=3 and conteo!=2:
                    valorNuevo.append("0")
                    columnas.append(c)
                    filas.append(f)
                    sanas[Indice]+=1
                    contagiadas[Indice]-=1

            if temp2.Contenido=="0":
                if conteo==3:
                    valorNuevo.append("1")            
                    columnas.append(c)
                    filas.append(f)
                    sanas[Indice]-=1
                    contagiadas[Indice]+=1

            temp2=temp2.siguiente
            temp3=temp3.siguiente
            c+=1
        print("datos cargados")
        ## Reemplazar información

    def mostrarContenido(self,i):
        temp=self.primero
        for m in range(0,i):
            temp.siguiente

        return temp.Contenido


    def reporte(self,nombre,edad,Patron,Multiplo,sanas,contagiadas):
        temp=self.primero
        temp2=self.primero
        text=None
        text="subgraph cluster_p{\n"
        text+="node [shape=plaintext]\n"
        text+="label=\"PACIENTE: "+nombre+" \\n EDAD: "+edad+" \\n PATRON: "+Patron+" \\n Celulas Sanas: "+sanas+", Celulas Contagiadas: "+contagiadas+"\"\n"
        text+="fontcolor=\"#000000\"\n"
        text+="bgcolor=\"#e77b00\"\n"
        text+="fontsize=\"27\"\n"
        text+="struct1 [label=<<TABLE bgcolor=\"#000000\" CELLBORDER=\"1\" CELLSPACING=\"5\" CELLPADDING=\"1\"> \n"

        i=0
        for Numero in range(0,int(Multiplo)):
            text+="<TR>"
            for Numero2 in range(0,int(Multiplo)):
                if temp.Contenido=="1":
                    text+="<TD BGCOLOR=\"#84FE87\" WIDTH=\"30\" HEIGHT=\"30\"></TD>\n"#verde
                else:
                    text+="<TD BGCOLOR=\"#7B241C\" WIDTH=\"30\" HEIGHT=\"30\"></TD>\n"#rojo
                temp=temp.siguiente
                
            text+="</TR>"
            i=0
        """while temp:
            if i==0:
                text+="<TR>"
                i=0
            if temp.Contenido=="1":
                text+="<TD BGCOLOR=\"#84FE87\" WIDTH=\"30\" HEIGHT=\"30\"></TD>\n"#verde
            else:
                text+="<TD BGCOLOR=\"#7B241C\" WIDTH=\"30\" HEIGHT=\"30\"></TD>\n"#rojo
            temp=temp.siguiente
            i+=1
            if temp==NULL:
                print("")
                text+="</TR>"
                break 

            if i==int(Multiplo):
                text+="</TR>"
                i=0"""
             
        text+="</TABLE>>];"
        text+="}"
        return text

    def crearReporte(self,nombre,edad,Patron,Multiplo,sanas,contagiadas):
        contenido="digraph G{\n\n"
        r=open("reporte.txt","w")
        contenido+=self.reporte(nombre,edad,Patron,Multiplo,sanas,contagiadas)
        contenido+="\n}"
        r.write(contenido)
        r.close()
        print("Paciente "+nombre+": información guardada")
        os.system("dot -Tpng reporte.txt -o Paciente_"+nombre.replace(" ","")+"/"+nombre.replace(" ","")+"_P_"+Patron+".png") 

    