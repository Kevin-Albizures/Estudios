
##### **Clase 21/07/2022**
---
# **UNIDAD 1**
## **Administración De La Memoria**

> Gestión de Memoria: Es realizada por el S.O. Para eso gestiona MMU o Unidad de Administración de Memoria el cuál transforma las direcciones lógicas en físicas. 
>  
> Objetivos de la gestión de memoria:
> - Ofrecer a cada proceso un espacio lógico propio.
> - Proporcionar protección entre procesos.
> - Permitir que los procesos compartan memoria.
> - Maximizar el rendimiento del sistema.      



##### **Clase 22/07/2022** 

---

## **Algunos términos:**

> - Multiprogramación: Es la técnica de cuando dos o más procesos pueden alojarse en la memoria principal y ejecutarse juntos por el procesador.
>
> - Memoria Principal: Es donde se alojan temporalmente los datos que el CPU está procesando o va a procesar en un determinadao momento.
>
> - Memoria Secundaria: Son memorias con mayor capacidad pero más lentas. Se usan como dispositivos de almacenamiento masivo.

## **Requisitos para gestionar la memoria**

> - Reubicación:   
> Los procesos van y vienen dentro de la memoria principal, lo que hace que tengan que ser cargados y descargados de la memoria.   
> 
> - Protección:   
> Protege los espacios de direcciones de los posibles accesos que puedan ocurrir mientras los procesos se están ejecutando.    
> 
> - Compartición:   
> Es cuando bajo supervisión y por medio del S.O. Se tienen procesos compartiendo el mismo espacio de dirección.
> 
> - Organización lógica:   
> Es un espacio lineal donde se almacenan los procesos y tiene comunicación con la memoria principal o secundaria.
> 
> - Organización física:    
> Debe ser parte de la gestión de memoria, es la organización de todos los procesos o datos que se dan entre la memoria principal y la memoria secundaria.

## **Administración de la memoria**
> 
> ### Objetivos de la Administración de memoria:
> 
> - Proveer una abstracción simple de programación.
> 
> - Proveer aislamiento entre procesos.
> 
> - Asignar memoria (Limitada) a procesos que la requieren maximizando el rendimiento.
> 
> ### Mecanismos:
> 
> - Memoria física versus virtual.
> 
> - Administración de tablas de páginas y segmentación.
> 
> - Algoritmos.

## **Otros términos**

> Memoria física: Son chips de memoria RAM que están insertados en las ranuras de la placa madre.
> 
> Memria Virtual: No son chips existentes, es simulada mediante otro medio (comunmente siendo un disco duro).

## **Memoria Virtual**

> Abstracción básica que proporciona S.O. para la administración de memoria.   
>   - Permite la ejecución de procesos sin estar contenidos completamente en memoria física.
>       - Puede ser porque un programa necesite más memoria de la que se dispone.
>
>   - Es posible porque algunos programas no requieren de toda la información o datos al mismo tiempo.
>       - El S.O. puede asignar memoria durante el tiempo de ejecución.
>
>   - Memoria virtual aisla procesos.
>       - Cada proceso tiene su propio espacio de direccionamiento.  
> 
> La implementación de memoria virtual requiere apoyo del hardware:
> 1. MMUs
> 2. TLBs (Buffer de transmission anticipada): Es una memoria caché administrada por la MMU y contiene la tabla de paginación (relaciones entre las direcciones virtuales y reales).
> 3. Tablas de páginas
> 
>       ![Ejemplo 2](/FotosI/Memoria%20lógica.png)

## Historia 

> Sistemas Batch:   
> - Programas usaban mejor memoria física directamente.
> - OS cargaba trabajo, lo ejecutaba y lo descargaba.   
> 
> Sistemas Multiprogramados:
> - Múltiples procesos coexistían al mismo tiempo.
>   - Procesos usaban CPU y dispositivos I/O simultaneamente.
> - Requerimientos de administración de memoria.
>   - Protección, restringiendo espacios de direccionamiento para evitar daños entre ellos.
>   - Traducción rápida, acceso a la memoria debe ser rápida.
>   - Cambia contexto, debe ser rápido, (Protección y traducción).
> - Swapping
>   - Salvar el estado de programa completo (incluyendo memoria) a disco para permitir la ejecución de otros.
>   - Swap in: de disco a memoria.
>   - Swap out: de memoria a disco

## Direcciones Virtuales

> Para facilidades de los procesos, estos usan la memoria virtual.
> - Direcciones virtuales son independientes a las direcciones de memoria física (Donde realmente están los datos).
>   - SO determina la ubicación de la memoria física.
> - Las instrucciones que trabaja el CPU usan direcciones virtuales.
>   - Punteros, argumentos de load/store, PC, etc.
> - Traducciones de direcciones virtuales a físicas se realiza por hardware con ayuda del SO.

El conjunto de direcciones virtuales que un proceso puede direccionar corresponde a su espacio de direccionamiento.    
Existen muchos mecanismos para la traducción de direcciones virtuales a físicas:
- Particiones fijas.
- Particiones variables.
- Paginación (Moderna).
- Segmentación (Moderna).
- Paginación y segmentación.

## **Traducción con particiones fijas**

> ### Memoria física
> Se divide en particiones fijas, son de tamaño fijo y nunca cambian pero pueden haber particiones de diferentes tamaños.   
> 
> - Hardware requerido: **Registro base y registro limite.**
>   - Dirección física = dirección virtual + registro base.
>   - Registro base es cargado por el SO después del cambio de contexto y entonces un proceso será ejecutado (indica el inicio).
>   - Para la protección entonces: Si (Dirección física > registro base + limite) entonces error
> - Ventajas: Sencillo y cambio de contexto rápido.
> - Desventajas: 
>   - Fragmentación interna: Partición más grande de lo necesario.
>   - Fragmentación externa: Donde dos particiones disponibles pero ambas son pequeñas para contener un proceso grande.
> Entonces cuál debería de ser el tamaño de la partición.
> 
>   ![Ejemplo 2](/FotosI/Particiones%20fijas.png)

## **Traducciones con particiones variables**

> Ventajas
> - No hay fragmentación interna (Si sabemos cuanto necesita el proceso)
> - Asignar partición solo lo suficiente para contener el proceso.
> 
> Desventajas
> - Fragmentación externa: Van quedando porciones de memoria sin ser reutilizada.
> 
>   ![Ejemplo 2](/FotosI/Traduccion%20con%20particiones%20variables.png)

## **¿Qué hacer con la fragmentación?**
> Swap out: Sacar programa de memoria.
> 
> Acercar los programas recargandolos.
> 
> Aunque eso no es tan eficiente.

## **Paginación (Técnica Actual)**

> - Concepto
>   
>   ![Ejemplo 2](/FotosI/Páginación.png)
> 
>   ![Ejemplo](/FotosI/Paginación%202.png)
> 
> - Ejemplo de paginación: 
>   
>   ![Ejemplo 2](/FotosI/Paginación%20ej1.png)
> 


## **Estrategias de asignación**

> - First fit: utilizar el primer bloque accesible.
> - Best fit: Utilizar el mejor bloque que se adecue al proceso.
> - Worst fit: Utilizar el bloque más grande para almacenar el proceso.

##### Clase 28/07/2022

---

## **Aspectos de la paginación**

> - El cociente es la página.
> - El residuo es el desplazamiento.
> - Pasos:
>   1. Se divide la dirección lógica en forma de la capacidad de las páginas.
>   2. Después se busca en el marco de página el resultado de la división anterior.
>   3. Se calcula la dirección física de la dirección virtual.

## **Ventajas de la paginación**

> - Fácil para asignar memoria física:
>   - Se administra la memoría física usando un marco de páginas libres.  
>   - Fragmentación externa no es un problema.
> - Fácil quitarles páginas a programas:
>   - Páginas son de particiones fijas.
>   - Uso de bits válido para saber que páginas ha perdido el proceso.

## **Desventajas de la páginación**

> - Expone fragmentación interna.
>   - No puede usar memoria de marco que le sobra a otro proceso.
>   - Referencia a memoria en 2 pasos.
>   - Memoria requerida para mantener tablas de páginas puede ser grande.

## **SEGMENTACIÓN**

> Permite observar la memoria en varios bloques de direcciones o segmentos dinámicos con un tamaño variable.   
> Se pueden asignar a cada elemento derechos de acceso y uso.
> 
> ![Ejemplo 2](/FotosI/Segmentación.png)

## **Garbage Collector**

> Reconoce los bloques de memoria no referenciados.  
> 
> Recolectores de traza:
> - Recolector de marcas (traicing collector).
>   - Recolector de copias (Mark-sweep Collection).
>   - Recolector de copias (Copying collection).
>   - Recolector incremental (Incremental collection).
>   - Recolector conservador (Conservative collection).
> 