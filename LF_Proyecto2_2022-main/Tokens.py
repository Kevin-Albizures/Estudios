
"""<!--Controles>

/* HOLA 
fasfaksjflak
fasdflasÃ±l4kas
faksdfas
asdjflakds
fasdfkal

*/
Contenedor Fa0; 
<Controles -->"""
#Tokens
global tokens,lexemas
tokensControl={
    "LLAL"          :"<",
    "LLAR"          :">",
    "COMENTARIOM"   :"/*",
    "CONTROLES"     :"Controles",
    "EXCLAMACION"   :"!",
    "MENORDOBLE"    :"--",
    "ETIQUETA"      :"Etiqueta",
    "BOTON"         :"Boton",
    "CHECK"         :"Check",
    "RADIOBOTON"    :"RadioBoton",
    "TEXTO"         :"Texto",
    "AREATEXTO"     :"AreaTexto",
    "CLAVE"         :"Clave",
    "CONTENEDOR"    :"Contenedor",
    "PUNTOCOMA"     :";"
}
TokensPropiedades={
    "LLAL"          :"<",
    "LLAR"          :">",
    "COMENTARIOM"   :"/*",
    "PROPIEDADES"     :"propiedades",
    "EXCLAMACION"   :"!",
    "MENORDOBLE"    :"--",
    "PARENTESISABRIR" :"(",
    "PARENTESISCERRAR": ")",
    "COLORLETRA"      :"setColorLetra",
    "TEXTO"         :"setTexto",
    "ALINEACION"    :"setAlineacion",
    "COLORFONDO"    :"setColorFondo",
    "MARCACONTROL"  :"setMarcada",
    "GRUPO"         :"setGrupo",
    "TAMAÑOANCHO"   :"setAncho",
    "TAMAÑOALTO"    :"setAlto",
    "PUNTO"         :".",
    "PUNTOCOMA"     :";"
}
TokensColocacion={
    "LLAL"          :"<",
    "LLAR"          :">",
    "COMENTARIOM"   :"/*",
    "COLOCACION"     :"Colocacion",
    "EXCLAMACION"   :"!",
    "MENORDOBLE"    :"--",
    "PARENTESISABRIR" :"(",
    "PARENTESISCERRAR": ")",
    "POSICION"      :"setPosicion",
    "ADD"         :"add",
    "THIS"    :"this",
    "PUNTO"         :".",
    "PUNTOCOMA"     :";"
}
lexemasControl={
    "LLAL"          :"<--Control",
    "LLAR"          :"Control-->",
    "COMENTARIOM"   :"/*[TEXTO]*/",
    "CONTROLES"     :"<!--Control , Control-->",
    "EXCLAMACION"   :"<!--Control , Control-->",
    "MENORDOBLE"    :"<!--Control , Control-->",
    "ETIQUETA"      :"Etiqueta \"ID\" ",
    "BOTON"         :"Boton \"ID\"",
    "CHECK"         :"Check \"ID\"",
    "RADIOBOTON"    :"RadioBoton \"ID\"",
    "TEXTO"         :"Texto \"ID\"",
    "AREATEXTO"     :"AreaTexto \"ID\"",
    "CLAVE"         :"Clave \"ID\"",
    "CONTENEDOR"    :"Contenedor \"ID\"",
    "PUNTOCOMA"     :";"
}

lexemasPropiedades={
    "LLAL"          :"<--Propiedades",
    "LLAR"          :"Propiedades-->",
    "COMENTARIOM"   :"/*[TEXTO]*/",
    "PROPIEDADES"     :"<!--Propiedades , Propiedades-->",
    "EXCLAMACION"   :"<!--Propiedades",
    "MENORDOBLE"    :"<!--Propiedades",
    "PARENTESISABRIR" :"([Valor])",
    "PARENTESISCERRAR": "([Valor])",
    "COLORLETRA"      :"setColorLetra(numero, numero , numero);",
    "TEXTO"         :"setTexto (\"texto del control\");",
    "ALINEACION"    :"setAlineacion(valor);",
    "COLORFONDO"    :"setColorFondo (numero, numero, numero);",
    "MARCACONTROL"  :"setMarcada (parametro);",
    "GRUPO"         :"setGrupo(ID);",
    "TAMAÑOANCHO"   :"setAncho(numero);",
    "TAMAÑOALTO"    :"setAlto(numero); ",
    "PUNTO"         : ".",
    "PUNTOCOMA"     :";"
}
lexemasColocacion={
    "LLAL"          :"<!--Colocacion",
    "LLAR"          :"Colocacion-->",
    "COMENTARIOM"   :"/*[TEXTO]*/",
    "COLOCACION"     :"<!--Colocacion , Colocacion-->",
    "EXCLAMACION"   :"<!--Colocacion",
    "MENORDOBLE"    :"<!--Colocacion , Colocacion-->",
    "PARENTESISABRIR" :"([Valor])",
    "PARENTESISCERRAR": "([Valor]))",
    "POSICION"      :".setPosicion",
    "ADD"         :".add",
    "THIS"    :"this.",
    "PUNTO"         :"[Control].[Propiedad]",
    "PUNTOCOMA"     :";"
}