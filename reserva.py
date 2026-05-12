class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a 0")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo() * self.duracion
            return costo
        except Exception as e:
            raise Exception("Error al procesar la reserva") from e

    def mostrar_info(self):
        return f"Reserva de {self.cliente.nombre} | Servicio: {self.servicio.nombre} | Estado: {self.estado}"