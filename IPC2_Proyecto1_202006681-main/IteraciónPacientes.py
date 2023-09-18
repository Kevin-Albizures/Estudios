from CargarArchivo import patrones, Patrones2, Patrones1, periodos, m,edad,nombre
from ListasCeldas import N1, filas,columnas,valorNuevo,sanas,contagiadas,N

def IterarPacientes(Pacientes,Indice):

    for iteración in range(0,int(periodos[Indice])):
        if iteración==0:
            Patrones2[Indice].Iterar(m[Indice],Indice)
            for n in range(0,len(valorNuevo)):
                Patrones2[Indice].reemplazarItera(m[Indice],filas[n],columnas[n],valorNuevo[n])
            #Patrones2[Indice].recorrerIteracion(m[Indice])
            Patrones2[Indice].crearReporte(Pacientes,edad[Indice],str(iteración+1),m[Indice],str(sanas[Indice]),str(contagiadas[Indice]))
            if contagiadas[Indice]==0:
                N[Indice]=iteración
                break
        else:
            Patrones2[Indice].Iterar(m[Indice],Indice)
            for n in range(0,len(valorNuevo)):
                Patrones2[Indice].reemplazarItera(m[Indice],filas[n],columnas[n],valorNuevo[n])
            Patrones1[Indice].Iterar(m[Indice],Indice)
            for n in range(0,len(valorNuevo)):
                Patrones1[Indice].reemplazarItera(m[Indice],filas[n],columnas[n],valorNuevo[n])
            Patrones2[Indice].crearReporte(nombre[Indice],edad[Indice],str(iteración+1),m[Indice],str(sanas[Indice]),str(contagiadas[Indice]))
            if contagiadas[Indice]==0:
                N[Indice]=iteración
                break
    input("Información iterada.  ")
    