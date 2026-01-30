class Sector:
    def __init__(self, sector, precio_base, stock_actual):
        self.sector = sector
        self.precio_base = precio_base
        self.__stock_actual = stock_actual
    #getters
    def stock_actual(self):
        return self.__stock_actual
    # Setter?
    def vender_entrada(self, cantidad):
        if 0 < cantidad <= self.__stock_actual:
            self.__stock_actual -= cantidad
            return True
        else:
            print(f"¡Error! No hay suficiente stock en {self.sector}.")
            return False
    #getters
    def __str__(self):
        return f"Sector: {self.sector} |"\
               f"Precio: ${self.precio_base} |"\
               f"Ticket Disponibles: {self.__stock_actual}"
