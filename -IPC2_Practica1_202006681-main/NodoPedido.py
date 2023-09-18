"""
            Pedido
Tipo de HotDog: "ingrediente"
Cantidad: "Cantidad"
Tiempo en cola: "Sumatoria de ordenes pendientes."
"""
class Pedido:

    def __init__(self,nombre,dirección,nit, formaPago,ingrediente, tiempo, cantidad):
        
        self.nombre=nombre
        self.dirección=dirección
        self.nit=nit
        self.formaPago=formaPago
        self.ingrediente=ingrediente
        self.tiempo=tiempo
        self.cantidad=cantidad
        self.anterior=None
        self.siguiente=None