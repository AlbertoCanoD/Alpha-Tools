import random

# Lista de responsables
responsables = ["Alberto", "Dani.R", "Dani.J", "Mari", "Mario", "Maria.D", "Alex.H",
                "Fernando", "Ema", "Clara", "Natalia", "Almudena", "Espe", "Raquel", "Selene", "Sonia"]

# Introduccion de días de campamento, sólo se pueden introducir números
while True:
    try:
        dias = int(input("Número de Días del campamento: "))
        break
    except ValueError:
        print("¡¡Se debe introducir un número!!")

# Si se puede emparejar cada respon a un día
if len(responsables) > dias:

    # Se hace una lista con responsables sin repeticion
    eleccion_sin_repeticion = random.sample(responsables, dias)

    # Se itera para cada día
    for i in range(int(dias)):
        # Sin repeticion de responsables
        print(f"Dia {i + 1}, Jefe de Día: " + eleccion_sin_repeticion[i])

# Si hay más días que responsables
else:
    for i in range(int(dias)):
        # Con repeticion de responsables
        print(f"Dia {i + 1}, Jefe de Día: " + random.choice(responsables))
