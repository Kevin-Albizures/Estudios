from tkinter import *

def valoresGestionar(VentanaG,FondoVentana3,BotonListar,BotonAgregar,BotonEditar,BotonEliminar,BotonRegresar,FondoVentana4):
    VentanaG.config(bg="#298FFC",relief="sunken")
    VentanaG.resizable(False, False)
    VentanaG.title("Gestionar Archivos")
    VentanaG.geometry("500x360")

    FondoVentana3.grid(row=0, column=0,columnspan=10,padx=200, ipadx=50,pady=20)
    FondoVentana3.columnconfigure(0,weight=1)
    FondoVentana3.rowconfigure(0,weight=1)

    BotonListar.grid(row=1, column=0,columnspan=10,pady=5,ipady=10)
    BotonListar.config(width=30)

    BotonAgregar.grid(row=2, column=0,columnspan=10,pady=5,ipady=10)
    BotonAgregar.config(width=30)

    BotonEditar.grid(row=3, column=0,columnspan=10,pady=5,ipady=10)
    BotonEditar.config(width=30)

    BotonEliminar.grid(row=4, column=0,columnspan=10,pady=5,ipady=10)
    BotonEliminar.config(width=30)

    BotonRegresar.grid(row=5, column=0,columnspan=10,pady=5,ipady=10)
    BotonRegresar.config(width=30)

    FondoVentana4.grid(row=6, column=0,columnspan=10,padx=200, ipadx=50,pady=20)
    FondoVentana4.columnconfigure(0,weight=1)
    FondoVentana4.rowconfigure(0,weight=1)