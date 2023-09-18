import xml.etree.ElementTree as ET
from tkinter import Tk, filedialog
from ListasCeldas import N1,N, ListaNodosDoble,sanas,contagiadas
from colorama import Fore
import os

nombre=list()
edad=list()
periodos=list()
m=list()
PacienteInv=list()
patrones=list()
saltar=list()
n=0
indice=0
v=0
patrones=list()
Patrones1=list()
Patrones2=list()
def reiniciarListas():
    global nombre,edad,periodos,m,PacienteInv,saltar,indice,n,v,patrones
    patrones.clear()
    nombre.clear()
    edad.clear()
    periodos.clear()
    m.clear()
    PacienteInv.clear()
    saltar.clear()
    indice=0
    n=0
    v=0

def refrescarPantalla2():
    os.system("cls")

def CargarArchivo():
    ##Ocultar ventana para usar mensaje emergente .-.
    ventana=Tk()
    ventana.withdraw()
    global nombre,edad,periodos,m,PacienteInv,saltar,indice,n
    global patrones,Patrones1,Patrones2
    global v

    if v==1:
        print("Información ya cargada.")
        input("Presione ENTER para regresar. ")

    if v==0:
        Patron="0.Inicial"
        ##Lectura del archivo con mensaje emergente
        ruta=filedialog.askopenfilename(title="Solo archivos xml")
        tree =ET.parse(ruta)
        root=tree.getroot() ## Obtiene la raíz
        #Variable para validar si hay pacientes inválidos
        k=0
        #
        for j in range(0,len(root)):
            if int(root[j][2].text)%10==0:
                nombre.append(root[j][0][0].text) ##Guarda los nombres
                edad.append(root[j][0][1].text)   ## Guarda la edad
                periodos.append(root[j][1].text)  ## Guarda los periodos
                m.append(root[j][2].text)         ## Guarda el multiplo
                saltar.append("no")
            else:
                saltar.append("si")
                nombre.append(root[j][0][0].text) ##Guarda los nombres
                edad.append(root[j][0][1].text)   ## Guarda la edad
                periodos.append(root[j][1].text)  ## Guarda los periodos
                PacienteInv.append(root[j][0][0].text)
                m.append(root[j][2].text)
                k=1

        for Multiplo in m:
            if saltar[n]=="si":
                n+=1
                sanas.append(0)
                contagiadas.append(0)
                N.append(0)
                N1.append(0)
            else:
                s=0
                c=0
                N.append(0)
                N1.append(0)
                patrones.append(ListaNodosDoble())
                Patrones1.append(ListaNodosDoble())
                Patrones2.append(ListaNodosDoble())
                for Numero in range(0,int(Multiplo)):
                    patrones[indice].agregarAListaAbajo("0")
                    Patrones1[indice].agregarAListaAbajo("0")
                    Patrones2[indice].agregarAListaAbajo("0")
                    s+=1
                    for Numero2 in range(0,int(Multiplo)-1):
                        patrones[indice].agregarAListaUltimo("0")
                        Patrones1[indice].agregarAListaAbajo("0")
                        Patrones2[indice].agregarAListaAbajo("0")
                        s+=1
                sanas.append(s)
                contagiadas.append(c)
                for remplazo in root[n][3]:
                    c+=1
                    patrones[indice].remplazar(Multiplo,remplazo.attrib["f"],remplazo.attrib["c"])
                    Patrones1[indice].remplazar(Multiplo,remplazo.attrib["f"],remplazo.attrib["c"])
                    Patrones2[indice].remplazar(Multiplo,remplazo.attrib["f"],remplazo.attrib["c"])
                contagiadas[n]=c
                sanas[n]-=c
                try:
                    os.mkdir("Paciente_"+nombre[n].replace(" ",""))
                except FileExistsError:
                    print("")
                
                patrones[indice].crearReporte(nombre[n],edad[n],Patron,Multiplo,str(sanas[n]),str(contagiadas[n]))

                indice+=1
                n+=1
                
        if k==1:
            print("")
            print(Fore.RED+"Número de rejilla no válido en paciente(s) ")
            print("Información no guardada de: ")
            for paciente in PacienteInv:
                print(paciente)
        print("")
        input(Fore.GREEN+"Archivo cargado correctamente.")
        
    
    v=1
    ventana.destroy()
    
    ##print(root[o][0][0].text)## Nombre
    ##print(root[o][0][1].text)## edad
    ##print(root[o][1].text)## Periodos
    ##print(root[o][2].text)## Multiplos

    #print(root[0][3][0].attrib["f"])##filas
    #print(root[0][3][0].attrib["c"])##filas
    ##print(len(root[0][3]))## cantidad

    ##print(root[1][0][0].text)## Nombre siguiente