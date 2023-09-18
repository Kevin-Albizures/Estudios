##### 29/07/2022
---
## **Memoria Dinámica Y** 

## **Gestión de Apuntadores**

> Existen dos tipos de memoria con la que operan los lenguajes de programación:
> 1. Estática: Se define explícitamente al declarar una variable. El compilador es el encargado de reservar esa memoria. Se mantiene fija durante toda la vida de la variable.
>  
> 2. Dinámica: Utiliza una parte de la memoria principal denominado heap; Apoya el uso de la memoria durante la ejecución; Requiere apuntadores que almacena en direcciones de memoria real.   
>
> Estructura lógica:
>   - Segmentos de código del 1 al N: almacena el código compilado.
>   - Segemento de datos: Almacena las variables globales y los datos del programa.
>   - Pila: Almacena las variables locales y la de control del programa.
>   - Montículo: Almacena las variables dinámicas, tiene como límite la capacidad de memoria disponible.
>    
>   - ![Estructura_lógica](/FotosI/Estructura%20lógica.png)

## Asignación de memoria dinámica

> - El espacio a utilizar por la variable dinámica se va creando conforme se vaya ejecutando el programa.
> - La asignación dinámica de memoria controla los requisitos de memoria del programa.

## Variables Punteros

> Es una variable que señala la posición en la memoria en que se encuentra otro dato como valor (su registro base).   
> Este valor puede ser una variable simple, arreglos, estructuras, funciones, etc.
>
> La manera de proteger las direcciones de memoria de las variables es por medio de sus registros base y límite.

Tamaño de los tipos de datos:
- int: 4 bits
- apuntador: 4 bits
- caracter: 1 bit

> ### Momentos en cuando un apuntador lleva (*)
> - Cuando se define un apuntador.
> - Cuando se quiere ingresar a la información de ese apuntador.

> Los punteros como ejemplo de una mejor práctica, deben apuntar a null cuando son inicializados.

## Crear y liberar memoria

> Cuando se usa la memoria dinámica se puede cargar y descargar dependiendo del problema a resolver, según el lenguaje de programación a usar se usan diferentes operaciones.  
> 
> Para ocupar espacio en la memoria: 
> 
> - Se define el apuntador (**Tipo de dato**  *apunt)
> 
> Para liberar el espacio en memoria:
> - Usando delete **apunt** 

## **Reglas para programar con apuntadores y memoria dinámica**

> - Por cada vez que se ejecute un crear, se deberá ejecutarse un delete antes de culminar la ejecución de un programa.
> 
> - Un liberar actúa liberando el espacio de apuntado.
> 
> - Un apuntador local a un modulo se destruye al terminar su ejecución, sin importar a qué espacio hace referencia.
> 
> - Los valores basura y nulo son diferentes.
> 
> - Hacer un liberar con un apuntador que no hace referencia a un espacio de memoria dinámica provoca fallas de ejecución.
> 
> - Una referencia a través de un apuntador, cuyo valor sea Nulo, provocará fallas en la ejecución del programa.
> 
> - No siempre se tiene que realizar un crear para utilizar un apuntador.
> 
> - Los valores de los apuntadores se pueden comparar para verificar si señalan al mismo valor.
> 
> - A un dato referenciado por un apuntador se le puede aplicar todas las operaciones validas para el tipo de dato.

## Operadores de punteros 

> Operador monario y prefijo
> - (&) devuelve la dirección de memoria base del dato al que precede.
> - (*) accede a lo que hay en la dirección de memoria a la que precede.


##### 04/08/2022
---
## **TIPOS DE DATOS ABSTRACTOS**

> ### Enteros
> Tamaño: 4 bits = 4*8=32 bits  
> Con 32 bits se pueden representar 4294967296 valores
> 
> ### Número reales
> Tamaño: 32 bits 3.4E-38  a  3.4E38
> 
> ### Valores lógicos
> 
> ### Caracteres

## TDA

> Es un tipo de dato definido por el programador. Su desarrollo es independiente del lenguaje de programación utilizado.
> 
> ### Estructura 
>
>Como los elementos de cada estructura están dispersos por toda la memoria, es necesario tener un mecanismo para saber cuál elemento será el siguiente en seguir.
> - Cada elemento es un **Nodo**.
> - Cada nodo contiene la información y por lo menos un puntero que indica el siguiente elemento.
> - Existe una variable de tipo puntero que señala el primer elemento.

## **Tipos**
> De acuerdo a su comportamiento, los conjuntos lineales se clasifican en:
> - Listas
> - Pilas
> - Colas
> 
> De acuerdo a su implementación, las **listas** se clasifican en:
> - Simples
> - Doblemente enlazadas
> - Circulantes
> - Ortogonales

## Listas

> - Una lista es una colección de 0 o más elementos. En una lista todos los elementos son del mismo tipo.
> - Son estructuras lineales, es decir que cada elemento está colocado uno detrás del otro.
> - Permite un trabajo dinámico con un grupo de elementos.

## Listas Simples (Nivel lógico)

> Se define como un conjunto de nodos.
> - Uno detrás del otro.
> - Del cual siempre se conoce el nodo inicial y final.
> - Cada nodo tiene su propio contenido.
> - Todos tienen un sucesor único.
> 
> ### Comportamiento
> 
> - Crear y eliminar.
> - Conocer si está vacía.
> - Añadir elementos y removerlos.
> - Consultar el primer y último elemento.
> - Imprimir sus elementos en pantalla.
> - Buscar un elemento con cierta información en la lista.
> 
> ### Implementación Contigua
> 
> Se utilizan arreglos, por lo tanto tiene límites, los nodos son adyacentes en memoria.
> 
> - Al crearla se debe indicar el tamaño máximo del arreglo.
> 
> - Al insertar o remover un elemento todos lo elementos restantes avanzarán o retrocerán.

## Listas Simples Enlazadas

> Es una implementación flexible
> - Los nodos ya no están adyacentes en la memoria.
> 
> - Cada nodo tiene su contenido y su puntero que indica el siguiente nodo (enlace).
> 
> - Al insertar o eliminar un nodo ya no hay que mover al resto de elementos, solo enlazarlo a la lista.
> 
> ### Comportamientos
> 
> - Crear y eliminar
> 
> - Consultar y modificar contenido.
> 
> - Consultar y modificar sus enlaces.
> 
> ### Declaración:
> 
> - typedef struct TLSE_Nodo{
>   - Generico G;
>   - Struct TLSE_Nodo *sig;
> 
> - }LSE_Nodo;
> 
> - typedef LSE_Nodo * LSE_NodoPTR
>
> ### Implementación de la lista:
> 
> - En una lista se tiene que llevar un control de las posiciones.
> 
> - En la lista las posiciones contienen direcciones de memoria: punteros.
> 
> - La posición de un nodo estará dada por un puntero.
> 
> - La lista enlazada no tiene nodos predefinidos. Se van creando según se vayan necesitando.
>
> ### Busqueda en la lista
> - Hay que ubicarse en el inicio: header
> 
> - E ir avanzando hasta: Encontrar el nodo con la información buscada o que ya no haya más nodos.
> 
> - Como no se usan índices, se usan punteros: Comenzará en el header e irá avanzando.
> 
> - Al encontrar el nodo buscado, no se retorna su posición como índice, esta no importa.
> 
> - Se retorna la dirección de este nodo (puntero).

Ejemplos:

![Ej1](/FotosI/Ej%20Insercion%20nodo.png)

###### 12/08/2022

---

## Insertar al inicio/Final

![Ej1](/FotosI/Insertar%20nodos%20ej.png)

## Insertar en medio

> - Debe recibir la posición donde se va a insertar.


## Sacar Nodos de Listas

![Sacar nodos](/FotosI/Sacar%20un%20nodo.png)

> - La lista no debe estar vacía.

## Para sacar justo un nodo

> - No debe estar vacía.
>
> - La posición enviada debe existir en la lista.
>
> - Revisar si se desea eliminar el header o el last.

![Sacar nodos](/FotosI/Sacar%20justo%20un%20nodo.png)


##### 19/08/2022
---

## **ESTRUCTURA PILAS Y COLAS**

> **PILAS:** todas las inserciones se realizan por arriba y de igual las extracciones cumplen ese requisito.  
>       
>   - PUSH: Ingresar elemento a la lista.
>   - POP: Extraer elemento.
> 
> **COLAS:** Todas las inserciones se realizan por arriba y las extracciones se realizan desde abajo.
> - Adicionar: Ingresar elemento.
> - Extraer: Extrae elemento.
