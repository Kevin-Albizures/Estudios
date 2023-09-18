import os
from CargarArchivo import CargarArchivo, nombre,m,patrones,edad,saltar,periodos
from colorama import Fore
from IteraciónPacientes import IterarPacientes
from ListasCeldas import N

SalidaMenu=1

def refrescarPantalla():
    os.system("cls")

def reporteXML2(indice):
    text=""
    for i in range(0,indice):
        text+="  <paciente>\n"
        text+="     <datospersonales>\n"
        text+="         <nombre>"+str(nombre[i])+"</nombre>\n"
        text+="         <edad>"+str(edad[i])+"</edad>\n"
        text+="     </datospersonales>\n"
        text+="     <periodos>"+str(periodos[i])+"</periodos>\n"
        text+="     <m>"+str(m[i])+"</m>\n"
        text+="     <n>"+str(N[i])+"</n>\n"
        text+="  </paciente>\n"
    return text
    
def reporteXML(indice):
    contenido="<pacientes>"
    r=open("reporte.xml","w")
    contenido+=reporteXML2(indice)
    contenido+="</pacientes>"
    r.write(contenido)
    r.close()

def MostrarRejillas():
    indice=0
    p=0
    n=0
    print("")
    for Multiplo in m:
        if saltar[n]=="si":
            n+=1
            indice+=1
        else:
            print(Fore.YELLOW+"Paciente: "+nombre[indice])
            print(Fore.YELLOW+"Edad: "+edad[indice])
            print("")
            patrones[p].recorrerInicio_Fin(Multiplo)
            indice+=1
            p+=1
            n+=1

def MenuPacientes(Pacientes,indice):
    OpPaciente="31312"
    print(Fore.LIGHTBLUE_EX+" Paciente(s): "+Pacientes)
    print( Fore.YELLOW+" ---------------------------------------------------------------")
    print("| "+Fore.LIGHTBLUE_EX+"1. Identificar enfermedad dentro de los periodos.  "+Fore.YELLOW+"           |")
    print("| "+Fore.LIGHTBLUE_EX+"2. Identificar sin periodos.                       "+Fore.YELLOW+"           |")
    print(" ---------------------------------------------------------------")
    OpPaciente=input("Escoja la opción: ")

    if OpPaciente=="1":
        IterarPacientes(Pacientes,indice)
    elif OpPaciente=="2":
        IterarPacientes(Pacientes,indice)
    else:
        print("Opción inválida")

while SalidaMenu==1:
    print(Fore.YELLOW+" --------------------- Menú ------------------- ")
    print("| "+Fore.LIGHTBLUE_EX+"1. Cargar archivo xml.              "+Fore.YELLOW+"         |")
    print("| "+Fore.LIGHTBLUE_EX+"2. Mostrar información de pacientes."+Fore.YELLOW+"         |")
    print("| "+Fore.LIGHTBLUE_EX+"3. Elegir paciente.                 "+Fore.YELLOW+"         |")
    print("| "+Fore.LIGHTBLUE_EX+"4. Generar archivo xml.             "+Fore.YELLOW+"         |")
    print("| "+Fore.LIGHTBLUE_EX+"5. Salir                            "+Fore.YELLOW+"         |")
    print(" ----------------------------------------------")
    OpMenu=input("Escoja la opción: ")

## ----------------------------------- Cargar Archivo --------------------------------------------------
    if OpMenu=="1":
        refrescarPantalla()
        CargarArchivo()
## ---------------------------------- Mostrar pacientes -------------------------------------------------        
    elif OpMenu=="2":
        refrescarPantalla()
        MostrarRejillas()
## ---------------------------------- Elegir paciente -------------------------------------------------
    elif OpMenu=="3":
        refrescarPantalla()
        SalidaMenu2=1
        while SalidaMenu2==1:
            i=1
            j=0
            print("       Seleccione el paciente")
            print("-----------------------------------------"+Fore.LIGHTBLUE_EX)
            for elem in nombre:
                if saltar[j]=="si":
                    j+=1
                else:
                    print(str(i)+". "+elem)
                    i+=1
                    j+=1
            print(str(i)+". Regresar"+Fore.YELLOW)
            print("-----------------------------------------")
            OpMenu2=input("Ingrese la opción: ")

            for vari in range(0,i):
                if OpMenu2==str(vari):
                    refrescarPantalla()
                    v=vari-1
                    MenuPacientes(nombre[vari-1],v)
                    SalidaMenu2=0
                    break
            if OpMenu2==str(i):
                SalidaMenu2=0
            refrescarPantalla()
            print(Fore.RED+"Ingrese un valor númerico dentro de las opciones"+Fore.YELLOW)
        refrescarPantalla()

##--------------------------------------------------- Generar XML --------------------------------------------
    elif OpMenu=="4":
        refrescarPantalla()
        reporteXML(len(nombre))
        print("Reporte generado")

## ---------------------------------------------------- Salida ------------------------------------------------
    elif OpMenu=="5":
        SalidaMenu=0
    else:
        refrescarPantalla()
        input(Fore.RED+"Ingrese una opción válida"+Fore.YELLOW)
        refrescarPantalla()
refrescarPantalla()
print(Fore.WHITE+"Ha salido del programa.")