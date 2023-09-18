from tkinter import *
from tkinter import ttk
import tkinter.messagebox

## Variables globales
lista=[]
lista2=[]
listaIvalidos=[]

## ---------------------Leer documento----------------------------
def seleccionar(Entrada):

    ## Variables de función
    global lista
    condición2=1
    condición3=1
    i=0
    
    def cursosAmbos():
        def regresar():
            vGestionar.destroy()
            tkinter.messagebox.showinfo("Carga extiosa",  "Se termino de cargar el archivo") 
        
        vGestionar = Tk(className=" Lista de Cursos Repetidos")
        vGestionar.columnconfigure(0,weight=1)
        vGestionar.rowconfigure(0,weight=1)
        vGestionar.config(bg="#298FFC",relief="sunken")
        vGestionar.resizable(False, False)

        ## Label 1
        Repetido=Label(vGestionar,text="Cursos Repetidos",bg="#FC9F29",fg="#6A4201")
        Repetido.grid(row=0, column=0,columnspan=7,pady=10,ipady=1)
        Repetido.config(width=15)

        ## Tabla
        tablaR=ttk.Treeview(vGestionar,columns=[f"#{n}" for n in range (1, 7)],height=5)
        tablaR.grid(row=1,column=0,columnspan=7)

        tablaR.heading("#0",text="Código",anchor=CENTER)
        tablaR.heading("#1",text="Nombre")
        tablaR.heading("#2",text="Prerrequisito",anchor=CENTER)
        tablaR.heading("#3",text="Opcionalidad",anchor=CENTER)
        tablaR.heading("#4",text="Semestre",anchor=CENTER)
        tablaR.heading("#5",text="Créditos",anchor=CENTER)
        tablaR.heading("#6",text="Estado",anchor=CENTER)

        tablaR.column("#0",width=50,anchor=CENTER)
        tablaR.column("#1",width=250,anchor=CENTER)
        tablaR.column("#2",width=100,anchor=CENTER)
        tablaR.column("#3",width=90 ,anchor=CENTER)
        tablaR.column("#4",width=70,anchor=CENTER)
        tablaR.column("#5",width=70,anchor=CENTER)
        tablaR.column("#6",width=70,anchor=CENTER)
        for r in range(0,len(lista2)):        
            tablaR.insert("",0,text=lista2[r]["Código"],values=(lista2[r]["Nombre"],lista2[r]["Prerrequisito"],lista2[r]["Opcionalidad"],lista2[r]["Semestre"],lista2[r]["Créditos"],lista2[r]["Estado"]))

        ## Label 2
        Parámetro=Label(vGestionar,text="Cursos con parámetros inválidos",bg="#FC9F29",fg="#6A4201")
        Parámetro.grid(row=2, column=0,columnspan=7,pady=5,ipady=1)

        ## Tabla
        tabla=ttk.Treeview(vGestionar,columns=[f"#{n}" for n in range (1, 7)],height=5)
        tabla.grid(row=3,column=0,columnspan=7)

        tabla.heading("#0",text="Código",anchor=CENTER)
        tabla.heading("#1",text="Nombre")
        tabla.heading("#2",text="Prerrequisito",anchor=CENTER)
        tabla.heading("#3",text="Opcionalidad",anchor=CENTER)
        tabla.heading("#4",text="Semestre",anchor=CENTER)
        tabla.heading("#5",text="Créditos",anchor=CENTER)
        tabla.heading("#6",text="Estado",anchor=CENTER)

        tabla.column("#0",width=50,anchor=CENTER)
        tabla.column("#1",width=250,anchor=CENTER)
        tabla.column("#2",width=100,anchor=CENTER)
        tabla.column("#3",width=90 ,anchor=CENTER)
        tabla.column("#4",width=70,anchor=CENTER)
        tabla.column("#5",width=70,anchor=CENTER)
        tabla.column("#6",width=70,anchor=CENTER)
        for r in range(0,len(listaIvalidos)):        
            tabla.insert("",0,text=listaIvalidos[r]["Código"],values=(listaIvalidos[r]["Nombre"],listaIvalidos[r]["Prerrequisito"],listaIvalidos[r]["Opcionalidad"],listaIvalidos[r]["Semestre"],listaIvalidos[r]["Créditos"],listaIvalidos[r]["Estado"]))

        ## Botón de regresar
        BotonRegresar=ttk.Button(vGestionar,text="Salir",command=regresar)
        BotonRegresar.grid(row=4, column=0,columnspan=7,pady=5,ipady=1)
        BotonRegresar.config(width=15)

    def cursosRepetidos():

        def regresar():
            vGestionar.destroy()
            tkinter.messagebox.showinfo("Carga extiosa",  "Se termino de cargar el archivo") 
        
        vGestionar = Tk(className=" Lista de Cursos Repetidos")
        vGestionar.columnconfigure(0,weight=1)
        vGestionar.rowconfigure(0,weight=1)
        vGestionar.config(bg="#298FFC",relief="sunken")
        vGestionar.resizable(False, False)

        ## Label 1
        Repetido=Label(vGestionar,text="Cursos Repetidos",bg="#FC9F29",fg="#6A4201")
        Repetido.grid(row=0, column=0,columnspan=7,pady=10,padx=20,ipady=0)
        Repetido.config(width=15) 

        ## Botón de regresar
        BotonRegresar=ttk.Button(vGestionar,text="Salir",command=regresar)
        BotonRegresar.grid(row=2, column=0,columnspan=7,pady=5,ipady=1)
        BotonRegresar.config(width=15)

        ## Tabla
        tabla=ttk.Treeview(vGestionar,columns=[f"#{n}" for n in range (1, 2)],height=10)
        tabla.grid(row=1,column=0,columnspan=7)

        tabla.heading("#0",text="Código",anchor=CENTER)
        tabla.heading("#1",text="Nombre")

        tabla.column("#0",width=50,anchor=CENTER)
        tabla.column("#1",width=250,anchor=CENTER)

        for r in range(0,len(lista2)):        
            tabla.insert("",0,text=lista2[r]["Código"],values=(lista2[r]["Nombre"]))

    def cursosInvalidos():

        def regresar():
            vGestionar.destroy()
            tkinter.messagebox.showinfo("Carga extiosa",  "Se termino de cargar el archivo") 
        
        vGestionar = Tk(className=" Lista")
        vGestionar.columnconfigure(0,weight=1)
        vGestionar.rowconfigure(0,weight=1)
        vGestionar.config(bg="#298FFC",relief="sunken")
        vGestionar.resizable(False, False)

        ## Label 1
        Repetido=Label(vGestionar,text="Cursos con información inválida",bg="#FC9F29",fg="#6A4201")
        Repetido.grid(row=0, column=0,columnspan=7,pady=10,ipady=1)
        Repetido.config(width=15) 

        ## Botón de regresar
        BotonRegresar=ttk.Button(vGestionar,text="Salir",command=regresar)
        BotonRegresar.grid(row=2, column=0,columnspan=7,pady=5,ipady=1)
        BotonRegresar.config(width=15)

        ## Tabla
        tablaR=ttk.Treeview(vGestionar,columns=[f"#{n}" for n in range (1, 7)],height=10)
        tablaR.grid(row=1,column=0,columnspan=7)

        tablaR.heading("#0",text="Código",anchor=CENTER)
        tablaR.heading("#1",text="Nombre")
        tablaR.heading("#2",text="Prerrequisito",anchor=CENTER)
        tablaR.heading("#3",text="Opcionalidad",anchor=CENTER)
        tablaR.heading("#4",text="Semestre",anchor=CENTER)
        tablaR.heading("#5",text="Créditos",anchor=CENTER)
        tablaR.heading("#6",text="Estado",anchor=CENTER)

        tablaR.column("#0",width=50,anchor=CENTER)
        tablaR.column("#1",width=250,anchor=CENTER)
        tablaR.column("#2",width=100,anchor=CENTER)
        tablaR.column("#3",width=90 ,anchor=CENTER)
        tablaR.column("#4",width=70,anchor=CENTER)
        tablaR.column("#5",width=70,anchor=CENTER)
        tablaR.column("#6",width=70,anchor=CENTER)

        for r in range(0,len(listaIvalidos)):        
            tablaR.insert("",0,text=listaIvalidos[r]["Código"],values=(listaIvalidos[r]["Nombre"],listaIvalidos[r]["Prerrequisito"],listaIvalidos[r]["Opcionalidad"],listaIvalidos[r]["Semestre"],listaIvalidos[r]["Créditos"],listaIvalidos[r]["Estado"]))

    ## Entrada de ruta
    Documento= open(Entrada, 'r+',encoding="utf-8")
    ## Se divide en lineas el documento
    linea = Documento.readline()

    ## itera todas las líneas
    while linea != '':
        ## Condición se usar para saltar o no el "append" en la lista
        condición=1
        j=0

        ## Se separa en una cadena la línea
        temp=linea.split(sep=',')

        ## validar el prerrequisito 
        if temp[2]=='':
            temp[2]='Ninguno'

        if temp[3]=="0":
            temp[3]="Opcional"
        elif temp[3]=="1":
            temp[3]="Obligatorio"

        ## Quitamos el '\n'
        if '0\n' == temp[6] or "0" ==temp[6]:
            temp[6]='Aprobado'
        elif "-1\n" == temp[6] or "-1" ==temp[6]:
            temp[6]='Pendiente'
        elif "1\n" ==temp[6] or "1" ==temp[6] :
            temp[6]='Cursando'

## ----------------------------------------------------- Crear directorio ---------------------------------------------------------------------        
        directorio={"Código":temp[0],"Nombre":temp[1],"Prerrequisito":temp[2],"Opcionalidad":temp[3],"Semestre":temp[4],"Créditos":temp[5],"Estado":temp[6]}
        
        ## Analizar parámetros
        if not directorio["Código"].isnumeric():
            print("op1")
            listaIvalidos.append(directorio)
            condición3=0
            linea = Documento.readline()
            continue
        elif not (directorio["Prerrequisito"].isnumeric() or directorio["Prerrequisito"]=="Ninguno" or (";" in directorio["Prerrequisito"])):
            listaIvalidos.append(directorio)
            condición3=0
            print("op2")
            linea = Documento.readline()
            continue
        elif not (directorio["Opcionalidad"]=="Obligatorio" or directorio["Opcionalidad"]=="Opcional"):
            listaIvalidos.append(directorio)
            condición3=0
            print("op3")
            linea = Documento.readline()
            continue
        elif not directorio["Semestre"].isnumeric(): #and directorio["Semestre"] in rangoN:
            listaIvalidos.append(directorio)
            condición3=0
            print("op4")
            linea = Documento.readline()
            continue
        elif not directorio["Créditos"].isnumeric():
            listaIvalidos.append(directorio)
            condición3=0
            print("op5")
            linea = Documento.readline()
            continue
        elif not (directorio["Estado"]=="Cursando" or directorio["Estado"]=="Pendiente" or directorio["Estado"]=="Aprobado"):
            listaIvalidos.append(directorio)
            condición3=0
            print("op6")
            linea = Documento.readline()
            continue
        
        ## if para validar lista vacía
        if not lista:
            lista.append(directorio)
            print(lista[i])
            i+=1
            condición=0
        
        ## else para buscar diccionarios repetidos
        else:
            for j in range(0,len(lista)):
                if directorio["Código"] == lista[j]["Código"]:
                    lista[j]=directorio
                    lista2.append(directorio)
                    condición=0
                    condición2=0
                    print("repetido")
                    print(lista[j])
                    break
        
        ## if para omitir el append
        if condición==1:
            lista.append(directorio)
            print(lista[i])
            i+=1
        
        linea = Documento.readline()

    if condición3==0 and condición2==0:
        if tkinter.messagebox.askyesno("Cursos no añadidos",  "Se encontró información inválida y repetida, ¿Quiere verlos?"):
            cursosAmbos()
        else:
            condición3=1
            condición2=1
    
    if condición2==0 and condición3==1:
            if tkinter.messagebox.askyesno("Cursos repetidos",  "Se encontró cursos repetidos, ¿Quiere verlos?"):
                cursosRepetidos()
            else:
                condición2=1

    if condición3==0 and condición2==1:
        if tkinter.messagebox.askyesno("Cursos no añadidos",  "Se encontró cursos con parámetros inválidos, ¿Quiere verlos?"):
            cursosInvalidos()
        else:
            condición3=1
    Documento.close()

    ## Ventana emergente
    if condición2!=0 and condición3!=0:
        tkinter.messagebox.showinfo("Carga extiosa",  "Se termino de cargar el archivo") 

    return lista

## -------------------------------- Diseño de ventana cargar ---------------------------------
def diseñoCargar(VentanaC,FondoVentana2,text1,etiquetaRuta,MarcoVentana2,BotonCarga,BotonRegresar):

    VentanaC.config(bg="#298FFC",relief="sunken")
    VentanaC.resizable(False, False)
    VentanaC.title("Cargar Archivos")
    VentanaC.geometry("557x300")

    FondoVentana2.grid(row=0, column=0,columnspan=1,padx=(30,30), pady=(40,40))
    FondoVentana2.columnconfigure(0,weight=1)
    FondoVentana2.rowconfigure(0,weight=1)

    text1.config(background="#298FFC",font=("Verdana",11)) 
    text1.grid(row=1, column=1,columnspan=10)

    etiquetaRuta.config(bg="#F6DDCC",fg="#6A4201",font=("Verdana",11)) 
    etiquetaRuta.grid(row=2, column=2,columnspan=9,ipadx=200,padx=9)

    MarcoVentana2.grid(row=3, column=1,columnspan=10,pady=5,ipady=0)
    MarcoVentana2.config(width=30,bg="#298FFC")

    BotonCarga.grid(row=4, column=1,columnspan=10,pady=5,ipady=5)
    BotonCarga.config(width=15)

    BotonRegresar.grid(row=5, column=1,columnspan=10,pady=5,ipady=5)
    BotonRegresar.config(width=15)
