package Estructura

import (
	"fmt"
	"strconv"
)


type Pila struct {
    head *Bitacora
	tail *Bitacora
}

func (Pila *Pila) EnPila(texto string , fechaa string) {
    newNodoB1 := &Bitacora{texto:texto, fechaa: fechaa, back:nil, next:nil}
    if Pila.head == nil {
        Pila.head = newNodoB1
		Pila.tail = newNodoB1
    } else {
		
        newNodoB1.back =Pila.head
        Pila.head.next = newNodoB1
		Pila.head = newNodoB1
    }
	//fmt.Print("Inserción a nodo hecha.")
}

// Método para imprimir la lista
func (Pila *Pila) Print() {
	temp := Pila.head
	for temp.back != nil {
		fmt.Printf("\n"+temp.texto+temp.fechaa)
		temp = temp.back
		fmt.Print("\n")
	}
	fmt.Printf("\n"+temp.texto+temp.fechaa)
	fmt.Print("\n")
}

func (Pila *Pila) DePila(carnet int) interface{} {
    if Pila.head == nil {
        return nil
    }
    value := Pila.head
    Pila.head = Pila.head.back
    if Pila.head == nil {
        Pila.head = nil
    }
	fmt.Print("Bitacora reducida")
    return value
}

// GENERAR CÓDIGO GRAPHVIZ
func (Pila *Pila) GraphCode() string {
	temp := Pila.head
	if temp!=nil{
		nodes := ""
		contenido := ""
		counter := 0    
		for temp.back != nil {
			nodes += "N" + strconv.Itoa(counter) + "[label=\"" + temp.texto+ "\n " + temp.fechaa + "\"];\n"
			contenido += "N" + strconv.Itoa(counter) + "->"
			temp = temp.back
			counter++
		}
		nodes += "N" + strconv.Itoa(counter) + "[label=\""+ temp.texto+ "\n " + temp.fechaa +"\"];\n"
		contenido += "N" + strconv.Itoa(counter) + "\n"

		return "digraph G {\n" +
			"node[shape=septagon, style=filled, color=darkgoldenrod];\n" +
			"rankdir=LR;\n" +
			nodes +
			contenido + 
			"\n}"
	}
	fmt.Print("********** Pila vacía **********")
	return "digraph G {\n" +
	"node[shape=septagon, style=filled, color=darkgoldenrod];\n" +
	"rankdir=L;\n NZ[label=\"** Pila Vacía **\"];\n}"
}

