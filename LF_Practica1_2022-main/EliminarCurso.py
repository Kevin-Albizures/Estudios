from tkinter import *
import tkinter.messagebox
from Cargar import lista

## Variables globales
condiciónEliminar=1
CondiciónE1=1

## Función de buscar curso
def buscarEliminar(Código):
    global condiciónEliminar
    global CondiciónE1
    if Código.isnumeric():
        CondiciónE1=1
        for j in range(0,len(lista)):
            if Código == lista[j]["Código"]:
                CondiciónE1=0
                condiciónEliminar=j
                break
        if CondiciónE1==1:
            tkinter.messagebox.showinfo("No encontrado",  "No se encontró el curso")
    else:
        tkinter.messagebox.showinfo("Código inválido",  "Ingresar un código numérico")
        CondiciónE1=1

### ------------------------------------ Diseño de ventana eliminar ------------------------------------------------------
def valoresEliminar(vGestionar,Marco,Código,TCódigo,Marco2,TBotonAgregar,TBotonRegresar,Marco3):
    vGestionar.title(" Eliminar")
    vGestionar.columnconfigure(0,weight=1)
    vGestionar.rowconfigure(0,weight=1)
    vGestionar.config(bg="#298FFC",relief="sunken")
    vGestionar.resizable(False, False)

    Marco.grid(row=0, column=0,columnspan=5,padx=30,ipadx=70,pady=10)
    Marco.config(width=30,bg="#6A4201")

    Código.config(bg="#298FFC",font=("Verdana",11),fg="#FFFFFF") 
    Código.grid(row=1, column=1,padx=0,pady=5,columnspan=1,sticky=E+W)

    TCódigo.config(bg="#FC9F29",fg = "#6A4201") 
    TCódigo.insert(0, 'Código completo del curso a eliminar')
    TCódigo.grid(row=1, column=2,columnspan=2,padx=0,ipadx=15,pady=5,sticky=E+W)

    Marco2.grid(row=2, column=0,columnspan=5,ipadx=20,pady=10,padx=30)
    Marco2.config(width=30,bg="#298FFC")

    TBotonAgregar.grid(row=3, column=0,columnspan=5,padx=20,pady=5,ipady=0)
    TBotonAgregar.config(width=13)

    TBotonRegresar.grid(row=4, column=0,columnspan=5,padx=20,pady=5,ipady=0)
    TBotonRegresar.config(width=13)
    
    Marco3.grid(row=5, column=0,columnspan=5,padx=30,ipadx=70,pady=10)
    Marco3.config(width=30,bg="#6A4201")
