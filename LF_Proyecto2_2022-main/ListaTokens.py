from tkinter import *
from tkinter import ttk
from Analizador import ListaTokens

def gestionarLista():
    global ListaTokens
    #print(ListaTokens)

    def actualizar():
        for item in tabla.get_children():
            tabla.delete(item)

        for r in range(len(ListaTokens)-1,-1,-1):        
            tabla.insert("",0,text=ListaTokens[r]["NO"],values=(ListaTokens[r]["Token"],ListaTokens[r]["Lexema"]))
    
    def regresar():
        vGestionar.destroy()
    
    vGestionar = Tk(className=" Lista de Tokens")
    vGestionar.columnconfigure(0,weight=1)
    vGestionar.rowconfigure(0,weight=1)
    vGestionar.config(bg="#298FFC",relief="sunken")
    vGestionar.resizable(False, False)

    ## Tabla
    tabla=ttk.Treeview(vGestionar,columns=[f"#{n}" for n in range (1, 3)],height=20)
    tabla.grid(row=0,column=0,columnspan=3)

    tabla.heading("#0",text="No",anchor=CENTER)
    tabla.heading("#1",text="Token")
    tabla.heading("#2",text="Lexema",anchor=CENTER)

    tabla.column("#0",width=50,anchor=CENTER)
    tabla.column("#1",width=100,anchor=CENTER)
    tabla.column("#2",width=250,anchor=CENTER)

    for r in range(len(ListaTokens)-1,-1,-1):        
        tabla.insert("",0,text=ListaTokens[r]["NO"],values=(ListaTokens[r]["Token"],ListaTokens[r]["Lexema"]))
    
    ## Botón de actualizar
    BotonActualizar=ttk.Button(vGestionar,text="Actualizar",command=actualizar)
    BotonActualizar.grid(row=1, column=0,columnspan=7,pady=5,ipady=1)
    BotonActualizar.config(width=15)

    ## Botón de regresar
    BotonRegresar=ttk.Button(vGestionar,text="Salir",command=regresar)
    BotonRegresar.grid(row=2, column=0,columnspan=7,pady=5,ipady=1)
    BotonRegresar.config(width=15)
    ListaTokens.clear()

    vGestionar.mainloop()

