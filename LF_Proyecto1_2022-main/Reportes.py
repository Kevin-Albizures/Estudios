from errores import error_L
from estilo import conjuntos

def report(text__, problemas,resultados):
    def reporteError():
        global error_L
        texto=""
        texto+="<HTML>\n" 
        texto+="    <title> Reporte Error </title>\n" 
        
        texto+="    <font size=+2>\n"  
        texto+="        <font face=\"Times New Roman\">\n"
        texto+="            <font color=orange>\n"
        texto+="    <body style=\"background-color:#002D45\">\n"
        texto+="                <h1 align=center> REPORTE DE ERRORES </h1>\n"
        texto+="            </font>\n" 
        texto+="        </font>\n"
        texto+="    </font>\n"
        texto+="    <font color=white>\n"
        texto+="        <h1 align=center>  </h1>\n" 
        texto+="    </font>\n"
        texto+="    <font size=+2>\n"
        texto+="        <table border=1 align=center TR BGCOLOR=\"#1A5760\" TABLE BORDERCOLOR=\"Black\">\n" 
        texto+="            <thead>\n" 
        texto+="                <tr>\n" 
        texto+="                    <th>No.</th>\n" 
        texto+="                    <th>Lexema</th>\n" 
        texto+="                    <th>Tipo</th>\n"   
        texto+="                    <th>Fila</th>\n"
        texto+="                    <th>Columna</th>\n"   
        texto+="                </tr>\n"
        texto+="            </thead>\n"
        texto+="            <tbody>\n"
        if len(error_L)==0:
            texto+="    <font color=white>\n"
            texto+="        <h1 align=center> NO SE ENCONTRARON ERRORES B) </h1>\n" 
            texto+="    </font>\n"
        else:
            texto+="    <font color=white>\n"
            texto+="        <h1 align=center> OH NO, SE ENCONTRARON ERRORES B( </h1>\n" 
            texto+="    </font>\n"
            for j in range(0,len(error_L)): 
                texto+="            <tr>\n" 
                texto+="                <td>\n"+str(j+1)+"</td>\n"
                texto+="                <td>\n"+str(error_L[j]["Lexema"])+"</td>\n"
                texto+="                <td>\n"+str(error_L[j]["Tipo"])+"</td>\n"
                texto+="                <td>\n"+str(error_L[j]["Fila"])+"</td>\n"
                texto+="                <td>\n"+str(error_L[j]["Columna"])+"</td>\n"
                texto+="            </tr>\n"
        texto+="            </tbody>\n"    
        texto+="        </table>\n"
        texto+="    </font>\n"
        texto+="    </body>\n"
        texto+="</HTML>\n"
        return texto

    def reporteRESULTADO(text_, problemas,resultados):
        texto=""
        texto+="<HTML>\n" 
        texto+="    <title> Reporte de RESULTADOS </title>\n" 
        
        texto+="    <font size=+2>\n" 
        texto+="        <font face=\"Terminal\">\n" 
        texto+="            <font size="+str(conjuntos[0]["Tamaño"])+" color="+conjuntos[0]["Color"]+">\n" 
        texto+="    <body style=\"background-color:#002D45\">\n" 
        texto+="                <h1 align=center>RESULTADOS DE OPERACIONES</h1>\n" 
        texto+="            </font>\n" 
        texto+="        </font>\n"
        texto+="    </font>\n"
        texto+="    <font color=orange size=5>"
        texto+="    <h1 align=center>Descripcion:</h1></font>\n"
        texto+="    <font size="+str(conjuntos[2]["Tamaño"])+" color="+conjuntos[2]["Color"]+">\n" 
        texto+="        <p align=center>" +str(text_)+"</p>\n" 
        texto+="    </font>\n"
        texto+="    <font size=+2>\n" 
        texto+="        <table border=1 align=center width=1000 height=600 TR BGCOLOR= \"#FFFFF\" TABLE BORDERCOLOR=black>\n" 
        texto+="            <thead>\n"
        texto+="                <tr>\n" 
        texto+="                    <th>Operacion No.</th>\n"
        texto+="                    <th>Gramatica</th>\n" 
        texto+="                    <th>Resultado</th>\n"                 
        texto+="                </tr>\n"
        texto+="            </thead>\n"
        texto+="            <tbody>\n"
        
        j=1
        for i in range(0,len(problemas)-3):
            texto+="            <tr>\n" 
            texto+="                <td align=center>\n"
            texto+="    <font size="+str(conjuntos[4]["Tamaño"])+" color="+conjuntos[4]["Color"]+"><b>"+str(i+1)+"</b></font></td>\n"
            texto+="                <td align=center>\n"
            texto+="    <font size="+str(conjuntos[4]["Tamaño"])+" color="+conjuntos[4]["Color"]+"><b>"+str(problemas[i])+"</b></font></td>\n"
            texto+="                <td align=center>\n"
            texto+="    <font size="+str(conjuntos[4]["Tamaño"])+" color="+conjuntos[4]["Color"]+"><b>"+str(resultados[i])+"</b></font></td>\n"                
            texto+="            </tr>\n"
            
        texto+="            </tbody>\n"    
        texto+="        </table>\n"
        texto+="    </font>\n"
        texto+="    </body>\n"
        texto+="</HTML>\n"
        return texto

    Temp=open("Errores_202006681.html","w", encoding="utf-8") 
    Contenido=reporteError()
    Temp.write(Contenido)
    Temp.close
    print("Reporte de errores generado")

    Temp=open("RESULTADOS_202006681.html","w", encoding="utf-8") 
    Contenido=reporteRESULTADO(text__, problemas,resultados)
    Temp.write(Contenido)
    Temp.close
    print("Reporte de resultados generado")
    