from tkinter import *
import tkinter.messagebox
from Cargar import lista
## Variable globales
condiciónAgregar=1

## Función para agregar cursos
def Agregar(Código,Nombre,Prerrequisito,Opcionalidad,Semestre,Créditos,Estado):
    global condiciónAgregar
    condiciónAgregar=1
    condición=1
    str(Código)
        
    directorio={"Código":Código,"Nombre":Nombre,"Prerrequisito":Prerrequisito,"Opcionalidad":Opcionalidad,"Semestre":Semestre,"Créditos":Créditos,"Estado":Estado}
    j=0

    if not directorio["Código"].isnumeric():
        print("op1")
        tkinter.messagebox.showinfo("Código inválido",  "Ingrese un código válido")
        condiciónAgregar=0
    elif not (directorio["Prerrequisito"].isnumeric() or directorio["Prerrequisito"]=="Ninguno" or (";" in directorio["Prerrequisito"])):
        print("op2")
        tkinter.messagebox.showinfo("Prerrequisito inválido",  "Ingrese un valor válido en prerrequisito")
        condiciónAgregar=0
    elif not (directorio["Opcionalidad"]=="Obligatorio" or directorio["Opcionalidad"]=="Opcional"):
        print("op3")
        tkinter.messagebox.showinfo("Opcionalidad inválido",  "Ingrese una opcionalidad válida")
        condiciónAgregar=0
    elif not directorio["Semestre"].isnumeric(): #and directorio["Semestre"] in rangoN:
        print("op4")
        tkinter.messagebox.showinfo("Semestre inválido",  "Ingrese un valor válido en semestre")
        condiciónAgregar=0
    elif not directorio["Créditos"].isnumeric():
        print("op5")
        tkinter.messagebox.showinfo("Dato inválido",  "Ingrese un valor válido en créditos")
        condiciónAgregar=0
    elif not (directorio["Estado"]=="Cursando" or directorio["Estado"]=="Pendiente" or directorio["Estado"]=="Aprobado"):
        print("op6")
        tkinter.messagebox.showinfo("Estado ingresado inválido",  "Ingrese un estado válido")
        condiciónAgregar=0


    if condiciónAgregar==1:
        ## if para validar lista vacía
        if not lista:
            lista.append(directorio)
            print(lista[-1])
            condición=0
            tkinter.messagebox.showinfo("Curso Añadido",  "Se añadió el curso con éxito")
        ## else para buscar diccionarios repetidos
        else:
            for j in range(0,len(lista)):
                if directorio["Código"] == lista[j]["Código"]:    
                    ## Ventana emergente
                    condición=0
                    if tkinter.messagebox.askyesno(message="Se reemplazará la información del curso. ¿Desea continuar?", title= "Curso Repetido"): 
                        lista[j]=directorio
                        print("valor repetido encontrado")
                        condición=0
                        print(lista[j])
                        tkinter.messagebox.showinfo("Curso Añadido",  "Se añadió el curso con éxito") 
                        break
                    else:
                        tkinter.messagebox.showinfo("Cancelado",  "Proceso cancelado") 
        
        ## if para omitir el append
        if condición==1:
            lista.append(directorio)
            print(lista[-1])
            tkinter.messagebox.showinfo("Curso Añadido",  "Se añadió el curso con éxito")

### ----------------------------------- Diseño de ventana agregar ------------------------------------

## Labels y ventana agregar
def valoresLabelsA(vGestionar,Marco,Código,Nombre,Prerrequisito,Opcionalidad,Semestre,Créditos,Estado,Marco2):

    vGestionar.title(" Agregar Cursos")
    vGestionar.columnconfigure(0,weight=1)
    vGestionar.rowconfigure(0,weight=1)
    vGestionar.config(bg="#298FFC",relief="sunken")
    vGestionar.resizable(False, False)

    Marco.grid(row=0, column=0,columnspan=5,ipadx=50,pady=10)
    Marco.config(width=30,bg="#6A4201")

    Código.config(bg="#298FFC",font=("Verdana",11),fg="#FFFFFF") 
    Código.grid(row=1, column=1,padx=10,pady=10,sticky=E+W)

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
def valoresEntrysA(TCódigo,TNombre,TPrerrequisito,TOpcionalidad,TSemestre,TCréditos,TEstado,TBotonAgregar,TBotonRegresar):

    TCódigo.config(bg="#FC9F29",fg = "#6A4201") 
    TCódigo.insert(0, '0000')
    TCódigo.grid(row=1, column=2,columnspan=3,padx=10,ipadx=25,pady=10,sticky=E+W)

    TNombre.config(bg="#FC9F29",fg="#6A4201") 
    TNombre.insert(0, 'Nombre del Curso')
    TNombre.grid(row=2, column=2,columnspan=3,padx=10,pady=10,sticky=E+W)

    TPrerrequisito.config(bg="#FC9F29",fg="#6A4201")
    TPrerrequisito.insert(0, 'Ninguno ó 0000;0000;0000...')
    TPrerrequisito.grid(row=3, column=2,columnspan=3,padx=10,pady=10,sticky=E+W)

    TOpcionalidad.config(bg="#FC9F29",fg="#6A4201")
    TOpcionalidad.insert(0, 'Obligatorio/Opcional')
    TOpcionalidad.grid(row=4, column=2,columnspan=3,padx=10,pady=10,sticky=E+W)

    TSemestre.config(bg="#FC9F29",fg="#6A4201")
    TSemestre.insert(0, 'No.')
    TSemestre.grid(row=5, column=2,columnspan=3,padx=10,pady=10,sticky=E+W)

    TCréditos.config(bg="#FC9F29",fg="#6A4201") 
    TCréditos.insert(0, 'No.')
    TCréditos.grid(row=6, column=2,columnspan=3,padx=10,pady=10,sticky=E+W)

    TEstado.config(bg="#FC9F29",fg="#6A4201")
    TEstado.insert(0, 'Aprobado/Cursando/Pendiente')
    TEstado.grid(row=7, column=2,columnspan=3,padx=10,pady=10,sticky=E+W)

    TBotonAgregar.grid(row=9, column=1,columnspan=5,pady=5,ipady=1)
    TBotonAgregar.config(width=14)

    TBotonRegresar.grid(row=10, column=1,columnspan=5,pady=5,ipady=1)
    TBotonRegresar.config(width=14)