import re


def filter(fleetName, workSheet):
    pass
    
# Lista de componentes de motor
components = [
    "RADIADOR",
    "TRANSMISION",
    "CONVERTIDOR",
    "DIFERENCIAL",
    "MANDO FINAL DERECHO",
    "MANDO FINAL IZQUIERDO",
    "SUSPENSION FRONTAL DERECHA",
    "SUSPENSION FRONTAL IZQUIERDA",
    "CILINDRO DE LEVANTE DERECHO",
    "CILINDRO DE LEVANTE IZQUIERDO"
]

# Patrón de expresión regular para buscar las palabras "cambio" o "cambiar"
pattern = r"(cambio|cambiar)"

# Patrón de expresión regular para buscar las frases exactas para el componente "MOTOR"
motor_pattern_exact = ("CAMBIO DE MOTOR","CAMBIO MOTOR","CAMBIAR MOTOR","CAMBIO DE MOTOR DIESEL", "CAMBIO DE MOTOR BASICO","CAMBIO MOTOR BASICO", "CAMBIAR MOTOR DIESEL","CAMBIAR MOTOR BASICO")

# Crear una expresión regular para cada componente de motor
component_patterns = [re.compile(f"{pattern} ?(?:de )?{component}", re.IGNORECASE) for component in components]

# Lista de cadenas para buscar las coincidencias


# Buscar las coincidencias en cada cadena
# for string in strings:
#     for component_pattern in component_patterns:
#         if("MOTOR" in string or "motor" in string):
#             if(string.upper() in motor_pattern_exact):
#                 print(f"Se encontró una coincidencia para la cadena {string}")
#                 break
#         elif component_pattern.search(string):
#             print(f"Se encontró una coincidencia para la cadena '{string}': {component_pattern.pattern}")
#             break
