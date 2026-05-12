from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass

    def mostrar_info(self):
        return f"Servicio: {self.nombre} | Precio base: {self.precio}"


class ServicioSala(Servicio):
    def calcular_costo(self):
        return self.precio * 1.10


class ServicioEquipos(Servicio):
    def calcular_costo(self):
        return self.precio * 1.15


class ServicioAsesoria(Servicio):
    def calcular_costo(self):
        return self.precio * 1.20