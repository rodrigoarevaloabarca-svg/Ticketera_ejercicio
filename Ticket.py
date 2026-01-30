import secrets
import string

class Ticket:
    def __init__(self, nombre_comprador, rut, sector,cant_entradas):
        self.nombre_comprador = nombre_comprador
        self.rut = rut
        self.sector = sector
        self.cant_entradas = cant_entradas
        self.__token = self.__generar_token_seguridad()#composicion

    def __generar_token_seguridad(self):

        caracteres = string.ascii_uppercase + string.digits
        bloque1 = ''.join(secrets.choice(caracteres) for _ in range(3))
        bloque2 = ''.join(secrets.choice(string.digits) for _ in range(3))
        bloque3 = ''.join(secrets.choice(caracteres) for _ in range(2))

        return f"{bloque1}-{bloque2}-{bloque3}"

    def __str__(self):
        return (

            f" 🎫  **TICKET DIGITAL** 🎫 \n"
            f"  *MEGACONCIERTOS OFICIAL* \n"
            f"{'─' * 35}\n"
            f" 👤 **CLIENTE:** {self.nombre_comprador}\n"
            f" 🆔 **RUT:** {self.rut}\n"
            f" 📍 **SECTOR:** {self.sector}\n"
            f" 🎫 **CANT. ENTRADAS:** {self.cant_entradas}\n"
            f" 🔑 **CODIGO:** {self.__token}\n"
            f"{'─' * 35}\n"
            f"      ¡Disfruta el show! 🎸\n"

        )