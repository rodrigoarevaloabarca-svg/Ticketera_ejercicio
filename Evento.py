
class Evento:
    tasa_servicio = 0.1

    def __init__(self, nombre_artista):
        self.nombre_artista = nombre_artista
        self.lista_sectores = []

    def agregar_sector(self, sector):
        self.lista_sectores.append(sector)
        print(f"✅Sector {sector.sector} agregado correctamente")

    @classmethod
    def cambiar_tasa(cls, tasa):
        cls.tasa_servicio = tasa
        print(f"✅Tasa de servicio cambiada a {cls.tasa_servicio}")

    def mostrar_disponibilidad(self):
        if not self.lista_sectores:
            print("❌No hay sectores registrados aun")
            return
        for sector in self.lista_sectores:
            print(sector)