import webbrowser
from tkinter import filedialog
from tkinter import *
from tkinter import END
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import font
from Analizador import Analizador
from ListaTokens import gestionarLista

"""
******: Importante
------: eventos
......: Propiedades de las pestañas
# : widgets
##: Botones
###: labels
"""
d="Fila: 0 | Columna: 0"
#import re
salida=0
entrada=0
relleno=None
ruta=None

while salida==0:
    # Pestaña de ayuda:
    def abrirUsario():
        webbrowser.open_new_tab("Manual_Usuario_202006681.pdf")

    def abrirTecnico():
        webbrowser.open_new_tab("Manual_Técnico_202006681.pdf")
        
    def DatosPersonales():
        messagebox.showinfo(title=" Datos Personales", message="Nombre: Kevin Haroldo Albizures Sirín\nCarnet: 202006681\nCorreo: ks.panfilo@outlook.es")

    # Pestaña de archivo:
    def abrirArchivo():
        global relleno, ruta
        Analizador=None
        #try:
        Analizador=filedialog.askopenfilename(filetypes=[("Ficheros de texto ","*.gpw")],title="Buscar")
        if len(Analizador)!=0:
            relleno=""
            ruta=Analizador
            lectura=open(Analizador, 'r', encoding="utf-8")
            abc=lectura.readlines()
            for j in range(0,len(abc)):
                abc[j].replace("\n","")
                relleno+=abc[j]
            text_.delete("1.0",END)
            text_.insert(1.0,"")
            text_.insert(1.0,relleno)
            lectura.close()
            compilar(ruta)
        """except IndexError:
            messagebox.showinfo("Ruta inválida",  "Ingrese una ruta .gpw")
        except FileNotFoundError:
            print("Proceso cancelado")"""
        
    def Guardar():
        try:
            global ruta, relleno
            c=text_.get("1.0",END)
            if len(c)==1:
                relleno=None
            else:
                #relleno=c
                print("nada\n")
            if ruta==None and relleno==None:
                messagebox.showinfo(title=" Sin ruta", message="No hay archivo abierto.")
            elif ruta==None and relleno!=None:
                if messagebox.askyesno(title=" Crear archivo", message="¿Desea crear un archivo nuevo?"):
                    try:
                        r= filedialog.asksaveasfilename(title="Guardar archivo ", defaultextension=".gpw",filetypes=[("Text files", "*.gpw")])
                        if r is None: 
                            return
                        if len(r)!=0:
                            contenido=text_.get("1.0",END)
                            relleno=contenido
                            ruta=r
                            Temp=open(r,"w", encoding="utf-8")
                            Temp.write(contenido)
                            Temp.close
                            messagebox.showinfo(title=" Archivo Guardado", message="Archivo guardado correctamente.")
                    except IndexError:
                        messagebox.showinfo("Ruta inválida",  "Ingrese una ruta .gpw")
                    except FileNotFoundError:
                        print("Proceso cancelado")
            else:
                contenido=text_.get("1.0",END)
                r=open(ruta,"w", encoding="utf-8")
                relleno=contenido
                r.write(contenido)
                r.close
                messagebox.showinfo(title=" Archivo Guardado", message="Archivo guardado correctamente.")
        except:
            print("No hay ruta. ")

    def GuardarComo():
        try: 
            global relleno, ruta
            c=text_.get("1.0",END)
            if len(c)==1:
                relleno=None
            else:
                relleno=c
            if ruta==None and relleno==None:
                messagebox.showinfo(title=" Sin ruta", message="No hay archivo abierto.")
            elif ruta==None and relleno!=None:
                if messagebox.askyesno(title=" Crear archivo", message="¿Desea crear un archivo nuevo?"):
                    try:
                        r= filedialog.asksaveasfilename(title="Guardar archivo ", defaultextension=".gpw",filetypes=[("Text files", "*.gpw")])
                        if r is None: 
                            return
                        if len(r)!=0:
                            contenido=text_.get("1.0",END)
                            relleno=contenido
                            ruta=r
                            Temp=open(r,"w", encoding="utf-8")
                            Temp.write(contenido)
                            Temp.close
                            messagebox.showinfo(title=" Archivo Guardado", message="Archivo guardado correctamente.")
                    except IndexError:
                        messagebox.showinfo("Ruta inválida",  "Ingrese una ruta .gpw")
                    except FileNotFoundError:
                        print("Proceso cancelado")
            else:
                try:
                    r= filedialog.asksaveasfilename(title="Guardar archivo ", defaultextension=".gpw",filetypes=[("Text files", "*.gpw")])
                    if r is None: 
                        return
                    if len(r)!=0:
                        contenido=text_.get("1.0",END)
                        relleno=contenido
                        ruta=r
                        Temp=open(r,"w", encoding="utf-8")
                        Temp.write(contenido)
                        Temp.close
                        messagebox.showinfo(title=" Archivo Guardado", message="Archivo guardado correctamente.")
                except IndexError:
                    messagebox.showinfo("Ruta inválida",  "Ingrese una ruta .gpw")
                except FileNotFoundError:
                    print("Proceso cancelado")
        except:
            print("No hay ruta. ")

    def RutaVálida():
        global ruta
        if ruta==None:
            messagebox.showinfo(title=" No hay ruta.",message="Debe crear o abrir un archivo.")
        else:
            #Compile(ruta)
            webbrowser.open_new_tab("RESULTADOS_202006681.html")
            webbrowser.open_new_tab("Errores_202006681.html")

    def Salir():
        global salida
        salida=1
        Ventana.destroy()

    def actualizarTabla(Lista):
        global tabla
        for item in tabla.get_children():
            tabla.delete(item)
        for r in range(len(Lista)-1,-1,-1):   
        #ListaError.append({"Tipo":"Error Léxico","Fila":self.linea,"Columna":(self.columna+len(recorrido)+count),"Token":token,"Descripción":"Caracter inválido."})            
            tabla.insert("",0,text=Lista[r]["Tipo"],values=(Lista[r]["Fila"],Lista[r]["Token"],Lista[r]["Descripción"]))

    def compilar(ruta):
        a = Analizador()
        listaError=a.compile(ruta)
        print(listaError)
        actualizarTabla(listaError)

    # Eventos:
    #--------- Pestaña archivos
    def Eabrir(event=None):
        abrirArchivo()
    def Eguardar(event=None):
        Guardar()
    def EguardarComo(event=None):
        GuardarComo()
    def Esalir(event=None):
        Salir()
    
    #---------- Pestaña analisis
    def Eanalisis(event=None):
        print("pendiente")
    
    #---------- Pestaña ayuda
    def Etokens(event=None):
        print("pendiente")

    #---------- Pestaña ayuda
    def EmanualUsuario(event=None):
        abrirUsario()
    def EmanualTecnico(event=None):
        abrirTecnico()
    def EdatosPersonales(event=None):
        DatosPersonales()


    # ********** Creación de ventana
    Ventana=Tk("""className=\" COMPILADOR DE PAGINAS WEB\"""")
    Ventana.geometry("1000x500+100+10")

    # ********** Barra de herramientas
    Barra=Menu()

    # ............... Archivos
    pestaña_archivo=Menu(Barra,tearoff=False,background="#1A5760",foreground="#F0E1C7")
    pestaña_archivo.add_command(label="Abrir archivo",accelerator="Ctrl+A",command=lambda: abrirArchivo(),font=font.Font(family="Times", size=10),activebackground="#438C97")
    pestaña_archivo.bind_all("<Control-a>", Eabrir)
    pestaña_archivo.add_command(label="Guardar",accelerator="Ctrl+G",command=lambda: Guardar(),font=font.Font(family="Times", size=10),activebackground="#438C97")
    pestaña_archivo.bind_all("<Control-g>", Eguardar)
    pestaña_archivo.add_command(label="Guardar cómo",accelerator="Ctrl+S",command=lambda: abrirArchivo(),font=font.Font(family="Times", size=10),activebackground="#438C97")
    pestaña_archivo.bind_all("<Control-s>", EguardarComo)
    pestaña_archivo.add_command(label="Salir",accelerator="Ctrl+W",command=lambda: Salir(),font=font.Font(family="Times", size=10),activebackground="#438C97")
    pestaña_archivo.bind_all("<Control-w>", Esalir)

    # ................ Análisis
    pestaña_analisis=Menu(Barra,tearoff=False,background="#1A5760",foreground="#F0E1C7")
    pestaña_analisis.add_command(label="Generar página web",accelerator="Ctrl+Q",command=lambda: DatosPersonales(),font=font.Font(family="Times", size=10),activebackground="#438C97")
    pestaña_analisis.bind_all("<Control-q>", Eanalisis)


    # ................ Tokens
    pestaña_Tokens=Menu(Barra,tearoff=False,background="#1A5760",foreground="#F0E1C7")
    pestaña_Tokens.add_command(label="Ver tokens",accelerator="Ctrl+T",command=lambda: DatosPersonales(),font=font.Font(family="Times", size=10),activebackground="#438C97")
    pestaña_Tokens.bind_all("<Control-t>", Etokens)

    # ................ Ayuda
    pestaña_ayuda=Menu(Barra,tearoff=False,background="#1A5760",foreground="#F0E1C7")
    pestaña_ayuda.add_command(label="Manual de usuario",accelerator="Ctrl+M",command=lambda: abrirUsario(),font=font.Font(family="Times", size=10),activebackground="#438C97")
    pestaña_ayuda.bind_all("<Control-m>", EmanualUsuario)
    pestaña_ayuda.add_command(label="Manual técnico",accelerator="Ctrl+K",command=lambda: abrirTecnico(),font=font.Font(family="Times", size=10),activebackground="#438C97")
    pestaña_ayuda.bind_all("<Control-k>", EmanualTecnico)
    pestaña_ayuda.add_command(label="Datos desarrollador",accelerator="Ctrl+L",command=lambda: DatosPersonales(),font=font.Font(family="Times", size=10),activebackground="#438C97")
    pestaña_ayuda.bind_all("<Control-l>", EdatosPersonales)

    # ********* Añadir a barra de herramientas
    Barra.add_cascade(menu=pestaña_archivo, label="Archivo")
    Barra.add_cascade(menu=pestaña_analisis, label="Análisis")
    Barra.add_cascade(menu=pestaña_Tokens, label="Tokens")
    Barra.add_cascade(menu=pestaña_ayuda, label="Ayuda")

    Ventana.config(bg="#002D45",relief="sunken",menu=Barra)
    Ventana.minsize(width=550,height=660)
    
    #Ventana.resizable(False, False)

    Ventana.grid_rowconfigure(0, weight=1)
    Ventana.grid_rowconfigure(1, weight=1)
    
    #Ventana.grid_columnconfigure(0, weight=1)
    Ventana.grid_columnconfigure(1, weight=1)

    # Contenedor de los widgets
    PrimerFrame=Frame(Ventana)
    PrimerFrame.grid(row=1, column=1,pady=10,ipady=1,padx=9,sticky=E+W+N+S)
    PrimerFrame.config(bg="#1A5760",relief=GROOVE)
    PrimerFrame.grid_rowconfigure(0, weight=1)
    PrimerFrame.grid_columnconfigure(0, weight=1)

    # Ventana/Text_
    Text1=Label(Ventana, text="COMPILADOR DE PAGINAS WEB",bg="#DE7104", font = ("Century Gothic", 15),relief=RIDGE)
    Text1.grid(row=0, column=0,columnspan=2,pady=10,ipady=5,padx=9,ipadx=500)
    Text1.config(height=2)

    # PrimerFrame/Paned1
    Paned1=PanedWindow(PrimerFrame,orient=VERTICAL,bg="#1A5760")
    Paned1.grid(row=0, column=0,ipady=1,padx=1,sticky=N+S+E+W)
    Paned1.grid_rowconfigure(0, weight=1)
    Paned1.grid_rowconfigure(2, weight=1)
    Paned1.grid_columnconfigure(0, weight=1)

    # PrimerFrame/Paned1/SegundoFrame
    SegundoFrame=Frame(Paned1,bg="#1A5760",relief=GROOVE)
    Paned1.grid(row=0, column=0,columnspan=1,rowspan=1,ipady=1,padx=1,sticky=N+S+E+W)
    SegundoFrame.grid_rowconfigure(0, weight=1)
    SegundoFrame.grid_columnconfigure(0, weight=1)

    # PrimerFrame/Paned1/SegundoFrame/TercerFrame
    TercerFrame=Frame(Ventana,bg="#1A5760",relief=RIDGE)
    TercerFrame.grid(row=1, column=0,rowspan=1,ipady=1,padx=9,pady=10,sticky=N+S+E+W)
    TercerFrame.grid_rowconfigure(0, weight=1)
    TercerFrame.grid_rowconfigure(1, weight=1)
    TercerFrame.grid_rowconfigure(2, weight=1)
    TercerFrame.grid_rowconfigure(3, weight=1)
    TercerFrame.grid_rowconfigure(4, weight=1)
    TercerFrame.grid_rowconfigure(5, weight=1)
    TercerFrame.grid_rowconfigure(6, weight=1)
    TercerFrame.grid_rowconfigure(7, weight=1)
    TercerFrame.grid_rowconfigure(8, weight=1)
    TercerFrame.grid_rowconfigure(9, weight=1)
    TercerFrame.grid_columnconfigure(0, weight=1)

    # 2.1.1.1
    ## Configurar el estilo de los botones
    s = ttk.Style()
    s.configure("TButton", background="#002D45",font = ("Century Gothic", 10))
    s.configure("Treeview",background="#1A5760",fieldbackground="#1A5760",foreground="white")
    s.map("Treeview",background=[("selected","#D35400")])
    s.map("TButton", background=[("active", "#85C1E9")])

    MarcoOp=Label(TercerFrame, text=" OPCIONES ",bg="#002D45", font = ("Century Gothic", 14),fg="#FFFFFF",relief=GROOVE)
    MarcoOp.grid(row=0, column=0,columnspan=1,pady=10,ipady=5,padx=9)
    MarcoOp.config(height=1,width=12)

    ## PrimerFrame/Paned1/SegundoFrame/TercerFrame/Boton1
    Boton4=ttk.Button(TercerFrame, text="Abrir archivo", command= lambda: abrirArchivo())
    Boton4.grid(row=1, column=0,columnspan=1,pady=5,ipady=5,padx=10)
    Boton4.config(width=13)

    ## PrimerFrame/Paned1/SegundoFrame/TercerFrame/Boton2
    Boton5=ttk.Button(TercerFrame, text="Guardar", command= lambda: Guardar())
    Boton5.grid(row=2, column=0,columnspan=1,pady=5,ipady=5,padx=10)
    Boton5.config(width=13)

    ## PrimerFrame/Paned1/SegundoFrame/TercerFrame/Boton3
    Boton6=ttk.Button(TercerFrame, text="Guardar como", command= lambda: GuardarComo())
    Boton6.grid(row=3, column=0,columnspan=1,pady=5,ipady=5,padx=10)
    Boton6.config(width=13)

    M=Label(TercerFrame, text=" COMPILAR ",bg="#002D45", font = ("Century Gothic", 14),fg="#FFFFFF",relief=GROOVE)
    M.grid(row=4, column=0,columnspan=1,rowspan=1,pady=10,ipady=5,padx=9)
    M.config(height=1,width=12)

    ## PrimerFrame/Paned1/SegundoFrame/TercerFrame/Boton1
    Boton1=ttk.Button(TercerFrame, text="Generar Página", command= lambda: compilar(ruta))
    Boton1.grid(row=5, column=0,columnspan=1,pady=5,ipady=5,padx=10)
    Boton1.config(width=13)

    M=Label(TercerFrame, text=" TOKEN ",bg="#002D45", font = ("Century Gothic", 14),fg="#FFFFFF",relief=GROOVE)
    M.grid(row=6, column=0,columnspan=1,rowspan=1,pady=10,ipady=5,padx=9)
    M.config(height=1,width=12)

    ## PrimerFrame/Paned1/SegundoFrame/TercerFrame/Boton2
    Boton2=ttk.Button(TercerFrame, text="Ver tokens", command= lambda: gestionarLista())
    Boton2.grid(row=7, column=0,columnspan=1,pady=5,ipady=5,padx=10)
    Boton2.config(width=13)

    M=Frame(TercerFrame)
    M.grid(row=8, column=0,columnspan=1,rowspan=1,pady=10,ipady=1,padx=9)
    M.config(bg="#1A5760",relief=GROOVE,height=3)

    ## PrimerFrame/Paned1/SegundoFrame/TercerFrame/Boton3
    Boton3=ttk.Button(TercerFrame, text="Salir", command= lambda: Salir())
    Boton3.grid(row=9, column=0,columnspan=1,pady=10,ipady=5,padx=10)
    Boton3.config(width=13)

    
    
    # PrimerFrame/Paned1/SegundoFrame/text_
    text_ = scrolledtext.ScrolledText(SegundoFrame, font = ("Century Gothic", 15),selectbackground="#174142",background="#7DC1CB",relief= SUNKEN)
    text_.grid(row=0, column=0,ipady=1,padx=1,sticky=N+S+E+W)
    
    def Posición():
        global d 
        v=text_.index(INSERT).split(".")
        #print("Fila: "+v[0]+" Columna: "+str(int(v[1])))
        d="Fila: "+v[0]+" | Columna: "+v[1]
        text_.after(1000,Posición)
        Mostrar=Label(SegundoFrame, text=d,anchor="e",relief=SUNKEN)
        Mostrar.grid(row=1,column=0,columnspan=1,sticky=N+S+E+W)
        Mostrar.config(height=1)

    text_.after(1000,Posición)
    # 2.2
    Mostrar=Label(SegundoFrame, text=d,font = ("Century Gothic", 10),anchor="e",relief=SUNKEN)
    Mostrar.grid(row=1,column=0,columnspan=1,sticky=N+S+E+W)
    Mostrar.config(height=1)
    

    # PrimerFrame/Paned1/tabla
    global tabla
    tabla=ttk.Treeview(Paned1,columns=[f"#{n}" for n in range (1, 4)],height=15)
    tabla.grid(row=2,column=0,columnspan=1,ipady=50,sticky=N+S)

    tabla.heading("#0",text="Tipo de error",anchor=CENTER)
    tabla.heading("#1",text="Fila")
    #tabla.heading("#2",text="Columna",anchor=CENTER)
    tabla.heading("#2",text="Token",anchor=CENTER)
    tabla.heading("#3",text="Descripción",anchor=CENTER)

    tabla.column("#0",width=80,anchor=CENTER)
    tabla.column("#1",width=60,anchor=CENTER)
    #tabla.column("#2",width=70,anchor=CENTER)
    tabla.column("#2",width=220,anchor=CENTER)
    tabla.column("#3",width=220,anchor=CENTER)

    Paned1.add(SegundoFrame)
    Paned1.add(tabla)

    # relleno del textscroll
    if entrada==0:
        text_.insert(1.0,"""
        \"Por favor ingrese un archivo\"""")
        entrada=1
    elif ruta!=None:
        text_.insert(1.0,relleno)
    else:
        text_.insert(1.0,"")

    Ventana.mainloop()