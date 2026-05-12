class Cliente:
    def __init__(self, nombre, id_cliente):
        if not nombre:
            raise ValueError("El nombre del cliente no puede estar vacío")
        
        if id_cliente <= 0:
            raise ValueError("El ID del cliente debe ser mayor a 0")

        self.nombre = nombre
        self.id_cliente = id_cliente

    def mostrar_info(self):
        return f"Cliente: {self.nombre} | ID: {self.id_cliente}"