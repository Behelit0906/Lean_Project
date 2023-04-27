import re

motor_pattern_exact = re.compile(r"\b(cambio de motor)\b", re.IGNORECASE)


cadena = "Cambio de motor de levante"
lista = ("CAMBIO DE MOTOR","CAMBIO MOTOR","CAMBIAR MOTOR","CAMBIO DE MOTOR DIESEL", "CAMBIO DE MOTOR BASICO","CAMBIO MOTOR BASICO", "CAMBIAR MOTOR DIESEL","CAMBIAR MOTOR BASICO")

print("cambiar motor" in lista)
