import webbrowser
from tkinter import filedialog
from tkinter import *
from tkinter import END
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import messagebox
from analizador_lexico import texto1

from analizador_lexico import Compile
#import re
salida=0
entrada=0
relleno=None
ruta=None
while salida==0:


    def abrirUsario():
        webbrowser.open_new_tab("Manual_Usuario_202006681.pdf")

    def abrirTecnico():
        webbrowser.open_new_tab("Manual_Técnico_202006681.pdf")
        
    def DatosPersonales():
        messagebox.showinfo(title=" Datos Personales", message="Nombre: Kevin Haroldo Albizures Sirín\nCarnet: 202006681\nCorreo: ks.panfilo@outlook.es")

    def abrirArchivo():
        global relleno, ruta
        Analizador=None
        try:
            Analizador=filedialog.askopenfilename(filetypes=[("Ficheros de texto ","*.txt")],title="Buscar")
            if len(Analizador)!=0:
                relleno=""
                ruta=Analizador
                lectura=open(Analizador, 'r')
                abc=lectura.readlines()
                for j in range(0,len(abc)):
                    abc[j].replace("\n","")
                    relleno+=abc[j]
                text_.delete("1.0",END)
                text_.insert(1.0,"")
                text_.insert(1.0,relleno)
                lectura.close()
        except IndexError:
            messagebox.showinfo("Ruta inválida",  "Ingrese una ruta .txt")
        except FileNotFoundError:
            print("Proceso cancelado")
        
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
                        r= filedialog.asksaveasfilename(title="Guardar archivo ", defaultextension=".txt",filetypes=[("Text files", "*.txt")])
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
                        messagebox.showinfo("Ruta inválida",  "Ingrese una ruta .txt")
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
                        r= filedialog.asksaveasfilename(title="Guardar archivo ", defaultextension=".txt",filetypes=[("Text files", "*.txt")])
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
                        messagebox.showinfo("Ruta inválida",  "Ingrese una ruta .txt")
                    except FileNotFoundError:
                        print("Proceso cancelado")
            else:
                try:
                    r= filedialog.asksaveasfilename(title="Guardar archivo ", defaultextension=".txt",filetypes=[("Text files", "*.txt")])
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
                    messagebox.showinfo("Ruta inválida",  "Ingrese una ruta .txt")
                except FileNotFoundError:
                    print("Proceso cancelado")
        except:
            print("No hay ruta. ")
    
    def RutaVálida():
        global ruta
        if ruta==None:
            messagebox.showinfo(title=" No hay ruta.",message="Debe crear o abrir un archivo.")
        else:
            Compile(ruta)
            webbrowser.open_new_tab("RESULTADOS_202006681.html")
            webbrowser.open_new_tab("Errores_202006681.html")

    def Salir():
        global salida
        salida=1
        Ventana.destroy()

    Ventana=Tk(className=" Menú")
    Ventana.config(bg="#002D45",relief="sunken")
    Ventana.resizable(False, False)
    #Ventana.geometry("500x400")

    Text1=Label(Ventana, text="ANALIZADOR LÉXICO",bg="#DE7104", font = ("Times New Roman", 15),relief=GROOVE)
    Text1.grid(row=0, column=0,columnspan=6,pady=10,ipady=10,padx=9,sticky=E+W)

    Marco1=Frame(Ventana)
    Marco1.grid(row=1, column=0,columnspan=1,rowspan=7,pady=10,ipady=1,padx=9)
    Marco1.config(bg="#1A5760",relief=GROOVE)

    ## Configurar el estilo de los botones
    s = ttk.Style()
    s.configure("TButton", background="#D35400")
    s.map("TButton", background=[("active", "#85C1E9")])

    MarcoOp=Label(Marco1, text=" OPCIONES ",bg="#438C97", font = ("Times New Roman", 15),fg="#FFFFFF",relief=GROOVE)
    MarcoOp.grid(row=0, column=0,columnspan=1,pady=10,ipady=1,padx=9,sticky=E+W+N+S)
    MarcoOp.config(width=15)

    text_ = scrolledtext.ScrolledText(Marco1, font = ("Times New Roman", 15),selectbackground="#174142",background="#7DC1CB",relief= SUNKEN)
    text_.grid(row=0, column=1,columnspan=1,rowspan=10,ipady=1,padx=1)

    MarcoOp=Label(Marco1, text=" AYUDA ",bg="#438C97", font = ("Times New Roman", 15),fg="#FFFFFF",relief=GROOVE)
    MarcoOp.grid(row=0, column=2,columnspan=1,pady=10,ipady=1,padx=9,sticky=E+W+N+S)
    MarcoOp.config(width=15)

    # Botón que abre un archivo
    Boton1=ttk.Button(Marco1, text="Manual De Usuario", command= lambda: abrirUsario())
    Boton1.grid(row=1, column=2,columnspan=1,pady=5,ipady=5,padx=10)
    Boton1.config(width=20)

    # Botón que abre un archivo
    Boton1=ttk.Button(Marco1, text="Manual Técnico", command= lambda: abrirTecnico())
    Boton1.grid(row=2, column=2,columnspan=1,pady=5,ipady=5,padx=10)
    Boton1.config(width=20)

    # Botón que abre un archivo
    Boton1=ttk.Button(Marco1, text="Temas De Ayuda", command= lambda: DatosPersonales())
    Boton1.grid(row=3, column=2,columnspan=1,pady=5,ipady=5,padx=10)
    Boton1.config(width=20)

    # Botón que abre un archivo
    Boton1=ttk.Button(Marco1, text="Abrir", command= lambda: abrirArchivo())
    Boton1.grid(row=1, column=0,columnspan=1,pady=5,ipady=5,padx=10)
    Boton1.config(width=20)

    ## Botón ejecuta la ventana "Gestionar Cursos" 
    Boton2=ttk.Button(Marco1, text="Guardar", command=lambda:Guardar())
    Boton2.grid(row=2, column=0,columnspan=1,pady=5,ipady=5)
    Boton2.config(width=20)

    ## Botón ejecuta la salida del programa
    Boton3=ttk.Button(Marco1, text="Guardar Como",command=lambda: GuardarComo())
    Boton3.grid(row=3, column=0,columnspan=1,pady=5,ipady=5)
    Boton3.config(width=20)

    ## Botón ejecuta la venta de "Conteo de Créditos"
    Boton4=ttk.Button(Marco1, text="Ejecutar",command=lambda : RutaVálida())
    Boton4.grid(row=4, column=0,pady=5,ipady=5)
    Boton4.config(width=20)

    ## Botón ejecuta la salida del programa
    Boton5=ttk.Button(Marco1, text="Salir", command=lambda: Salir())
    Boton5.grid(row=5, column=0,pady=5,ipady=5)
    Boton5.config(width=20)


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