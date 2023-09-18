package main

import (
	"bufio"
	"fmt"
	"os"
	"log"
	"time"
	"strconv"
    "encoding/csv"
	Estructura "gitb.com/EDD_ProyectoF1/Estructuras"
	dot "gitb.com/EDD_ProyectoF1/Dot"
)


func readCsvFile(filePath string) [][]string {
	f, err := os.Open(filePath)
	if err != nil {
		log.Print("Archivo no existe: "+filePath, err)
		records:= [][]string{{"", ""}}
		return records
	}
	defer f.Close()

	csvReader := csv.NewReader(f)
	records, err := csvReader.ReadAll()
	if err != nil {
		log.Print("Error en la lectura del archivo: "+filePath, err)
		records:= [][]string{{"", ""}}
		return records
	}
	return records
}

func main() {

	Cola:=Estructura.Cola{}
	ListaEnlazada:=Estructura.List{}
	PilaAdmin:=Estructura.Pila{}
	var Op int

	// Variables de Verificación
	var usuario string
	var contraseña string
	salida:=1

	//Variables de conteo
	NoPendientes:=0

	scanner:=bufio.NewScanner(os.Stdin)

	for salida==1 {
		// Menú de inicio
		fmt.Print("-----------------------------------------------\n")
		fmt.Print("--                                           --\n")
		fmt.Print("--             INICIO DE SESION              --\n")
		fmt.Print("--                                           --\n")
		fmt.Print("--  1. Inicio de sesión como administrador   --\n")
		fmt.Print("--  2. Inicio de sesión como estudiante      --\n")
		fmt.Print("--  3. Cerrar programa                       --\n")
		fmt.Print("--                                           --\n")
		fmt.Print("-----------------------------------------------\n")
		fmt.Print("                      - Ingrese la opción: ")
		scanner.Scan()
		fmt.Sscan(scanner.Text(),&Op)

		switch Op {

		case 1:
			intentos:=0
			Op1:=0
			var OpM int
			fmt.Print("\n")
			for intentos<3 {
				fmt.Print("---------- Ingreso de adiministrador ----------\n")
				fmt.Print("--                                           --\n")
				fmt.Print("    - Ingrese usuario: ")
				scanner.Scan()
				fmt.Sscan(scanner.Text(),&usuario)
				fmt.Print("    - Ingrese contraseña: ")
				scanner.Scan()
				fmt.Sscan(scanner.Text(),&contraseña)
				fmt.Print("--                                           --\n")
				fmt.Print("-----------------------------------------------\n")

				if usuario=="Admin" && contraseña=="Admin" {
					usuario=""
					contraseña=""
					fmt.Print("------------------ Bienvenido administrador ------------------\n")
					scanner.Scan()
					intentos=3
					salidaAdmin:=1
					for salidaAdmin==1 {
						// Menú de admin
						fmt.Print("-----------------------------------------------\n")
						fmt.Print("--                                           --\n")
						fmt.Print("--             MENU ADMINISTRADOR            --\n")
						fmt.Print("--                                           --\n")
						fmt.Print("--  1. Ver Estudiantes Pendientes            --\n")
						fmt.Print("--  2. Ver Estudiantes del Sistema           --\n")
						fmt.Print("--  3. Registrar Nuevo Estudiante            --\n")
						fmt.Print("--  4. Carga Masiva de Estudiantes           --\n")
						fmt.Print("--  5. Generar Bítacora                      --\n")
						fmt.Print("--  6. Cerrar Sesión                         --\n")
						fmt.Print("--                                           --\n")
						fmt.Print(" ---------------------------------------------\n")
						fmt.Print("                      - Ingrese la opción: ")
						scanner.Scan()
						fmt.Sscan(scanner.Text(),&OpM)

						switch OpM {
							
						case 1:
							i:=NoPendientes
							if i>0 {
								fmt.Print("\n----------- Estudiantes Pendientes ------------\n")
								for i!=0 {
									Nombre,carne,contra, v:=Cola.DeCola(NoPendientes)
									if v==1{
										NoPendientes--
										i--
										if ListaEnlazada.Find(carne){
											fmt.Print("Usuario ya existente, solicitud denegada. \n")
											now:=time.Now()
											PilaAdmin.EnPila("Usuario\n"+Nombre+"\nya existente: ",now.Format("2006-01-02 15:04:05"))
										} else{
											ListaEnlazada.Insert(Nombre,"", carne , contra)
											now:=time.Now()
											PilaAdmin.EnPila("Se aceptó a\n"+Nombre+": ",now.Format("2006-01-02 15:04:05"))
										}
										
									} 
									if v==2 {
										NoPendientes--
										i--
										now:=time.Now()
										PilaAdmin.EnPila("Se rechazó a \n"+Nombre+": ",now.Format("2006-01-02 15:04:05"))
									} else{
										i=0
									}
								}
							} else {
								fmt.Print(" *********************************************\n")
								fmt.Print("*        No hay solicitudes pendientes        *\n")	
								fmt.Print(" *********************************************\n")
								scanner.Scan()
							}

						case 2:
							ListaEnlazada.Print()
							scanner.Scan()
						case 3:
							Nombre:=""
							Apellido:=""
							Carnet:=0
							Passw:=""
							fmt.Print("\n----------- Añadir nuevo estudiante -----------\n")
							fmt.Print("--                                           --\n")
							fmt.Print("    - Ingrese nombre: ")
							scanner.Scan()
							fmt.Sscan(scanner.Text(),&Nombre)
							fmt.Print("    - Ingrese apellido: ")
							scanner.Scan()
							fmt.Sscan(scanner.Text(),&Apellido)
							fmt.Print("    - Ingrese carnet: ")
							scanner.Scan()
							fmt.Sscan(scanner.Text(),&Carnet)
							fmt.Print("    - Ingrese Pass: ")
							scanner.Scan()
							fmt.Sscan(scanner.Text(),&Passw)
							fmt.Print("--                                           --\n")
							fmt.Print("-----------------------------------------------\n")

							fmt.Print("Creando solicitud de estudiante..........\n")
							if Cola.Find(Carnet){
								fmt.Print("Ya has mandado una solicitud, espera que te acepten.")
							} else{
								Cola.EnCola(Nombre,Apellido,Carnet,Passw)
								NoPendientes++
							}
							scanner.Scan()

						case 4:
							var filee string
							fmt.Print("\n----------------- Carga Masiva ----------------\n")
							fmt.Print(" Ingrese la ruta del archivo: ")
							scanner.Scan()
							fmt.Sscan(scanner.Text(),&filee)
							Doc:=readCsvFile(filee)

							if Doc[0][0]!=""{
								for index, row := range Doc { // EJEMPLO DE FOR EACH EN GOLANG
									if index > 0 { // Ignorar la primera línea de encabezado
										//fmt.Print(row[0], row[1], row[2],"\n")
										carne,Error:=strconv.Atoi(row[0])
										if ListaEnlazada.Find(carne) && Error==nil{
											fmt.Print("---- El usuario: "+row[0]+" ya existe...\n")
										} else {
											if Error==nil {
												ListaEnlazada.Insert(row[1],"",carne,row[2])
											} else {
												fmt.Print("Carnet no permitido...")
											}
										}
	
									}
								}
							}
							
							scanner.Scan()
							

						case 5:
							var OpBit int
							fmt.Print("\n******************** BITACORAS ********************\n")
							fmt.Print(  "**   1. Lista enlazada doble                     **\n")
							fmt.Print(  "**   2. Reporte cola de solicitudes              **\n")
							fmt.Print(  "**   3. Reporte pila de administrador            **\n")
							fmt.Print(  "**   4. Reporte JSON                             **\n")
							fmt.Print(  " *************************************************\n")
							fmt.Print("                      - Ingrese la opción: ")
							scanner.Scan()
							fmt.Sscan(scanner.Text(),&OpBit)
							switch OpBit {
							case 1:
								path, err := os.Getwd()
								if err != nil {
									log.Println(err)
								}

								// Escribir el archivo .dot
								dot.WriteDotFile(ListaEnlazada.GraphCode(), "Lista_enlazada.dot", path)
								// Ejecutar COmando en consola
								dot.GeneratePNG("Lista_enlazada.dot", path)
								scanner.Scan()

							case 2:
								path, err := os.Getwd()
								if err != nil {
									log.Println(err)
								}

								// Escribir el archivo .dot
								dot.WriteDotFile(Cola.GraphCode(), "Cola_Solicitudes.dot", path)
								// Ejecutar COmando en consola
								dot.GeneratePNG("Cola_Solicitudes.dot", path)
								scanner.Scan()
							
							case 3:
								path, err := os.Getwd()
								if err != nil {
									log.Println(err)
								}

								// Escribir el archivo .dot
								dot.WriteDotFile(PilaAdmin.GraphCode(), "Pila_Admin.dot", path)
								// Ejecutar COmando en consola
								dot.GeneratePNG("Pila_Admin.dot", path)
								scanner.Scan()
							
							case 4:
								ListaEnlazada.JSONCode()
							
							default:
								fmt.Print("\n ****** Elija una opción válida. ******\n")	
							}

						case 6:
							fmt.Print("\n\n**************** Sesión cerrada... ****************\n")
							usuario=""
							contraseña=""
							salidaAdmin=0

						default:
							fmt.Print("\n ****** Elija una opción válida. ******\n")
						}
					}
					

				} else {
					usuario=""
					contraseña=""
					fmt.Print("\n ***** Usuario o contraseña incorrectos. *****\n")
					intentos++
					fmt.Print("**                                           **\n")
					fmt.Print("** Regresar ingrese: 1                       **\n")
					fmt.Print("** Intentar de nuevo: ENTER                  **\n")
					fmt.Print("**                                           **\n")
					fmt.Print(" *********************************************\n")
					fmt.Print("                      - Ingrese la opción: ")
					fmt.Print("\n")
					scanner.Scan()
					fmt.Sscan(scanner.Text(),&Op1)

					if Op1==1 {
						intentos=3
					}
				}
			}
			
		case 2:
			var usuario2 int
			intentos2:=0
			Op2:=0
			if ListaEnlazada.Verifica() {
				usuario2=0
				for intentos2<3 {
					fmt.Print("\n-------------- Ingreso de alumnos -------------\n")
					fmt.Print("--                                           --\n")
					fmt.Print("    - Ingrese usuario: ")
					scanner.Scan()
					fmt.Sscan(scanner.Text(),&usuario2)
					fmt.Print("    - Ingrese contraseña: ")
					scanner.Scan()
					fmt.Sscan(scanner.Text(),&contraseña)
					fmt.Print("--                                           --\n")
					fmt.Print("-----------------------------------------------\n")
		
					if ListaEnlazada.Comprobar(usuario2,contraseña) {
						
						intentos2=3
						fmt.Print("------------------ Bienvenido alumno ------------------\n")
						//now:=time.Now()
						//fmt.Print(" - "+strconv.Itoa(usuario2)+" accediste en la fecha: ")
						//fmt.Println(now.Format("2006-01-02 15:04:05"))
						scanner.Scan()
		
					} else {
						usuario2=0
						contraseña=""
						fmt.Print("\n ***** Usuario o contraseña incorrectos. *****\n")
						intentos2++
						fmt.Print("**                                           **\n")
						fmt.Print("** Regresar ingrese: 1                       **\n")
						fmt.Print("** Intentar de nuevo: ENTER                  **\n")
						fmt.Print("**                                           **\n")
						fmt.Print(" *********************************************\n")
						fmt.Print("                      - Ingrese la opción: ")
						fmt.Print("\n")
						scanner.Scan()
						fmt.Sscan(scanner.Text(),&Op2)
						
						if Op2==1 {
							intentos2=3
						}
		
					}
		
				}
			} else {
				fmt.Print("Aún no se han registrado alumnos.\n")
				scanner.Scan()
			}

		case 3:
			fmt.Print("\nCerrando programa...")
			salida=0

		default:
			fmt.Print("\n ****** Elija una opción válida. ******\n")
			scanner.Scan()

		}
	}
	
}