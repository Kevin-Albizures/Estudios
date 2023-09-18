## Apuntadores
 
> Para asignación:
> - ap <- crear tipo_de_variable
> 
> Ejemplo para gestionar los punteros:
> - int *ap    
> - ap <- crear int;
> - Desplegar "Edad: "
> - Ingresar *ap 
> - Desplegar "Tu edad es: " *ap
> - Liberar ap
> 
> Para usar los operadores monarios: 
> - desplegar (&**i**)
> 
> Para definir listas:
> - TipoDef estructura{
> - int último
> - ArrayU elemetos;
> - } LSCont;
> 
> Para definir una lista enlazada
> 
> - TipoDef estructura TLSE_Nodo{
>   - Generico G;
>   - Struct TLSE_Nodo *sig;
> - }LSE_Nodo;
> - TipoDef LSE_Nodo * LSE_NodoPTR
>
> Para crear una lista y liberarla:
> ![Ej 1](/FotosI/Crear%20una%20lista.png)

> Para crear un nodo: 
> ![Ej 2](/FotosI/Ej%20LSE%20Nodo.png)

> Visualizar
> ![Ej 3](/FotosI/Visualizar.png)