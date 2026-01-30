Ticketera Ejercicio 🎟️
Sistema de gestión de tickets desarrollado en Python bajo el paradigma de Programación Orientada a Objetos (POO). Este proyecto permite administrar de forma integral la venta de entradas para eventos, gestionando capacidades, precios y datos de clientes.

📁 Estructura del Proyecto
El código se organiza en módulos independientes para facilitar su mantenimiento:

App_Ticketera.py: Script principal que ejecuta la lógica de la aplicación y la interfaz de usuario.

Evento.py: Clase para definir el espectáculo (nombre, fecha y descripción).

Sector.py: Gestión de las áreas del recinto, permitiendo establecer precios y cupos máximos por zona.

Clientes.py: Módulo encargado de almacenar y gestionar la información de los compradores.

Ticket.py: Clase que representa la entrada final, vinculando un cliente con un sector y evento específicos.

🚀 Funcionalidades
1. Administración de Eventos y Sectores
El sistema permite segmentar un evento en diferentes sectores (por ejemplo: VIP, Platea, General), cada uno con su propio stock de entradas y valor monetario.

2. Control de Disponibilidad
Valida automáticamente si quedan asientos disponibles en un sector antes de confirmar la venta, evitando la sobreventa de entradas.

3. Registro y Asociación
Asocia cada ticket emitido a un cliente registrado, permitiendo llevar un control de quién adquirió cada ubicación.

4. Persistencia de Configuración
Incluye archivos de configuración para entornos de desarrollo como PyCharm y control de versiones mediante Git.

🛠️ Requisitos e Instalación
Lenguaje: Python 3.10 o superior.

Instalación: Descarga el repositorio y asegúrate de mantener la estructura de carpetas actual.

Ejecución:

Bash
python App_Ticketera.py
📝 Notas de Versión
v1.0: Implementación de clases base y lógica de venta.

Iconografía: Se han agregado iconos para mejorar la experiencia visual en la interfaz.