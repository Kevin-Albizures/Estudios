package Estructura

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


type Cola struct {
    head *Estudiante
    tail *Estudiante
}

/*func (Cola *Cola) verific() (result bool){
    if Cola.head==nil{
        return false
    } else {
        return true
    }
}*/

func (Cola *Cola) EnCola(nombre string , Apellido string , carnet int, Contraseña string) {
    nnombre:=nombre+" "+Apellido
    newNodo := &Estudiante{nnombre:nnombre, Contraseña:Contraseña, carnet: carnet, back: nil, next: nil, Bitacora: nil}
    if Cola.tail == nil {
        Cola.head = newNodo
        Cola.tail = newNodo
    } else {
        Cola.tail.next = newNodo
        Cola.tail = newNodo
    }
	fmt.Print("Inserción de solicitud hecha.\n")
}

func (Cola *Cola) Find(carnet int) (result bool) {
	temp := Cola.head
	result = false
	if Cola.head!=nil{
		for temp != nil {
			if temp.carnet == carnet {
				result = true
			}
			temp = temp.next
		}
	}
	return result
}

// Método para imprimir la lista
func (Cola *Cola) Print() (result bool) {
	temp := Cola.head
    fmt.Printf("  Carnet: "+strconv.Itoa(temp.carnet)+
                "\n  Contraseña"+temp.nnombre)
    temp = temp.next
    fmt.Print("\n")
	fmt.Printf(	"  Nombre: "+temp.nnombre+
				"\n  Contraseña"+temp.Contraseña)
	fmt.Print("\n")
    return false
}

func (Cola *Cola) DeCola(NoPendientes int) (string,int,string,int) {
    var Op int
    
	scanner:=bufio.NewScanner(os.Stdin)

    if Cola.head == nil {
        return "",0,"",0
    }

    fmt.Print(" *********** NO. Pendientes: "+strconv.Itoa(NoPendientes)+" ***********\n")  
    fmt.Print("  Estudiante Actual: "+Cola.head.nnombre+"\n")
    fmt.Print("         1. Aceptar al Estudiante           \n")
    fmt.Print("         2. Rechazar al Estudiante          \n")
    fmt.Print("         3. Volver al Menu                  \n")
    fmt.Print(" ******************************************\n")  
	fmt.Print("                      - Ingrese la opción: ")
    scanner.Scan()
	fmt.Sscan(scanner.Text(),&Op)
    fmt.Print("\n")
    
    switch Op {
    case 1:
        value := Cola.head
        Cola.head = Cola.head.next
        if Cola.head == nil {
            Cola.tail = nil
        }
        fmt.Print("Aceptando estudiante...\n")
        return value.nnombre,value.carnet,value.Contraseña , 1

    case 2:
        value := Cola.head
        Cola.head = Cola.head.next
        if Cola.head == nil {
            Cola.tail = nil
        }
        fmt.Print("Rechazando estudiante...\n")
        return value.nnombre,0,"",2
    
    case 3:
        return "",0,"",0

    default: 
        fmt.Print("No selección una opción válida, regresando...\n")
    }
    return "",0,"",0
}

// GENERAR CÓDIGO GRAPHVIZ
func (Cola *Cola) GraphCode() string {
	temp := Cola.head
    if temp!=nil{
        nodes := ""
        contenido := ""
        counter := 0    
        for temp.next != nil {
            nodes += "N" + strconv.Itoa(counter) + "[label=\"Carnet:" + strconv.Itoa(temp.carnet) + "\nNombre: " + temp.nnombre + "\"];\n"
            contenido += "N" + strconv.Itoa(counter) + "->"
            temp = temp.next
            counter++
        }
        nodes += "N" + strconv.Itoa(counter) + "[label=\"Carnet:" + strconv.Itoa(temp.carnet) + "\nNombre: " + temp.nnombre + "\"];\n"
        contenido += "N" + strconv.Itoa(counter) + "\n"

        return "digraph G {\n" +
            "node[shape=septagon, style=filled, color=darkgoldenrod];\n" +
            "rankdir=LR;\n" +
            nodes +
            contenido + 
            "\n}"
    }
    fmt.Print("********** Cola vacía **********")
    return "digraph G {\n" +
	"node[shape=septagon, style=filled, color=darkgoldenrod];\n" +
	"rankdir=LR;\n NZ[label=\"** Cola Vacía **\"];\n}"
}
