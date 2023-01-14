import random
from datetime import datetime as dt


def fecha_entrega():
    # Hora y fecha actual
    hora_fecha_actual = dt.now()

    # Hora actual formateada en HORAS:MINUTOS
    hora_actual = dt.now().time().strftime('%H:%M')

    # Se añade un día al plazo de entrega
    dia_entrega = hora_fecha_actual.day + 1
    mes_anio_entrega = str(hora_fecha_actual.month) + "-" + str(hora_fecha_actual.year)
    entrega = "Tenéis hasta --> " + str(dia_entrega) + "-" + mes_anio_entrega + " " + str(hora_actual)
    return entrega

# Lista de ramas
ramas = ["LOBATOS", "TROPA", "PIONEROS", "RUTAS"]

# Se elige la rama aleatoriamente desde la lista de ramas
print(f"El Kraal de " + random.choice(ramas) + " debe hacer el BeReal semanal")
print("QUEDAN 24 HORAS, TIC TAC TIC TAC TIC TAC")
print(fecha_entrega())
