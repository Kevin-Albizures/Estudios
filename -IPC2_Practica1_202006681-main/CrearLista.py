from asyncio.windows_events import NULL
from NodoPedido import Pedido
from colorama import Fore
import os
tiempoGeneral=0
Num=0
N=0
class ListaPedidos:
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def estaVacia(self):
        if self.primero==None:
            return True
        else:
            return False 
        
    def agregarAListaUltimo(self,nombre,dirección,nit, formaPago,ingrediente, tiempo, cantidad):
        global Num, tiempoGeneral
        Num+=1
        tiempoGeneral+=float(tiempo)
        nuevo=Pedido(nombre,dirección,nit, formaPago,ingrediente, tiempo, cantidad)
        if self.estaVacia():
            self.primero=self.ultimo=nuevo
        else:
            temp=self.ultimo
            self.ultimo=temp.siguiente=nuevo
            self.ultimo.anterior=temp
        input(Fore.LIGHTBLUE_EX+"Orden cargada")
        self.UnirNodos()

    def UnirNodos(self):
        if self.primero!=None:
            self.primero.anterior=NULL
            self.ultimo.siguiente=NULL

    def recorrerInicio_Fin(self):
        global tiempoGeneral
        if self.primero==None:
            input(Fore.LIGHTBLUE_EX+"No hay ordenes. ")
    
        temp=self.ultimo
        No=int(Num)
        tiempoDemora=tiempoGeneral
        tiempoTotal=0
        print(Fore.RED+"_____________________________________Fin de ordenes_____________________________________")
        while temp:

            print("")
            print(Fore.LIGHTYELLOW_EX+"---------------- "+Fore.LIGHTGREEN_EX+"Orden No."+str(No)+Fore.LIGHTYELLOW_EX+" ----------------")
            print(Fore.GREEN+"  Nombre: "+        Fore.LIGHTYELLOW_EX+    temp.nombre)
            print(Fore.GREEN+"  Dirección: "+     Fore.LIGHTYELLOW_EX+    temp.dirección)
            print(Fore.GREEN+"  NIT: "+           Fore.LIGHTYELLOW_EX+    temp.nit)
            print(Fore.GREEN+"  Forma de pago: "+ Fore.LIGHTYELLOW_EX+    temp.formaPago)

            if temp.ingrediente=="1":
                ingrediente="Salchicha"
            elif temp.ingrediente=="2":
                ingrediente="Chorizo"
            elif temp.ingrediente=="3":
                ingrediente="Salami"
            elif temp.ingrediente=="4":
                ingrediente="Longaniza"
            elif temp.ingrediente=="5":
                ingrediente="Costilla"
            
            tiempoDemora=tiempoDemora-(temp.tiempo)
            tiempoTotal=tiempoDemora+temp.tiempo
            print(Fore.GREEN+"  Ingrediente: "+         Fore.LIGHTYELLOW_EX+    ingrediente)
            print(Fore.GREEN+"  Cantidad: "+            Fore.LIGHTYELLOW_EX+    temp.cantidad)
            print(Fore.GREEN+"  Tiempo de preparación: "+Fore.LIGHTYELLOW_EX+   str(temp.tiempo)+" min")
            print(Fore.GREEN+"  Tiempo de demora: "+    Fore.LIGHTYELLOW_EX+    str(tiempoDemora)+" min")
            print(Fore.GREEN+"  Tiempo total: "+        Fore.LIGHTYELLOW_EX+    str(tiempoTotal)+" min")
            print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
            
            temp=temp.anterior

            if temp==NULL:
                print("")
                input(Fore.LIGHTBLUE_EX+"Cola de ordenes ")
                break      
            No-=1
    
    
    def CuerpoGrafica(self): 
        global tiempoGeneral, Num
        tiempoTotal=tiempoGeneral
        temp=self.ultimo
        text=None
        estructura=int(Num)
        ingrediente=None
        text=""
        while temp:
            text+="node [shape=component];\n"    
            text+="Orden"+str(estructura)+" [label=<<TABLE>\n"
            
            text+=" <TR>\n"
            text+="     <TD>No. Orden:</TD>\n"
            text+="     <TD>"+str(estructura)+"</TD>\n"
            text+=" </TR>\n"
            
            text+=" <TR>\n"
            text+="     <TD>Nombre</TD>\n"
            text+="     <TD>"+temp.nombre+"</TD>\n"
            text+=" </TR>\n"

            text+=" <TR>\n"
            text+="     <TD>Forma de pago</TD>\n"
            text+="     <TD>"+temp.formaPago+"</TD>\n"
            text+=" </TR>\n"

            text+=" <TR>\n"
            if temp.ingrediente=="1":
                ingrediente="Salchicha"
            elif temp.ingrediente=="2":
                ingrediente="Chorizo"
            elif temp.ingrediente=="3":
                ingrediente="Salami"
            elif temp.ingrediente=="4":
                ingrediente="Longaniza"
            elif temp.ingrediente=="5":
                ingrediente="Costilla"
            text+="     <TD>Ingrediente</TD>\n"
            text+="     <TD>"+ingrediente+"</TD>\n"
            text+=" </TR>\n"
            
            text+=" <TR>\n"
            text+="     <TD>Tiempo en cola</TD>\n"
            text+="     <TD>"+str(temp.tiempo)+" min</TD>\n"
            text+=" </TR>\n"
            
            text+=" <TR>\n"
            text+="     <TD>Tiempo total</TD>\n"
            text+="     <TD>"+str(int(tiempoTotal))+" min</TD>\n"
            text+=" </TR>\n"
            tiempoTotal-=temp.tiempo
            text+=" </TABLE>>];\n"
            
            if estructura<Num:
                text+="\n"
                text+="Orden"+str(estructura+1)+"->Orden"+str(estructura)+"\n"
                text+="\n"
            
            temp=temp.anterior
            estructura-=1
            if temp==NULL:
                print("nodo listo")
                break

        return text


    def grafica(self):
        global N
        if self.estaVacia():
            print("")
        else:
            N+=1
            contenido="digraph G{\n\n"
            r=open("grafica.txt","w")
            contenido+=self.CuerpoGrafica()
            contenido+="\n}"
            r.write(contenido)
            r.close()
            print("Gráfica generada")
            os.system("dot -Tpng grafica.txt -o Gráficas/Gráfica"+str(N)+".png") 

    def eliminar_inicio(self):
        global Num, tiempoGeneral
        if self.primero==None:
            input(Fore.LIGHTBLUE_EX+"No hay ordenes. ")

        else:
            temp=self.primero
            Num-=1
            tiempoGeneral-=int(temp.tiempo)
            print(Fore.RED+"---------------- Orden Eliminada ----------------")
            print(Fore.GREEN+"Nombre: "+        Fore.LIGHTYELLOW_EX+    temp.nombre)
            print(Fore.GREEN+"Dirección: "+     Fore.LIGHTYELLOW_EX+    temp.dirección)
            print(Fore.GREEN+"NIT: "+           Fore.LIGHTYELLOW_EX+    temp.nit)
            print(Fore.GREEN+"Forma de pago: "+ Fore.LIGHTYELLOW_EX+    temp.formaPago)
            if temp.ingrediente=="1":
                ingrediente="Salchicha"
            elif temp.ingrediente=="2":
                ingrediente="Chorizo"
            elif temp.ingrediente=="3":
                ingrediente="Salami"
            elif temp.ingrediente=="4":
                ingrediente="Longaniza"
            elif temp.ingrediente=="5":
                ingrediente="Costilla"
            print(Fore.GREEN+"Ingrediente: "+   Fore.LIGHTYELLOW_EX+    ingrediente)
            print(Fore.GREEN+"Cantidad: "+      Fore.LIGHTYELLOW_EX+    temp.cantidad)
            print(Fore.GREEN+"Tiempo de preparación: "+Fore.LIGHTYELLOW_EX+str(temp.tiempo))
            print(Fore.RED+"vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
            if self.estaVacia():
                print(Fore.LIGHTBLUE_EX+"AVISO: Ya no hay ordenes por atender.")
            elif self.primero==self.ultimo:
                self.primero=self.ultimo=None
            else:
                self.primero=self.primero.siguiente
            input(Fore.LIGHTBLUE_EX+"Orden eliminada. ")
            self.grafica()
            self.UnirNodos()