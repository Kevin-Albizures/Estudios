def reportes(ListaControles):

    def Contenedor(item2,ListaControles):
        for item in ListaControles:
            texto=""
            #print(item.ID+"=="+item2)
            if item.ID==item2:
                if item.Tipo=="Etiqueta":
                    vv=item.atributos["setTexto"].replace("\"","")
                    texto+="<label id=\""+item.ID+"\">"+vv+"</label>\n"
                elif item.Tipo=="Boton":
                    vv=item.atributos["setTexto"].replace("\"","")
                    if item.atributos["setAlineacion"]=="izquierdo" or item.atributos["setAlineacion"]=="Izquierdo":
                        vv1="LEFT"
                    elif item.atributos["setAlineacion"]=="derecho" or item.atributos["setAlineacion"]=="Derecho":
                        vv1="RIGHT"
                    elif item.atributos["setAlineacion"]=="centro" or item.atributos["setAlineacion"]=="Centro":
                        vv1="CENTER"
                    texto+="<input type=\"submit\" id=\""+item.ID+"\" value=\""+vv+"\"style=\"text-align:"+vv1+"\"/>\n"
                elif item.Tipo=="Check":
                    vv=item.atributos["setTexto"].replace("\"","")
                    texto+="<input type=\"checkbox\" id=\""+vv+"\""+item.atributos["setMarcada"]+"(checked) />"+vv+"\n"
                elif item.Tipo=="RadioBoton":
                    vv=item.atributos["setGrupo"].replace("\"","")
                    vv1=item.atributos["setTexto"].replace("\"","")
                    texto+="<input type=\"radio\" name=\""+vv+"\" id=\""+item.ID+"\""+item.atributos["setMarcada"]+"/>"+vv1+"\n"
                elif item.Tipo=="Texto":
                    vv=item.atributos["setTexto"].replace("\"","")
                    if item.atributos["setAlineacion"]=="izquierdo" or item.atributos["setAlineacion"]=="Izquierdo":
                        vv1="LEFT"
                    elif item.atributos["setAlineacion"]=="derecho" or item.atributos["setAlineacion"]=="Derecho":
                        vv1="RIGHT"
                    elif item.atributos["setAlineacion"]=="centro" or item.atributos["setAlineacion"]=="Centro":
                        vv1="CENTER"
                    texto+="<input type = \"text\" id=\""+item.ID+"\" value=\""+vv+"\"style=\"text-align:"+vv1+"\" />\n"
                elif item.Tipo=="AreaTexto":
                    texto+="<TEXTAREA id=\""+item.ID+"\">"+item.atributos["setTexto"]+"</TEXTAREA>\n"
                elif item.Tipo=="Clave":
                    vv=item.atributos["setTexto"].replace("\"","")
                    texto+="<input type = \"password\" id=\""+item.ID+"\"value=\""+vv+"\" style=\"text-align:"+item.atributos["setAlineacion"]+"\"/>\n"
                elif item.Tipo=="Contenedor":
                    texto+="<div id=\""+item.ID+"\">\n"
                    if len(item.CONTIENE)!=0:
                        for item3 in item.CONTIENE:
                            texto+=Contenedor(item3,ListaControles)
                    texto+= "</div>\n"
                return texto
    def rHTML(ListaControles):
        texto=""
        texto+="<HTML>\n" 
        texto+="<HEAD>\n"
        texto+="<meta charset=\"UTF-8\">\n"
        texto+="<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n"
        texto+="<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        texto+="<link rel=\"stylesheet\" href=\"Página.css\">"
        texto+="<title> Resultado </title>\n"
        texto+="</HEAD>\n"
        texto+="<BODY>\n"
        for item in ListaControles:
            if item.CONTENIDO=="si":
                if item.Tipo=="Etiqueta":
                    vv=item.atributos["setTexto"].replace("\"","")
                    texto+="<label id=\""+item.ID+"\">"+vv+"</label>\n"
                elif item.Tipo=="Boton":
                    texto+="<input type=\"submit\" id=\""+item.ID+"\" value=\"Texto\"style=\"text-align:"+item.atributos["setAlineacion"]+"\"/>\n"
                elif item.Tipo=="Check":
                    vv=item.atributos["setTexto"].replace("\"","")
                    texto+="<input type=\"checkbox\" id=\""+vv+"\""+item.atributos["setMarcada"]+"(checked) />"+vv+"\n"
                elif item.Tipo=="RadioBoton":
                    vv=item.atributos["setGrupo"].replace("\"","")
                    vv1=item.atributos["setTexto"].replace("\"","")
                    texto+="<input type=\"radio\" name=\""+vv+"\" id=\""+item.ID+"\""+item.atributos["setMarcada"]+"/>"+vv1+"\n"
                elif item.Tipo=="Texto":
                    vv=item.atributos["setTexto"].replace("\"","")
                    texto+="<input type = \"text\" id=\""+item.ID+"\" value=\""+vv+"\"style=\"text-align:"+item.atributos["setAlineacion"]+"\" />\n"
                elif item.Tipo=="AreaTexto":
                    texto+="<TEXTAREA id=\""+item.ID+"\">"+item.atributos["setTexto"]+"</TEXTAREA>\n"
                elif item.Tipo=="Clave":
                    vv=item.atributos["setTexto"].replace("\"","")
                    texto+="<input type = \"password\" id=\""+item.ID+"\"value=\""+vv+"\" style=\"text-align:"+item.atributos["setAlineacion"]+"\"/>\n"
                elif item.Tipo=="Contenedor":
                    texto+="<div id=\""+item.ID+"\">\n"
                    if len(item.CONTIENE)!=0:
                        for item2 in item.CONTIENE:
                            texto+=Contenedor(item2,ListaControles)
                    texto+= "</div>\n"
        texto+="</BODY>\n"
        texto+="</HTML>\n"
        return texto

    def rCSS(ListaControles):
        
        texto=""
        for item in ListaControles:
            texto+="#"+item.ID+"{\n"

            #setPosición
            if len(item.atributos["setPosicion"])!=0: 
                v=item.atributos["setPosicion"].split(",")
                texto+="position: absolute;\n"
                texto+="left:"+v[0]+"px;\n"
                texto+="top:"+v[1]+"px;\n"

            #setAncho
            texto+="width :"+item.atributos["setAncho"]+"px;\n"

            #setAlto
            texto+="height :"+item.atributos["setAlto"]+"px;\n"

            #setColorFondo(R,G,B);  
            if len(item.atributos["setColorFondo"])!=0: 
                texto+="background-color: rgb("+item.atributos["setColorFondo"]+");\n"

            #setColorLetra(R,G,B);
            if len(item.atributos["setColorLetra"])!=0: 
                texto+="color: rgb("+item.atributos["setColorLetra"]+");\n\n"
            texto+="}"

        return texto

    Temp=open("Página.html","w", encoding="utf-8") 
    Contenido=rHTML(ListaControles)
    Temp.write(Contenido)
    Temp.close
    print("HTML generado")

    Temp=open("Página.css","w", encoding="utf-8") 
    Contenido=rCSS(ListaControles)
    Temp.write(Contenido)
    Temp.close
    print("CSS generada")