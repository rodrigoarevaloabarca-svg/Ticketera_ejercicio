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
        if cantidad < self.__stock_actual:
            self.__stock_actual -= cantidad
            return True
        else:
            return False
    #getters
    def __str__(self):
        return f"Sector: {self.sector} | Precio: {self.precio_base} | Ticket Disponibles: {self.__stock_actual}"
