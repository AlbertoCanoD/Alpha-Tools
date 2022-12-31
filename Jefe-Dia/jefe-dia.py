import random

# Lista de responsables
responsables = ["Alberto", "Dani.R", "Dani.J", "Mari", "Mario", "Maria.D", "Alex.H",
                "Fernando", "Ema", "Clara", "Natalia", "Almudena", "Espe", "Raquel", "Selene", "Sonia"]

# Introduccion de días de campamento
dias = input("Número de Días del campamento: ")

# Se hace una lista con responsables sin repeticion
eleccion = random.sample(responsables, int(dias))

# Sin repeticion de responsables
for i in range(int(dias)):
    print(f"Dia {i + 1}, Jefe de Día: " + eleccion[i])

# Con repeticion de responsables
'''for i in range(int(dias)):
    print(f"Dia {i + 1}, Jefe de Día: " + random.choice(responsables))
'''
