from tkinter import *
from tkinter import ttk
from Cargar import lista

def gestionarLista():

    def actualizar():
        for item in tabla.get_children():
            tabla.delete(item)

        for r in range(0,len(lista)):        
            tabla.insert("",0,text=lista[r]["Código"],values=(lista[r]["Nombre"],lista[r]["Prerrequisito"],lista[r]["Opcionalidad"],lista[r]["Semestre"],lista[r]["Créditos"],lista[r]["Estado"]))
    
    def regresar():
        vGestionar.destroy()
    
    vGestionar = Tk(className=" Lista de Cursos")
    vGestionar.columnconfigure(0,weight=1)
    vGestionar.rowconfigure(0,weight=1)
    vGestionar.config(bg="#298FFC",relief="sunken")
    vGestionar.resizable(False, False)

    ## Tabla
    tabla=ttk.Treeview(vGestionar,columns=[f"#{n}" for n in range (1, 7)],height=20)
    tabla.grid(row=0,column=0,columnspan=7)

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

    for r in range(0,len(lista)):        
        tabla.insert("",0,text=lista[r]["Código"],values=(lista[r]["Nombre"],lista[r]["Prerrequisito"],lista[r]["Opcionalidad"],lista[r]["Semestre"],lista[r]["Créditos"],lista[r]["Estado"]))    
    
    ## Botón de actualizar
    BotonActualizar=ttk.Button(vGestionar,text="Actualizar",command=actualizar)
    BotonActualizar.grid(row=1, column=0,columnspan=7,pady=5,ipady=1)
    BotonActualizar.config(width=15)

    ## Botón de regresar
    BotonRegresar=ttk.Button(vGestionar,text="Salir",command=regresar)
    BotonRegresar.grid(row=2, column=0,columnspan=7,pady=5,ipady=1)
    BotonRegresar.config(width=15)

    vGestionar.mainloop()

