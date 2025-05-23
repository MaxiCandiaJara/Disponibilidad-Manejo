

#Creación de la clase hermano


class Hermano():


    def  __init__(self, Nombre:str ,Mañana:list,Tarde:list, Mensaje:bool, Comentario:str ):
        
        self.Nombre     = Nombre
        self.Mañana     = Mañana
        self.Tarde      = Tarde
        self.Mensaje    = Mensaje
        self.Comentario = Comentario

    def to_dict(self):
        return {
            "Nombre": self.Nombre,
            "Manana": self.Mañana,
            "Tarde": self.Tarde,
            "Mensaje": self.Mensaje,
            "Comentario": self.Comentario
        }

    def cNombre(self, Nombre):
        self.Nombre = Nombre
    
    def cMañana(self, Mañana):
        self.Mañana  = Mañana

    def cTarde(self, Tarde):
        self.Tarde  = Tarde

    def cCantidad(self, Cantidad):
        
        self.Cantidad = Cantidad

    def cMensaje(self, Mensaje):

        self.Mensaje = Mensaje

    def cComentario(self, Comentario):
        self.Comentario = Comentario

    def rNombre(self):
        return self.Nombre 
    
    def rMañana(self):
        return self.Mañana
        
    def rTarde(self):
        return self.Tarde
    
    def rCantidad(self):
        return self.Cantidad
    
    def rMensaje(self):
        return self.Mensaje
    
    def rComentario(self):
        return self.Comentario
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["Nombre"],
            data["Manana"],
            data["Tarde"],
            data["Mensaje"],
            data["Comentario"]
        )
    
    