package Estructura

import (
	"fmt"
	"strconv"
	"os"
	"time"
)

// Declaración de la estructura
type List struct {
	head *Estudiante
	tail *Estudiante
}

// Se agrega el puntero hacia el struct para hacerlo parte de el

func (list *List) Insert(nombre string , Apellido string,carnet int, Contraseña string) {
	nnombre:=nombre+" "+Apellido
	
	newEstudiante := &Estudiante{nnombre: nnombre,carnet: carnet,Contraseña:Contraseña,next: nil,back: nil,Bitacora:&Pila{}}
	
	if list.head == nil {
		list.head = newEstudiante
		list.tail=newEstudiante
	} else {
		
		temp := list.head
		for temp.next != nil {
			temp = temp.next
		}
		newEstudiante.back=temp
		temp.next = newEstudiante
		list.tail=newEstudiante
		
	}
	fmt.Print("Estudiante "+nnombre+"ingresado...\n")
}



// Método para imprimir la lista
func (list *List) Print() {
	temp := list.head
	if temp!=nil{
		fmt.Print("\n-------------- LISTADO DE ALUMNOS -------------\n")
		for temp.next != nil {
			fmt.Printf("- Nombre: "+temp.nnombre+", Carnet: "+strconv.Itoa(temp.carnet))
			temp = temp.next
			fmt.Print("\n-----------------------------------------------\n")
		}
			fmt.Printf("- Nombre: "+temp.nnombre+", Carnet: "+strconv.Itoa(temp.carnet))
			fmt.Print("\n-----------------------------------------------\n")
		fmt.Print("\n")
	}else{
		fmt.Print(" *********************************************\n")
		fmt.Print("*          No hay alumnos asignados          *\n")	
		fmt.Print(" *********************************************\n")
	}
	
}

// Método para buscar
func (list *List) Find(carnet int) (result bool) {
	temp := list.head
	result = false
	if list.head!=nil{
		for temp != nil {
			if temp.carnet == carnet {
				result = true
			}
			temp = temp.next
		}
	}
	return result
}

//Comprobar inicio de sesión
func (list *List) Comprobar(carnet int, contraseña string) (result bool) {
	temp := list.head
	result = false
	if list.head!=nil{
		for temp != nil {
			if temp.carnet == carnet && temp.Contraseña==contraseña {
				result = true
				now:=time.Now()
				temp.Bitacora.EnPila("Se inicio sensión ",now.Format("2006-01-02 15:04:05"))
				temp.Bitacora.Print()
			}
			temp = temp.next
		}
	}
	return result
}



func (list *List) Verifica() (result bool){
    return list.head!=nil

}


// GENERAR CÓDIGO GRAPHVIZ
func (list *List) GraphCode() string {
	temp := list.head
	if temp!=nil{
		nodes := ""
		contenido := ""
		counter := 0
		counter2 := 0
		nodes2:=""
		contenido2:=""
		contenido2_2:=""
		nodes+="NZ[label=\"Null\"];\nNZZ[label=\"Null\"];\n"
		contenido+="NZ->"
		for temp.next != nil {
			nodes += "N" + strconv.Itoa(counter) + "[label=\"Carnet:" + strconv.Itoa(temp.carnet) + "\nNombre: " + temp.nnombre + "\"];\n"
			contenido += "N" + strconv.Itoa(counter) + "->"
			if temp.Bitacora.head!=nil{  
				nodes2 += ""
				contenido2 += "N"+strconv.Itoa(counter)+"->"
				contenido2_2+="{rank=same; N"+strconv.Itoa(counter)  
				temp2:=temp.Bitacora.head
				for temp2.back != nil {
					nodes2 += "J" + strconv.Itoa(counter2) + "[label=\"" + temp2.texto+ "\n " + temp2.fechaa + "\"];\n"
					contenido2 += "J"+strconv.Itoa(counter2) + "->"
					contenido2_2+=" J"+strconv.Itoa(counter2)
					temp2 = temp2.back
					counter2++
				}
				nodes2 += "J" + strconv.Itoa(counter2) + "[label=\""+ temp2.texto+ "\n " + temp2.fechaa +"\"];\n"
				contenido2 += "J"+strconv.Itoa(counter2) + "\n"
				contenido2_2+=" J"+strconv.Itoa(counter2)+"}\n"
			}
			temp = temp.next
			counter++
		}
		nodes += "N" + strconv.Itoa(counter) + "[label=\"Carnet:" + strconv.Itoa(temp.carnet) + "\nNombre: " + temp.nnombre + "\"];\n"
		contenido += "N" + strconv.Itoa(counter) + "->NZZ\n"
		temp = list.tail
		for temp.back != nil {
			contenido += "N" + strconv.Itoa(counter)+"->"
			temp = temp.back
			counter--
		}
		contenido += "N" + strconv.Itoa(counter)+"\n"

		return "digraph G {\n" +
			"node[shape=septagon, style=filled, color=darkgoldenrod];\n" +
			"rankdir=LR;\n" +
			nodes +
			contenido + 
			nodes2 +
			contenido2 +
			contenido2_2 +
			"\n}"
	}
	fmt.Print("********** Lista vacía **********")
	return "digraph G {\n" +
	"node[shape=septagon, style=filled, color=darkgoldenrod];\n" +
	"rankdir=LR;\n NZ[label=\"** Lista Vacía **\"];\n}"
}

// GENERAR CÓDIGO GRAPHVIZ
func (list *List) JSONCode() {
	temp := list.head

	if temp!=nil{
		// Abrir el archivo en modo de escritura
		archivo, err := os.Create("Reporte.json")
		if err != nil {
			fmt.Print("Se encontró un error al generar el reporte: ")
			fmt.Println(err)
			return 
		}
		defer archivo.Close()

		// Escribir en el archivo
		text:=""
		text+=	"{\n"+
				"	alumnos: [\n"
		for temp.next != nil {
			text+="		{"+
				"			\"nombre\": \""+temp.nnombre+"\"\n"+
				"			\"carnet\": "+strconv.Itoa(temp.carnet)+"\n"+
				"			\"contraseña\": \""+temp.Contraseña+"\"\n"+
				"			\"Carpeta_Raiz\": \"/\""+"\n"+
			"		},\n"
			temp=temp.next
		}
		text+="		{"+
				"			\"nombre\": \""+temp.nnombre+"\"\n"+
				"			\"carnet\": "+strconv.Itoa(temp.carnet)+"\n"+
				"			\"contraseña\": \""+temp.Contraseña+"\"\n"+
				"			\"Carpeta_Raiz\": \"/\""+"\n"+
			"		}\n"
		text+=	"	]\n"+
				"}"
		_, err = archivo.WriteString(text)
		if err != nil {
			fmt.Print("Se encontró un error al generar el reporte: ")
			fmt.Println(err)
			return 
		}
	}else{
		fmt.Print("********** Lista vacía **********")
	}
}