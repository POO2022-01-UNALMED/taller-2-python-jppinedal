class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color 
        self.precio = precio
        self.registro = registro
    def cambiarColor(self,color):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        lista_tipo = ["gasolina","electrico"]
        if tipo in lista_tipo:
            self.tipo = tipo

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    def cantidadAsientos(self):
        j = 0
        for i in self.asientos:
            if i != None:
                j += 1
        return j
    def verificarIntegridad(self):
        if self.motor.registro != self.registro:
            return "Las piezas no son originales"
        for i in self.asientos:
            if i != None:
                if i.registro != self.registro:
                    return "Las piezas no son originales"
        return "Auto original"