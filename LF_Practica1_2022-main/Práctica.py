from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter.messagebox
from Cargar import lista, seleccionar, diseñoCargar
import ListarCurso
import AgregarCurso
import EditarCurso
import ConteoCréditos
import EliminarCurso
import GestionarCursos

if __name__=='__main__':
    ## Condición para que no se cierre la ventana principal
    salida= 1

    while salida==1:
    ## ------------------------------------- 1. Ventana Cargar Archivo ----------------------------------------
        def ventanaCargar():
            Ventana.withdraw()

            def pasarRuta():
                try:
                    ## Comando para abrir el explorador de archivos
                    filename=filedialog.askopenfilename(title="Buscar")
                    textmod2=filename

                    ## Etiqueta de la ruta a mostrar
                    etiquetaRuta2 =Label(FondoVentana2, text=textmod2)
                    etiquetaRuta2.config(bg="#F6DDCC",fg="#6A4201") 
                    etiquetaRuta2.grid(row=2, column=2,columnspan=9)
                    
                    ## Llama la función de la pestaña CARGAR
                    seleccionar(str(filename))
                except IndexError:
                    tkinter.messagebox.showinfo("Ruta inválida",  "Ingrese una ruta lfp")
                except FileNotFoundError:
                    print("Proceso cancelado")
                
            def Regresar1():
                VentanaC.destroy()
                Ventana.deiconify()

            ## Ventana de Carga
            VentanaC=Toplevel()
            ## Frame de la ventana donde van los demás widgets
            FondoVentana2=Frame(VentanaC,bg="#298FFC")
            ## Texto que dice "Ruta"
            text1 =ttk.Label(FondoVentana2, text="Ruta:")
            ## Etiqueta que muestra la dirección del archivo
            etiquetaRuta =Label(FondoVentana2, text="Ruta vacía")
            ## Frame que realiza un salto de fila
            MarcoVentana2=Frame(FondoVentana2)
            ## Botón de buscar ruta
            BotonCarga=ttk.Button(FondoVentana2,text="Seleccionar",command=pasarRuta)
            ## Botón de regresar
            BotonRegresar=ttk.Button(FondoVentana2,text="Regresar",command=Regresar1)

            diseñoCargar(VentanaC,FondoVentana2,text1,etiquetaRuta,MarcoVentana2,BotonCarga,BotonRegresar)
            VentanaC.mainloop()
            
    ## ---------------------------------- 2. Ventana Gestionar Archivo -------------------------------------------
        def ventanaGestionar():
            Ventana.withdraw()

            def Regresar2():
                VentanaG.destroy()
                Ventana.deiconify()
            
            ## Listar Cursos
            def mostrarVentana1():
                ListarCurso.gestionarLista()
            
            ## Agregar Cursos
            def mostrarVentana2():
                VentanaG.withdraw()

                def actualizar():
                    vGestionar.destroy()
                    mostrarVentana2()

                def regresar():
                    vGestionar.destroy()
                    VentanaG.deiconify()
                
                def Agregar(Código,Nombre,Prerrequisito,Opcionalidad,Semestre,Créditos,Estado):
                    AgregarCurso.Agregar(Código,Nombre,Prerrequisito,Opcionalidad,Semestre,Créditos,Estado)
                    if AgregarCurso.condiciónAgregar==1:
                        actualizar()

            ## ---------------------------- Funciones de eventos -------------------------------------

                def on_entry_click(event):
                    if TCódigo.cget('fg') == "#6A4201":
                        TCódigo.delete(0, "end") 
                        TCódigo.insert(0, '') 
                        TCódigo.config(fg = 'black')
                
                def on_focusout(event):
                    if TCódigo.get() == '':
                        TCódigo.insert(0, '0000')
                        TCódigo.config(fg = "#6A4201")
                
                def on_entry_clickN(event):
                    if TNombre.cget('fg') == "#6A4201":
                        TNombre.delete(0, "end") 
                        TNombre.insert(0, '') 
                        TNombre.config(fg = 'black')
                
                def on_focusoutN(event):
                    if TNombre.get() == '':
                        TNombre.insert(0, "Nombre del Curso")
                        TNombre.config(fg = "#6A4201")
                
                def on_entry_clickP(event):
                    if TPrerrequisito.cget('fg') == "#6A4201":
                        TPrerrequisito.delete(0, "end") 
                        TPrerrequisito.insert(0, '') 
                        TPrerrequisito.config(fg = 'black')
                
                def on_focusoutP(event):
                    if TPrerrequisito.get() == '':
                        TPrerrequisito.insert(0, 'Ninguno ó 0000;0000;0000...')
                        TPrerrequisito.config(fg = "#6A4201")
                
                def on_entry_clickT(event):
                    if TOpcionalidad.cget('fg') == "#6A4201":
                        TOpcionalidad.delete(0, "end") 
                        TOpcionalidad.insert(0, '') 
                        TOpcionalidad.config(fg = 'black')
                
                def on_focusoutT(event):
                    if TOpcionalidad.get() == '':
                        TOpcionalidad.insert(0, 'Obligatorio/Opcional')
                        TOpcionalidad.config(fg = "#6A4201")

                def on_entry_clickS(event):
                    if TSemestre.cget('fg') == "#6A4201":
                        TSemestre.delete(0, "end") 
                        TSemestre.insert(0, '') 
                        TSemestre.config(fg = 'black')
                
                def on_focusoutS(event):
                    if TSemestre.get() == '':
                        TSemestre.insert(0, 'No.')
                        TSemestre.config(fg = "#6A4201")
                
                def on_entry_clickC(event):
                    if TCréditos.cget('fg') == "#6A4201":
                        TCréditos.delete(0, "end") 
                        TCréditos.insert(0, '') 
                        TCréditos.config(fg = 'black')
                
                def on_focusoutC(event):
                    if TCréditos.get() == '':
                        TCréditos.insert(0, 'No.')
                        TCréditos.config(fg = "#6A4201")

                def on_entry_clickE(event):
                    if TEstado.cget('fg') == "#6A4201":
                        TEstado.delete(0, "end") 
                        TEstado.insert(0, '') 
                        TEstado.config(fg = 'black')
                
                def on_focusoutE(event):
                    if TEstado.get() == '':
                        TEstado.insert(0, 'Aprobado/Cursando/Pendiente')
                        TEstado.config(fg = "#6A4201")

            ## ----------------------------------------- Ventana y Labels con los datos a pedir --------------------------------------
                ## Creación de Ventana Secundaria
                vGestionar = Toplevel()
                ## Frame que realiza un salto de fila
                Marco=Frame(vGestionar)
                Código=Label(vGestionar, text="Código: ")
                Nombre=Label(vGestionar, text="Nombre: ")
                Prerrequisito=Label(vGestionar, text="Prerrequisito: ")
                Opcionalidad=Label(vGestionar, text="Opcionalidad: ")
                Semestre=Label(vGestionar, text="Semestre: ")
                Créditos=Label(vGestionar, text="Créditos: ")
                Estado=Label(vGestionar, text="Estado: ")
                Marco2=Frame(vGestionar)
                ## Función de diseño labels
                AgregarCurso.valoresLabelsA(vGestionar,Marco,Código,Nombre,Prerrequisito,Opcionalidad,Semestre,Créditos,Estado,Marco2)

            ## ------------------------------------------ Entrys para recibir la información -------------------------------------------------

                TCódigo=Entry(vGestionar)
                TCódigo.bind('<FocusIn>', on_entry_click)
                TCódigo.bind('<FocusOut>', on_focusout)

                TNombre=Entry(vGestionar)
                TNombre.bind('<FocusIn>', on_entry_clickN)
                TNombre.bind('<FocusOut>', on_focusoutN)
                
                TPrerrequisito=Entry(vGestionar)
                TPrerrequisito.bind('<FocusIn>', on_entry_clickP)
                TPrerrequisito.bind('<FocusOut>', on_focusoutP) 
                
                TOpcionalidad=Entry(vGestionar)
                TOpcionalidad.bind('<FocusIn>', on_entry_clickT)
                TOpcionalidad.bind('<FocusOut>', on_focusoutT) 
                
                TSemestre=Entry(vGestionar)
                TSemestre.bind('<FocusIn>', on_entry_clickS)
                TSemestre.bind('<FocusOut>', on_focusoutS) 
                
                TCréditos=Entry(vGestionar)
                TCréditos.bind('<FocusIn>', on_entry_clickC)
                TCréditos.bind('<FocusOut>', on_focusoutC)
                
                TEstado=Entry(vGestionar)
                TEstado.bind('<FocusIn>', on_entry_clickE)
                TEstado.bind('<FocusOut>', on_focusoutE) 
                
                ## Botón de Agregar
                TBotonAgregar=ttk.Button(vGestionar,text="Agregar",command=lambda : Agregar(TCódigo.get(),TNombre.get(),TPrerrequisito.get(),TOpcionalidad.get(),TSemestre.get(),TCréditos.get(),TEstado.get()))
                ## Botón de regresar
                TBotonRegresar=ttk.Button(vGestionar,text="Regresar",command=regresar)

                ## Función de diseño
                AgregarCurso.valoresEntrysA(TCódigo,TNombre,TPrerrequisito,TOpcionalidad,TSemestre,TCréditos,TEstado,TBotonAgregar,TBotonRegresar)
                vGestionar.mainloop()
            
            ## Editar Cursos
            def mostrarVentana3():
                VentanaG.withdraw()

                def regresar():
                    vGestionar.destroy()
                    VentanaG.deiconify()
            ## ------------------------------------------- Ventana de Edición -------------------------------------------------
                def Editar(Código,j):
                    vGestionar.withdraw()

                    def regresar2():
                        vGestionar.deiconify()
                        vEdición.destroy()
                    
                    def TEditar(j,Nombre,Prerrequisito,Opcionalidad,Semestre,Créditos,Estado):
                        EditarCurso.gestionarEditar(j,Nombre,Prerrequisito,Opcionalidad,Semestre,Créditos,Estado)
                            
                        if EditarCurso.condición3==1:
                            vGestionar.destroy()
                            vEdición.destroy()
                            VentanaG.deiconify()     
                ## ---------------------------- Funciones de eventos -------------------------------------
                    def on_entry_clickN(event):
                        if TNombre.cget('fg') == "#6A4201":
                            TNombre.delete(0, "end") 
                            TNombre.insert(0, '') 
                            TNombre.config(fg = 'black')
                    
                    def on_focusoutN(event):
                        if TNombre.get() == '':
                            TNombre.insert(0, lista[j]["Nombre"])
                            TNombre.config(fg = "#6A4201")
                    
                    def on_entry_clickP(event):
                        if TPrerrequisito.cget('fg') == "#6A4201":
                            TPrerrequisito.delete(0, "end") 
                            TPrerrequisito.insert(0, '') 
                            TPrerrequisito.config(fg = 'black')
                    
                    def on_focusoutP(event):
                        if TPrerrequisito.get() == '':
                            TPrerrequisito.insert(0, lista[j]["Prerrequisito"])
                            TPrerrequisito.config(fg = "#6A4201")
                    
                    def on_entry_clickT(event):
                        if TOpcionalidad.cget('fg') == "#6A4201":
                            TOpcionalidad.delete(0, "end") 
                            TOpcionalidad.insert(0, '') 
                            TOpcionalidad.config(fg = 'black')
                    
                    def on_focusoutT(event):
                        if TOpcionalidad.get() == '':
                            TOpcionalidad.insert(0, lista[j]["Opcionalidad"])
                            TOpcionalidad.config(fg = "#6A4201")

                    def on_entry_clickS(event):
                        if TSemestre.cget('fg') == "#6A4201":
                            TSemestre.delete(0, "end") 
                            TSemestre.insert(0, '') 
                            TSemestre.config(fg = 'black')
                    
                    def on_focusoutS(event):
                        if TSemestre.get() == '':
                            TSemestre.insert(0, lista[j]["Semestre"])
                            TSemestre.config(fg = "#6A4201")
                    
                    def on_entry_clickC(event):
                        if TCréditos.cget('fg') == "#6A4201":
                            TCréditos.delete(0, "end") 
                            TCréditos.insert(0, '') 
                            TCréditos.config(fg = 'black')
                    
                    def on_focusoutC(event):
                        if TCréditos.get() == '':
                            TCréditos.insert(0, lista[j]["Créditos"])
                            TCréditos.config(fg = "#6A4201")

                    def on_entry_clickE(event):
                        if TEstado.cget('fg') == "#6A4201":
                            TEstado.delete(0, "end") 
                            TEstado.insert(0, '') 
                            TEstado.config(fg = 'black')
                    
                    def on_focusoutE(event):
                        if TEstado.get() == '':
                            TEstado.insert(0, lista[j]["Estado"])
                            TEstado.config(fg = "#6A4201")

                    ## Creación de Ventana Secundaria
                    vEdición = Toplevel()
                ## ----------------------------------------- Labels con los datos a pedir --------------------------------------
                    ## Frame que realiza un salto de fila
                    Marco=Frame(vEdición)
                    Código=Label(vEdición, text="Código:"+Código)
                    Nombre=Label(vEdición, text="Nombre: ")
                    Prerrequisito=Label(vEdición, text="Prerrequisito: ")
                    Opcionalidad=Label(vEdición, text="Opcionalidad: ")
                    Semestre=Label(vEdición, text="Semestre: ")
                    Créditos=Label(vEdición, text="Créditos: ")
                    Estado=Label(vEdición, text="Estado: ")
                    Marco2=Frame(vEdición)

                    EditarCurso.valoresLabelsE(vEdición,Marco,Código,Nombre,Prerrequisito,Opcionalidad,Semestre,Créditos,Estado,Marco2)

                ## ------------------------------------------ Entrys para recibir la información -------------------------------------------------

                    TNombre=Entry(vEdición)
                    TNombre.bind('<FocusIn>', on_entry_clickN)
                    TNombre.bind('<FocusOut>', on_focusoutN)
                    
                    TPrerrequisito=Entry(vEdición)
                    TPrerrequisito.bind('<FocusIn>', on_entry_clickP)
                    TPrerrequisito.bind('<FocusOut>', on_focusoutP)     
                    
                    TOpcionalidad=Entry(vEdición)
                    TOpcionalidad.bind('<FocusIn>', on_entry_clickT)
                    TOpcionalidad.bind('<FocusOut>', on_focusoutT) 
                    
                    TSemestre=Entry(vEdición)
                    TSemestre.bind('<FocusIn>', on_entry_clickS)
                    TSemestre.bind('<FocusOut>', on_focusoutS) 

                    TCréditos=Entry(vEdición)
                    TCréditos.bind('<FocusIn>', on_entry_clickC)
                    TCréditos.bind('<FocusOut>', on_focusoutC)
                    
                    TEstado=Entry(vEdición)
                    TEstado.bind('<FocusIn>', on_entry_clickE)
                    TEstado.bind('<FocusOut>', on_focusoutE) 

                    ## Botón de Editar
                    TBotonAgregar=ttk.Button(vEdición,text="Editar",command=lambda : TEditar(j,TNombre.get(),TPrerrequisito.get(),TOpcionalidad.get(),TSemestre.get(),TCréditos.get(),TEstado.get()))
                    ## Botón de regresar
                    TBotonRegresar=ttk.Button(vEdición,text="Salir",command=regresar2)

                    EditarCurso.valoresEntrysE(j,TNombre,TPrerrequisito,TOpcionalidad,TSemestre,TCréditos,TEstado,TBotonAgregar,TBotonRegresar)

            ## -------------------------------------------- Buscar el curso ----------------------------------------------------
                def buscar(Código):
                    EditarCurso.buscarEditar(Código)
                    if EditarCurso.Condición==0:
                        Editar(Código,EditarCurso.condiciónEditar)
            ## ----------------------------------------------- Funciones de Eventos ---------------------------------------------------
                def on_entry_click(event):
                    if TCódigo.cget('fg') == "#6A4201":
                        TCódigo.delete(0, "end") 
                        TCódigo.insert(0, '') 
                        TCódigo.config(fg = 'black')
                
                def on_focusout(event):
                    if TCódigo.get() == '':
                        TCódigo.insert(0, 'Código completo del curso a editar')
                        TCódigo.config(fg = "#6A4201")
            ## ----------------------------------------------------- Ventana Secundaria -------------------------------------------------------
                ## Creación de Ventana Secundaria
                vGestionar = Toplevel()
                ## Frame para decorar
                Marco=Frame(vGestionar)
                ## Label de Código
                Código=Label(vGestionar, text="Código: ")
                ## Entrada del Código
                TCódigo=Entry(vGestionar)
                TCódigo.bind('<FocusIn>', on_entry_click)
                TCódigo.bind('<FocusOut>', on_focusout)
                ## Frame de salto de fila
                Marco2=Frame(vGestionar)
                ## Botón de Buscar
                TBotonAgregar=ttk.Button(vGestionar,text="Buscar",command=lambda : buscar(TCódigo.get()))
                ## Botón de regresar
                TBotonRegresar=ttk.Button(vGestionar,text="Regresar",command=regresar)
                ## Frame de decoración
                Marco3=Frame(vGestionar)

                EditarCurso.valoresBusqueda(vGestionar,Marco,Código,TCódigo,Marco2,TBotonAgregar,TBotonRegresar,Marco3)
            
            ## Eliminar Cursos
            def mostrarVentana4():
                VentanaG.withdraw()
                def regresar():
                    vGestionar.destroy()
                    VentanaG.deiconify()

            ## ------------------------------------------- Ventana de Eliminación -------------------------------------------------
                def Eliminar(j):
                    lista.pop(j)
                    vGestionar.destroy()
                    VentanaG.deiconify()
                    tkinter.messagebox.showinfo("Curso Eliminado",  "Se eliminó correctamente el curso.")

                ## Buscar el curso
                def buscar(Código):
                    EliminarCurso.buscarEliminar(Código)
                    if EliminarCurso.CondiciónE1==0:
                        Eliminar(EliminarCurso.condiciónEliminar)

            ## ----------------------------------------------- Funciones de Eventos ---------------------------------------------------
                def on_entry_click(event):
                    if TCódigo.cget('fg') == "#6A4201":
                        TCódigo.delete(0, "end") 
                        TCódigo.insert(0, '') 
                        TCódigo.config(fg = 'black')
                
                def on_focusout(event):
                    if TCódigo.get() == '':
                        TCódigo.insert(0, 'Código completo del curso a eliminar')
                        TCódigo.config(fg = "#6A4201")

            ## ----------------------------------------------------- Ventana Eliminar -------------------------------------------------------
                ## Creación de ventana
                vGestionar = Toplevel()
                ## Frame para decorar
                Marco=Frame(vGestionar)
                ## Label de Código
                Código=Label(vGestionar, text="Código: ")
                ## Entrada del Código
                TCódigo=Entry(vGestionar)
                TCódigo.bind('<FocusIn>', on_entry_click)
                TCódigo.bind('<FocusOut>', on_focusout)
                ## Frame de salto de fila
                Marco2=Frame(vGestionar)
                ## Botón de Buscar
                TBotonAgregar=ttk.Button(vGestionar,text="Eliminar",command=lambda : buscar(TCódigo.get()))
                ## Botón de regresar
                TBotonRegresar=ttk.Button(vGestionar,text="Regresar",command=regresar)
                ## Frame de decoración
                Marco3=Frame(vGestionar)
                EliminarCurso.valoresEliminar(vGestionar,Marco,Código,TCódigo,Marco2,TBotonAgregar,TBotonRegresar,Marco3)
        
        ### ----------------------------------------- Diseño de ventana gestionar --------------------------------------
            ## Ventana de Carga
            VentanaG=Toplevel()
            ## Frame de la ventana para posicionar los widgets
            FondoVentana3=Frame(VentanaG,bg="#6A4201")
            ## Botón Listar Cursos
            BotonListar=ttk.Button(VentanaG,text="Listar Cursos",command=mostrarVentana1)
            ## Botón de Agregar Cursos
            BotonAgregar=ttk.Button(VentanaG,text="Agregar Curso",command=mostrarVentana2)
            ## Botón de Editar Curso
            BotonEditar=ttk.Button(VentanaG,text="Editar Curso",command=mostrarVentana3)
            
            ## Botón de Eliminar Curso
            BotonEliminar=ttk.Button(VentanaG,text="Eliminar Curso",command=mostrarVentana4)
            ## Botón de regresar
            BotonRegresar=ttk.Button(VentanaG,text="Regresar",command=Regresar2)
            ## Frame de la ventana para posicionar los widgets
            FondoVentana4=Frame(VentanaG,bg="#6A4201")

            ## Función de diseño
            GestionarCursos.valoresGestionar(VentanaG,FondoVentana3,BotonListar,BotonAgregar,BotonEditar,BotonEliminar,BotonRegresar,FondoVentana4)

    ## ---------------------------------- 3. Ventana Conteo de Créditos -------------------------------------------
        def ventanaConteo():
            Ventana.withdraw()

            ## Funciones de conteo inicial
            ConteoCréditos.sumasCréditos()

            def Regresar3():
                vConteo.destroy()
                Ventana.deiconify()

            def CréditosO(N):
                Obligatorios=0
                if  N.isnumeric():
                    Conteo3=0
                    for i in range(0,int(N)+1):
                        j=0
                        for j in range(0,len(lista)):
                            if lista[j]["Semestre"]==str(i) and lista[j]["Opcionalidad"]=="Obligatorio":
                                Obligatorios+=int(lista[j]["Créditos"])
                                Conteo3=1
                    if Conteo3==1:
                        TextoSemestreO.set(str(Obligatorios))
                    else:
                        tkinter.messagebox.showinfo("Semestre no econtrado",  "No se encontró el semestre solicitado")
                else:
                    tkinter.messagebox.showinfo("Valor inválido",  "Ingresar un valor numérico por favor")

            def CréditosS(N):
                Ap=0
                Cur=0
                Pen=0
                if  N.isnumeric():
                    conteo3=0
                    for j in range(0,len(lista)):
                        if lista[j]["Estado"]=="Aprobado" and lista[j]["Semestre"]==N:
                            Ap+=int(lista[j]["Créditos"])
                            conteo3=1
                        elif lista[j]["Estado"]=="Cursando" and lista[j]["Semestre"]==N:
                            Cur+=int(lista[j]["Créditos"])
                            conteo3=1
                        elif lista[j]["Estado"]=="Pendiente" and lista[j]["Semestre"]==N:
                            Pen+=int(lista[j]["Créditos"])
                            conteo3=1

                    if conteo3==1:
                        TextoSemestreAp.set("Aprobados: "+str(Ap))
                        TextoSemestreCur.set("Asignados: "+str(Cur))
                        TextoSemestrePen.set("Pendientes: "+str(Pen))
                    else:
                        tkinter.messagebox.showinfo("Semestre no econtrado",  "No se encontró el semestre solicitado")
                else:
                    tkinter.messagebox.showinfo("Valor inválido",  "Ingresar un valor numérico por favor")


            ## ------------------------ Funciones de eventos -----------------------------------
            def on_entry_clickO(event):
                if TCreditosO.cget('fg') == "#6A4201":
                    TCreditosO.delete(0, "end") 
                    TCreditosO.insert(0, '') 
                    TCreditosO.config(fg = 'black',width=5)
        
            def on_focusoutO(event):
                if TCreditosO.get() == '':
                    TCreditosO.insert(0, 'No.')
                    TCreditosO.config(fg = "#6A4201",width=5)
            
            def on_entry_clickS(event):
                if TCreditos.cget('fg') == "#6A4201":
                    TCreditos.delete(0, "end") 
                    TCreditos.insert(0, '') 
                    TCreditos.config(fg = 'black',width=5)
        
            def on_focusoutS(event):
                if TCreditos.get() == '':
                    TCreditos.insert(0, 'No.')
                    TCreditos.config(fg = "#6A4201",width=5)
            
            ## Textos dinámicos a utilizar
            TextoAprobado=StringVar()
            TextoCursando=StringVar()
            TextoPendiente=StringVar()
            TextoSemestreO=StringVar()
            TextoSemestreAp=StringVar()
            TextoSemestreCur=StringVar()
            TextoSemestrePen=StringVar()
            
            TextoAprobado.set(ConteoCréditos.Suma1)
            TextoCursando.set(ConteoCréditos.Suma2)
            TextoPendiente.set(ConteoCréditos.Suma3)
            TextoSemestreO.set("0")

            TextoSemestreAp.set("Aprobados: xx")
            TextoSemestreCur.set("Asignados: xx  ")
            TextoSemestrePen.set("Pendientes: xx")
            
            ## Creación de ventana de conteo
            vConteo=Toplevel()
            ## Frame base
            frame=Frame(vConteo,bg="#298FFC")
            ## Frame que realiza una decoración
            Marco=Frame(frame)
            ## Frame que realiza una decoración
            Marco2=Frame(frame)
            ## Frame que realiza una decoración
            Marco3=Frame(frame)
            ## Frame que realiza un salto de columna al inicio
            Marco1=Frame(frame)
            ## Texto 1
            textoFijo1=ttk.Label(frame, text="Créditos Aprobados: ")
            CréditosAp=Label(frame,textvariable=TextoAprobado,bg="#FC9F29")
            ## Texto 2
            textoFijo2=ttk.Label(frame, text="Créditos Asignados: ")
            CréditosCur=Label(frame,textvariable=TextoCursando,bg="#FC9F29")
            ## Texto 3
            textoFijo3=ttk.Label(frame, text="Créditos Pendientes: ")
            CréditosPen=Label(frame,textvariable=TextoPendiente,bg="#FC9F29")
            ## Texto 4
            textoFijo4=ttk.Label(frame, text="Créditos obligatorios hasta semestre N:")
            CréditosSemestreO=Label(frame,textvariable=TextoSemestreO,bg="#FC9F29")
            ## Primera función con botón
            textoFijoT=ttk.Label(frame, text="Semestre ")
            TCreditosO=Entry(frame)
            TCreditosO.bind('<FocusIn>', on_entry_clickO)
            TCreditosO.bind('<FocusOut>', on_focusoutO) 
            ## Botón 1
            BotonO=ttk.Button(frame,text="Contar",command=lambda:CréditosO(TCreditosO.get()))
            ## Texto 5
            textoFijo5=ttk.Label(frame, text="Créditos por semestre:")
            CréditosSemestre1=Label(frame,textvariable=TextoSemestreAp,bg="#FC9F29")
            CréditosSemestre2=Label(frame,textvariable=TextoSemestreCur,bg="#FC9F29")
            CréditosSemestre3=Label(frame,textvariable=TextoSemestrePen,bg="#FC9F29")
            ## Segunda función con botón
            textoFijoS=ttk.Label(frame, text="Semestre ")
            TCreditos=Entry(frame)
            TCreditos.bind('<FocusIn>', on_entry_clickS)
            TCreditos.bind('<FocusOut>', on_focusoutS) 
            ## Botón 2
            BotonS=ttk.Button(frame,text="Contar",command=lambda : CréditosS(TCreditos.get()))
            ## Botón de regresar
            BotonRegresar=ttk.Button(frame,text="Regresar",command=Regresar3)
            
            ## Función para diseño de ventana
            ConteoCréditos.valoresConteo(vConteo,frame,Marco,Marco2,Marco3,Marco1,textoFijo1,CréditosAp,textoFijo2,CréditosCur,textoFijo3,CréditosPen,textoFijo4,CréditosSemestreO,
                                        textoFijoT,TCreditosO,BotonO,textoFijo5,CréditosSemestre1,CréditosSemestre2,CréditosSemestre3,textoFijoS,TCreditos,BotonS,BotonRegresar)
    ## --------------------------------------- 4. Cerrar programa ------------------------------------------------
        def saliendo():
            ## Llama la variable global "salida" 
            global salida
            salida=0
            Ventana.destroy()

    ## ---------------------------------------- 5. Diseño ventana menú-------------------------------------------------
        ## Crea la venta principal
        Ventana = Tk(className=" Menú")
        Ventana.config(bg="#298FFC",relief="sunken")
        Ventana.resizable(False, False)
        Ventana.geometry("500x400")
        
        ## Configurar el estilo de los botones
        s = ttk.Style()
        s.configure("TButton", background="#D35400")
        s.map("TButton", background=[("active", "#85C1E9")])

        ## Frame que almacena los labels
        Marco1=Frame(Ventana)
        Marco1.grid(row=0, column=0,columnspan=5,rowspan=2,pady=10,ipady=1,padx=9)
        Marco1.config(bg="#298FFC")

        ## Label del nombre del curso
        etiqueta1 =Label(Marco1, text="Nombre del Curso: Lab. Lenguajes Formales y de Programación")
        etiqueta1.config(bg="#FC9F29",font=("Verdana",11),fg="#6A4201") 
        etiqueta1.grid(row=0, column=0,columnspan=4,sticky=E+W)

        ## Label contiene nombre del estudiante
        etiqueta2 = Label(Marco1, text="Nombre del Estudiante: Kevin Haroldo Albizures Sirín")
        etiqueta2.config(font=("Verdana",11),bg="#FC9F29",fg="#6A4201")
        etiqueta2.grid(row=1, column=0,columnspan=4,sticky=E+W)
        
        ## Label contiene carné del estudiante
        etiqueta3 =Label(Marco1, text="Carné del Estudiante: 202006681")
        etiqueta3.config(bg="#FC9F29",font=("Verdana",11),fg="#6A4201")
        etiqueta3.grid(row=2, column=0,columnspan=4,sticky=E+W)
        
        ## Frame que realiza un salto de fila
        Marco=Frame(Ventana)
        Marco.grid(row=3, column=0,columnspan=5,ipadx=50,pady=10)
        Marco.config(width=30,bg="#6A4201")

        ## Botón ejecuta la ventana de "Carga de Archivos"
        Boton1=ttk.Button(Ventana, text="Cargar Archivo", command=ventanaCargar)
        Boton1.grid(row=4, column=0,columnspan=5,pady=5,ipady=10)
        Boton1.config(width=30)
        
        ## Botón ejecuta la ventana "Gestionar Cursos" 
        Boton2=ttk.Button(Ventana, text="Gestionar Cursos", command=ventanaGestionar)
        Boton2.grid(row=5, column=0,columnspan=5,pady=5,ipady=10)
        Boton2.config(width=30)

        ## Botón ejecuta la venta de "Conteo de Créditos"
        Boton3=ttk.Button(Ventana, text="Conteo de Créditos",command=ventanaConteo)
        Boton3.grid(row=6, column=0,columnspan=5,pady=5,ipady=10)
        Boton3.config(width=30)
        
        ## Botón ejecuta la salida del programa
        Boton4=ttk.Button(Ventana, text="Salir",command=saliendo)
        Boton4.grid(row=7, column=0,columnspan=5,pady=5,ipady=10)
        Boton4.config(width=30)

        ## Frame que realiza una decoración
        Marco=Frame(Ventana)
        Marco.grid(row=8, column=0,columnspan=5,ipadx=50,pady=10)
        Marco.config(width=30,bg="#6A4201")
        
        Ventana.mainloop()