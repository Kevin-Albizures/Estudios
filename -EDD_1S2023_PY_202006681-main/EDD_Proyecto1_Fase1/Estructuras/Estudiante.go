package Estructura
//El nodo solito xd
type Estudiante struct {
	nnombre string
	Contraseña string
	carnet int
	Bitacora *Pila
	next  *Estudiante
	back  *Estudiante
}

type Bitacora struct{
	texto string
	fechaa string
	next *Bitacora
	back *Bitacora
}