from Evento import *
from Clientes import *
from Sector import *
from Ticket import *

def menu():
    print(f"\n{'=' * 35}")
    print(" 🎫 TICKET OFICIAL-MEGACONCIERTOS 🎸")
    print(f"{'=' * 35}")
    print(" 1️⃣  Crear Sectores")
    print(" 2️⃣  Vender Entrada")
    print(" 3️⃣  Ver Estado del Estadio 🏟️")
    print(" 4️⃣  Ajustar Comisiones 💸")
    print(" 5️⃣  Salir 🚪")
    print(f"{'=' * 35}")
    return input("\n👉 Seleccione una opción: ")


def principal():
    evento = input("Ingrese el nombre del evento:").upper()
    evento_actual = Evento(evento)

    while True:
        print(f"\n Bienvenido al Concierto de {evento}!")
        opcion = menu()

        match opcion:
            case "1":
                print("\n--- 🛠️ CONFIGURACIÓN DE SECTOR ---")
                nombre_sector = input("📍 Nombre del sector: ").upper()
                precio = int(input("💵 Precio base: "))
                stock = int(input("📦 Stock inicial: "))
                nuevo_sector = Sector(nombre_sector, precio, stock)
                evento_actual.agregar_sector(nuevo_sector)
                print(f"✅ Sector '{nombre_sector}' configurado exitosamente.")

            case "2":
                if not evento_actual.lista_sectores:
                    print("❌ Error: Primero debe configurar sectores en la opción 1.")
                    continue

                print("\n--- 🛒 PROCESO DE VENTA ---")
                rut = input("🆔 Ingrese RUT del cliente: ")
                if not Validador.validar_rut(rut):
                    print("🚫 RUT inválido. Venta cancelada.")
                    continue

                edad = int(input("🎂 Edad del cliente: "))
                if not Validador.es_mayor_edad(edad):
                    print("🔞 El cliente debe ser mayor de edad para comprar.")
                    continue

                print("\n📍 Sectores Disponibles:")
                for i, s in enumerate(evento_actual.lista_sectores):
                    print(f"   [{i}] {s.sector} - ${s.precio_base:,.0f}")

                try:
                    eleccion = int(input("\n🔢 Seleccione el número de sector: "))
                    sector_elegido = evento_actual.lista_sectores[eleccion]
                except (ValueError, IndexError):
                    print("⚠️ Selección no válida.")
                    continue

                cant_entradas = int(input("ingrese cantidad de entradas( 4 Maximo):"))
                if cant_entradas > 4:
                    print("⚠️Excedes el maximo de entradas permitidas (4 por Rut)⚠️")
                    continue
                else:
                    if sector_elegido.vender_entrada(cant_entradas):
                        total = Validador.calcular_total_con_servicio(
                            sector_elegido.precio_base, Evento.tasa_servicio)

                        nombre_comprador = input("👤 Nombre del comprador: ")
                        nuevo_ticket = Ticket(nombre_comprador, rut, sector_elegido.sector, cant_entradas)

                        print(nuevo_ticket)
                        print(f"💰 TOTAL A COBRAR : ${total * cant_entradas:,.0f}")

                    else:
                        print("📉 Lo sentimos, no queda stock en este sector.")

            case "3":
                print("\n--- 🏟️ ESTADO DE DISPONIBILIDAD ---")
                evento_actual.mostrar_disponibilidad()

            case "4":
                print(f"\n📊 Tasa de servicio actual: {Evento.tasa_servicio * 100}%")
                try:
                    nueva_tasa = float(input("📈 Ingrese nueva tasa (ej. 0.15 para 15%): "))
                    Evento.cambiar_tasa(nueva_tasa)
                    print(f"✅ Tasa actualizada al {nueva_tasa * 100}%")
                except ValueError:
                    print("⚠️ Ingrese un valor numérico válido.")

            case "5":
                print("\n👋 Saliendo del sistema... ¡Gracias por preferirnos!")
                break

            case _:
                print("\n⚠️ Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    principal()