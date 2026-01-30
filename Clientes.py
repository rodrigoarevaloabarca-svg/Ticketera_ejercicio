import re
from itertools import cycle


class Validador:

    @staticmethod
    def validar_rut(rut):
        rut = rut.upper().replace(".", "").replace("-", "")
        if not re.match(r"^\d{7,8}[0-9K]$", rut):
            return False

        # 2. Separar el cuerpo del dígito verificador (DV)
        cuerpo = rut[:-1]
        dv_entregado = rut[-1]

        # 3. ALGORITMO MÓDULO 11
        # Multiplicamos los dígitos de atrás hacia adelante por la serie 2,3,4,5,6,7
        serie = cycle([2, 3, 4, 5, 6, 7])
        suma = sum(int(d) * next(serie) for d in reversed(cuerpo))

        # 4. Cálculo del dígito esperado
        resto = suma % 11
        dv_esperado = str(11 - resto)

        if dv_esperado == "11":
            dv_esperado = "0"
        elif dv_esperado == "10":
            dv_esperado = "K"

        # 5. Comparación final
        return dv_entregado == dv_esperado

    @staticmethod
    def es_mayor_edad(edad):
        return edad >= 18

    @staticmethod
    def calcular_total_con_servicio(precio_base, tasa_servicio):
        total = precio_base + (precio_base * tasa_servicio)
        return total
