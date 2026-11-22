import logging
from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva
from excepciones import ErrorSistema

logging.basicConfig(
    filename="registro.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

clientes = []
servicios = []
reservas = []


def ejecutar_operacion(numero, descripcion, funcion):
    print(f"\nOPERACIÓN {numero}: {descripcion}")
    try:
        resultado = funcion()
    except Exception as error:
        logging.exception("Error en operación %s: %s", numero, error)
        print(f"Error controlado: {error}")
    else:
        logging.info("Operación %s realizada: %s", numero, descripcion)
        print(resultado)
    finally:
        print("Fin de la operación.")


def registrar_cliente(cliente):
    clientes.append(cliente)
    return f"Cliente registrado: {cliente}"


def registrar_servicio(servicio):
    servicios.append(servicio)
    return f"Servicio registrado: {servicio.describir()}"


def crear_reserva(reserva):
    reservas.append(reserva)
    return f"Reserva creada: {reserva}"


def op1():
    return registrar_cliente(Cliente("C01", "Laura Pérez", "laura@email.com", "3001234567"))

def op2():
    return registrar_cliente(Cliente("C02", "Carlos Ruiz", "carlos@email.com", "3107654321"))

def op3():
    # Dato inválido: correo sin formato correcto.
    return registrar_cliente(Cliente("C03", "Ana López", "correo-invalido", "3001112233"))

def op4():
    return registrar_servicio(ReservaSala("S01", "Sala de reuniones", 50000, 12))

def op5():
    return registrar_servicio(AlquilerEquipo("S02", "Computador portátil", 15000, 8))

def op6():
    return registrar_servicio(Asesoria("S03", "Asesoría tecnológica", 80000, "Software"))

def op7():
    # Servicio inválido: tarifa negativa.
    return registrar_servicio(ReservaSala("S04", "Sala pequeña", -1000, 5))

def op8():
    reserva = Reserva("R01", clientes[0], servicios[0], 2)
    reservas.append(reserva)
    mensaje = reserva.confirmar()
    costo = reserva.procesar(impuesto=19)
    return f"{mensaje} Costo con impuesto: ${costo:,.2f}"

def op9():
    reserva = Reserva("R02", clientes[1], servicios[1], 3)
    reservas.append(reserva)
    reserva.confirmar()
    return f"{reserva}. Costo con descuento: ${reserva.procesar(descuento=10):,.2f}"

def op10():
    # La reserva se crea, pero el servicio no está disponible.
    servicio = Asesoria("S05", "Consultoría temporal", 60000, "Redes", disponible=False)
    reserva = Reserva("R03", clientes[0], servicio, 1)
    return reserva.confirmar()


def mostrar_resumen():
    print("\n========== RESUMEN DEL SISTEMA ==========")
    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas creadas: {len(reservas)}")
    for reserva in reservas:
        print(reserva)


if __name__ == "__main__":
    print("SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    operaciones = [
        ("Registro válido de cliente 1", op1),
        ("Registro válido de cliente 2", op2),
        ("Registro inválido de cliente", op3),
        ("Creación correcta de sala", op4),
        ("Creación correcta de alquiler de equipo", op5),
        ("Creación correcta de asesoría", op6),
        ("Creación incorrecta de servicio", op7),
        ("Reserva exitosa con impuesto", op8),
        ("Reserva exitosa con descuento", op9),
        ("Reserva fallida por servicio no disponible", op10),
    ]

    for numero, (descripcion, funcion) in enumerate(operaciones, start=1):
        ejecutar_operacion(numero, descripcion, funcion)

    mostrar_resumen()
    print("\nEl sistema finalizó sin detenerse por los errores.")
