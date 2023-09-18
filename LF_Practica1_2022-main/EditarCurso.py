from tkinter import *
import tkinter.messagebox
from Cargar import lista
## Variables globales
condición3=1
condiciónEditar=1
Condición=1

## Función Buscar
def buscarEditar(Código):
    global condiciónEditar
    global Condición
    if Código.isnumeric():
        Condición=1
        for j in range(0,len(lista)):
            if Código == lista[j]["Código"]:
                Condición=0
                condiciónEditar=j
                break
        if Condición==1:
            tkinter.messagebox.showinfo("No encontrado",  "No se encontró el curso")
    else:
        tkinter.messagebox.showinfo("Código inválido",  "Ingresar un código numérico")
        Condición=1

## Función de editar
def gestionarEditar(j,Nombre,Prerrequisito,Opcionalidad,Semestre,Créditos,Estado):
    global condición3
    condición3=1
    if not (Prerrequisito.isnumeric() or Prerrequisito=="Ninguno" or (";" in Prerrequisito)):
        print("op2")
        tkinter.messagebox.showinfo("Prerrequisito inválido",  "Ingrese un valor válido en prerrequisito")
        condición3=0
    elif not (Opcionalidad=="Obligatorio" or Opcionalidad=="Opcional"):
        print("op3")
        tkinter.messagebox.showinfo("Opcionalidad inválido",  "Ingrese una opcionalidad válida")
        condición3=0
    elif not Semestre.isnumeric(): #and directorio["Semestre"] in rangoN:
        print("op4")
        tkinter.messagebox.showinfo("Semestre inválido",  "Ingrese un valor válido en semestre")
        condición3=0
    elif not Créditos.isnumeric():
        print("op5")
        tkinter.messagebox.showinfo("Dato inválido",  "Ingrese un valor válido en créditos")
        condición3=0
    elif not (Estado=="Cursando" or Estado=="Pendiente" or Estado=="Aprobado"):
        print("op6")
        tkinter.messagebox.showinfo("Estado ingresado inválido",  "Ingrese un estado válido")
        condición3=0

    if condición3==1:
        lista[j]["Nombre"]=Nombre
        lista[j]["Prerrequisito"]= Prerrequisito
        lista[j]["Semestre"]=Semestre
        lista[j]["Opcionalidad"]=Opcionalidad
        lista[j]["Créditos"]=Créditos
        lista[j]["Estado"]=Estado
        tkinter.messagebox.showinfo("Curso Editado",  "Se editó correctamente el curso.") 

### -------------------------------------- Diseño de Editar Curso ------------------------------------------------

##  Diseño ventana de busqueda
def valoresBusqueda(vGestionar,Marco,Código,TCódigo,Marco2,TBotonAgregar,TBotonRegresar,Marco3):
    
    vGestionar.title(" Editar")
    vGestionar.columnconfigure(0,weight=1)
    vGestionar.rowconfigure(0,weight=1)
    vGestionar.config(bg="#298FFC",relief="sunken")
    vGestionar.resizable(False, False)

    Marco.grid(row=0, column=0,columnspan=5,padx=30,ipadx=70,pady=10)
    Marco.config(width=30,bg="#6A4201")

    Código.config(bg="#298FFC",font=("Verdana",11),fg="#FFFFFF") 
    Código.grid(row=1, column=1,padx=0,pady=5,columnspan=1,sticky=E+W)

    TCódigo.config(bg="#FC9F29",fg = "#6A4201") 
    TCódigo.insert(0, 'Código completo del curso a editar')
    TCódigo.grid(row=1, column=2,columnspan=2,padx=0,ipadx=15,pady=5,sticky=E+W)

    Marco2.grid(row=2, column=0,columnspan=5,ipadx=20,pady=10,padx=30)
    Marco2.config(width=30,bg="#298FFC")

    TBotonAgregar.grid(row=3, column=0,columnspan=5,padx=20,pady=5,ipady=0)
    TBotonAgregar.config(width=13)

    TBotonRegresar.grid(row=4, column=0,columnspan=5,padx=20,pady=5,ipady=0)
    TBotonRegresar.config(width=13)

    Marco3.grid(row=5, column=0,columnspan=5,padx=30,ipadx=70,pady=10)
    Marco3.config(width=30,bg="#6A4201")

## Labels
def valoresLabelsE(vEdición,Marco,Código,Nombre,Prerrequisito,Opcionalidad,Semestre,Créditos,Estado,Marco2):
    vEdición.title("Editar curso")
    vEdición.columnconfigure(0,weight=1)
    vEdición.rowconfigure(0,weight=1)
    vEdición.config(bg="#298FFC",relief="sunken")
    vEdición.resizable(False, False)

    Marco.grid(row=0, column=0,columnspan=5,ipadx=50,pady=10)
    Marco.config(width=30,bg="#6A4201")

    Código.config(bg="#298FFC",font=("Verdana",11),fg="#FFFFFF") 
    Código.grid(row=1, column=1,padx=10,pady=10,columnspan=4,sticky=E+W)

    Nombre.config(bg="#298FFC",font=("Verdana",11),fg="#FFFFFF") 
    Nombre.grid(row=2, column=1,padx=10,pady=10,sticky=E+W)

    Prerrequisito.config(bg="#298FFC",font=("Verdana",11),fg="#FFFFFF") 
    Prerrequisito.grid(row=3, column=1,padx=10,pady=10,sticky=E+W)

    Opcionalidad.config(bg="#298FFC",font=("Verdana",11),fg="#FFFFFF") 
    Opcionalidad.grid(row=4, column=1,padx=10,pady=10,sticky=E+W)

    Semestre.config(bg="#298FFC",font=("Verdana",11),fg="#FFFFFF") 
    Semestre.grid(row=5, column=1,padx=10,pady=10,sticky=E+W)

    Créditos.config(bg="#298FFC",font=("Verdana",11),fg="#FFFFFF") 
    Créditos.grid(row=6, column=1,padx=10,pady=10,sticky=E+W)

    Estado.config(bg="#298FFC",font=("Verdana",11),fg="#FFFFFF") 
    Estado.grid(row=7, column=1,padx=10,pady=10,sticky=E+W)

    Marco2.grid(row=8, column=0,columnspan=5,ipadx=50,pady=10)
    Marco2.config(width=30,bg="#6A4201")

## Entrys y botones
def valoresEntrysE(j,TNombre,TPrerrequisito,TOpcionalidad,TSemestre,TCréditos,TEstado,TBotonAgregar,TBotonRegresar):

    TNombre.config(bg="#FC9F29",fg="#6A4201") 
    TNombre.insert(0, lista[j]["Nombre"])
    TNombre.grid(row=2, column=2,columnspan=3,padx=10,pady=10,sticky=E+W)

    TPrerrequisito.config(bg="#FC9F29",fg="#6A4201")
    TPrerrequisito.insert(0, lista[j]["Prerrequisito"])
    TPrerrequisito.grid(row=3, column=2,columnspan=3,padx=10,pady=10,sticky=E+W)

    TOpcionalidad.config(bg="#FC9F29",fg="#6A4201")
    TOpcionalidad.insert(0, lista[j]["Opcionalidad"])
    TOpcionalidad.grid(row=4, column=2,columnspan=3,padx=10,pady=10,sticky=E+W)

    TSemestre.config(bg="#FC9F29",fg="#6A4201")
    TSemestre.insert(0, lista[j]["Semestre"])
    TSemestre.grid(row=5, column=2,columnspan=3,padx=10,pady=10,sticky=E+W)

    TCréditos.config(bg="#FC9F29",fg="#6A4201") 
    TCréditos.insert(0, lista[j]["Créditos"])
    TCréditos.grid(row=6, column=2,columnspan=3,padx=10,pady=10,sticky=E+W)

    TEstado.config(bg="#FC9F29",fg="#6A4201")
    TEstado.insert(0, lista[j]["Estado"])
    TEstado.grid(row=7, column=2,columnspan=3,padx=10,pady=10,sticky=E+W)

    TBotonAgregar.grid(row=9, column=1,columnspan=5,pady=5,ipady=1)
    TBotonAgregar.config(width=14)

    TBotonRegresar.grid(row=10, column=1,columnspan=5,pady=5,ipady=1)
    TBotonRegresar.config(width=14)