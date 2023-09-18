from Cargar import lista
## Valores globales
Suma1=0
Suma2=0
Suma3=0

## Función suma de créditos fijos
def sumasCréditos():
    global Suma1
    global Suma2
    global Suma3

    Suma1=0
    Suma2=0
    Suma3=0

    for j in range(0,len(lista)):
        if lista[j]["Estado"]=="Aprobado":
            Suma1+=int(lista[j]["Créditos"])
        elif lista[j]["Estado"]=="Cursando":
            Suma2+=int(lista[j]["Créditos"])
        elif lista[j]["Estado"]=="Pendiente":
            Suma3+=int(lista[j]["Créditos"])

### -------------------------------- Diseño ventana de conteo ------------------------------------------------
def valoresConteo(vConteo,frame,Marco,Marco2,Marco3,Marco1,textoFijo1,CréditosAp,textoFijo2,CréditosCur,textoFijo3,CréditosPen,textoFijo4,CréditosSemestreO,
textoFijoT,TCreditosO,BotonO,textoFijo5,CréditosSemestre1,CréditosSemestre2,CréditosSemestre3,textoFijoS,TCreditos,BotonS,BotonRegresar):
    vConteo.config(bg="#298FFC",relief="sunken")
    vConteo.resizable(False, False)
    vConteo.title("Gestionar Archivos")
    vConteo.geometry("516x470")

    frame.grid(row=0, column=0,columnspan=10)#,padx=(30,30), pady=(40,40)
    frame.columnconfigure(0,weight=1)
    frame.rowconfigure(0,weight=1)

    Marco.grid(row=0, column=0,columnspan=12,ipadx=200,pady=4)
    Marco.config(width=30,bg="#298FFC")

    Marco2.grid(row=5, column=0,columnspan=12,ipadx=200,pady=10)
    Marco2.config(width=30,bg="#6A4201")

    Marco3.grid(row=8, column=0,columnspan=12,ipadx=200,pady=10)
    Marco3.config(width=30,bg="#6A4201")

    Marco1.grid(row=1, column=0,rowspan=9,pady=10)
    Marco1.config(width=30,bg="#298FFC")

    textoFijo1.config(background="#298FFC",font=("Verdana",11)) 
    textoFijo1.grid(row=2, column=1,columnspan=2)

    CréditosAp.grid(row=2,column=2,columnspan=2,pady=10,ipadx=10)

    textoFijo2.config(background="#298FFC",font=("Verdana",11)) 
    textoFijo2.grid(row=3, column=1,columnspan=2)

    CréditosCur.grid(row=3,column=2,columnspan=2,pady=10,ipadx=10)

    textoFijo3.config(background="#298FFC",font=("Verdana",11)) 
    textoFijo3.grid(row=4, column=1,columnspan=2)

    CréditosPen.grid(row=4,column=2,columnspan=2,pady=10,ipadx=10)

    textoFijo4.config(background="#298FFC",font=("Verdana",11)) 
    textoFijo4.grid(row=6, column=1,columnspan=3)

    CréditosSemestreO.grid(row=6,column=4,columnspan=1,pady=10,ipadx=10)

    textoFijoT.config(background="#298FFC",font=("Verdana",11)) 
    textoFijoT.grid(row=7, column=2,columnspan=2)

    TCreditosO.config(bg="#FC9F29",fg="#6A4201",width=5)
    TCreditosO.insert(0, 'No.')
    TCreditosO.grid(row=7, column=3,columnspan=2,pady=10)

    BotonO.grid(row=7, column=4,columnspan=3,padx=0,pady=5)
    BotonO.config(width=14)

    textoFijo5.config(background="#298FFC",font=("Verdana",11)) 
    textoFijo5.grid(row=9, column=1,columnspan=2)

    CréditosSemestre1.grid(row=9,column=3,columnspan=1,pady=10,ipadx=30)
    CréditosSemestre1.config(width=10)

    CréditosSemestre2.grid(row=10,column=3,columnspan=1,pady=10,ipadx=30)
    CréditosSemestre2.config(width=10)

    CréditosSemestre3.grid(row=11,column=3,columnspan=1,pady=10,ipadx=30)
    CréditosSemestre3.config(width=10)

    textoFijoS.config(background="#298FFC",font=("Verdana",11)) 
    textoFijoS.grid(row=12, column=2,columnspan=2)

    TCreditos.config(bg="#FC9F29",fg="#6A4201",width=5)
    TCreditos.insert(0, 'No.')
    TCreditos.grid(row=12, column=3,columnspan=2,pady=10)

    BotonS.grid(row=12, column=4,columnspan=2,padx=0,pady=5)
    BotonS.config(width=14)

    BotonRegresar.grid(row=13, column=8,columnspan=3,padx=4,pady=5,ipady=0)
    BotonRegresar.config(width=10)