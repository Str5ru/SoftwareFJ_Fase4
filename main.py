from cliente import Cliente
from servicio import ServicioSala, ServicioEquipos, ServicioAsesoria
from reserva import Reserva

# archivo de logs
log_file = "log.txt"

def registrar_error(error):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(str(error) + "\n")


try:
    # =========================
    # CLIENTES (2 válidos)
    # =========================
    c1 = Cliente("Erick", 1)
    c2 = Cliente("Ana", 2)

    # =========================
    # SERVICIOS (3 válidos)
    # =========================
    s1 = ServicioSala("Sala de reuniones", 100)
    s2 = ServicioEquipos("Proyector", 50)
    s3 = ServicioAsesoria("Tutoría", 80)

    # =========================
    # OPERACIONES (10 EN TOTAL)
    # =========================

    # 1
    r1 = Reserva(c1, s1, 2)
    r1.confirmar()
    print(r1.mostrar_info(), "->", r1.procesar())

    # 2
    r2 = Reserva(c2, s2, 3)
    r2.confirmar()
    print(r2.mostrar_info(), "->", r2.procesar())

    # 3
    r3 = Reserva(c1, s3, 1)
    print(r3.mostrar_info(), "->", r3.procesar())

    # 4 (error intencional)
    try:
        r4 = Reserva(c1, s1, -1)
    except Exception as e:
        print("Error reserva 4:", e)
        registrar_error(e)

    # 5
    r5 = Reserva(c2, s3, 2)
    r5.confirmar()
    print(r5.mostrar_info(), "->", r5.procesar())

    # 6 (cancelación)
    r6 = Reserva(c1, s2, 1)
    r6.cancelar()
    print(r6.mostrar_info(), "->", r6.procesar())

    # 7
    r7 = Reserva(c2, s1, 4)
    print(r7.mostrar_info(), "->", r7.procesar())

    # 8 (error servicio nulo simulado)
    try:
        r8 = Reserva(c1, None, 2)
        print(r8.procesar())
    except Exception as e:
        print("Error reserva 8:", e)
        registrar_error(e)

    # 9
    r9 = Reserva(c2, s2, 2)
    print(r9.mostrar_info(), "->", r9.procesar())

    # 10
    r10 = Reserva(c1, s3, 3)
    print(r10.mostrar_info(), "->", r10.procesar())

except Exception as e:
    print("ERROR GENERAL:", e)
    registrar_error(e)