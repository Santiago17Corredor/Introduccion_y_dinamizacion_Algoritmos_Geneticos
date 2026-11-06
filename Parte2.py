import random
from itertools import combinations

import matplotlib.pyplot as plt

# Entrada por consola.
def pedir_entero(mensaje, minimo):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:
                return valor
        except ValueError:
            pass
        print(f"Ingrese un entero mayor o igual a {minimo}.")


def pedir_decimal(mensaje, minimo, maximo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo <= valor and (maximo is None or valor <= maximo):
                return valor
        except ValueError:
            pass
        print(f"Ingrese un número entre {minimo} y {maximo if maximo is not None else 'infinito'}.")


origen = input("Código de la ciudad origen: ").strip()
while not origen:
    origen = input("Ingrese un código para la ciudad origen: ").strip()

cantidad = pedir_entero("Número de ciudades a visitar: ", 1)
ciudades = []
while len(ciudades) < cantidad:
    ciudad = input(f"Código de la ciudad {len(ciudades) + 1}: ").strip()
    if ciudad and ciudad not in ciudades and ciudad != origen:
        ciudades.append(ciudad)
    else:
        print("El código debe ser único y diferente del origen.")

distancias = {}
for a, b in combinations([origen, *ciudades], 2):
    distancias[(a, b)] = pedir_decimal(f"Distancia {a}-{b} (km): ", 0)

TAM_POBLACION = pedir_entero("Tamaño de la población: ", 2)
GENERACIONES = pedir_entero("Número de generaciones: ", 1)
TASA_MUTACION = pedir_decimal("Tasa de mutación (0 a 1): ", 0, 1)

# Distancia simétrica.
def obtener_distancia(ciudad1, ciudad2):
    if ciudad1 == ciudad2:
        return 0
    if (ciudad1, ciudad2) in distancias:
        return distancias[(ciudad1, ciudad2)]
    return distancias[(ciudad2, ciudad1)]

# Orden de visita aleatorio.
def crear_individuo():
    ruta = ciudades[:]
    random.shuffle(ruta)
    return ruta

def crear_poblacion():
    poblacion = []
    for _ in range(TAM_POBLACION):
        poblacion.append(crear_individuo())
    return poblacion

# Distancia total, incluido el regreso.
def calcular_distancia(ruta):
    ruta_completa = [origen] + ruta + [origen]
    distancia_total = 0
    for i in range(len(ruta_completa) - 1):
        distancia_total += obtener_distancia(
            ruta_completa[i],
            ruta_completa[i + 1]
        )
    return distancia_total

def seleccionar_padres(poblacion):
    poblacion_ordenada = sorted(
        poblacion,
        key=lambda x: calcular_distancia(x)
    )
    return poblacion_ordenada[:2]

# Combina rutas sin repetir ciudades.
def cruce(padre1, padre2):
    # Una ciudad no admite corte.
    if len(padre1) < 2:
        return padre1[:]
    punto = random.randint(1, len(padre1) - 1)
    hijo = padre1[:punto]
    for ciudad in padre2:
        if ciudad not in hijo:
            hijo.append(ciudad)
    return hijo

def mutacion(individuo):
    if random.random() < TASA_MUTACION:
        i = random.randint(0, len(individuo) - 1)
        j = random.randint(0, len(individuo) - 1)
        individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo

def algoritmo_genetico():
    poblacion = crear_poblacion()
    mejores = []
    promedios = []
    print("\nPOBLACIÓN INICIAL\n")
    for individuo in poblacion:
        print(
            [origen] + individuo + [origen],
            "Distancia:",
            calcular_distancia(individuo)
        )

    for generacion in range(GENERACIONES):
        print("\n==============================")
        print(f"GENERACIÓN {generacion + 1}")
        print("==============================")
        padre1, padre2 = seleccionar_padres(poblacion)
        print("\nMEJORES PADRES:")
        print("Padre 1:", [origen] + padre1 + [origen])
        print("Padre 2:", [origen] + padre2 + [origen])
        nueva_poblacion = []
        # Reemplazo sin elitismo.
        while len(nueva_poblacion) < TAM_POBLACION:
            hijo = cruce(padre1, padre2)
            hijo = mutacion(hijo)
            nueva_poblacion.append(hijo)
        poblacion = nueva_poblacion

        # Mínimo y promedio por generación.
        valores = [calcular_distancia(individuo) for individuo in poblacion]
        mejores.append(min(valores))
        promedios.append(sum(valores) / len(valores))

        for individuo in poblacion:
            print(
                [origen] + individuo + [origen],
                "Distancia:",
                calcular_distancia(individuo)
            )

    # Mejor ruta de la última generación.
    mejor = min(
        poblacion,
        key=lambda x: calcular_distancia(x)
    )
    print("\n===================================")
    print("MEJOR RUTA ENCONTRADA")
    print("===================================")
    print(
        "Ruta:",
        [origen] + mejor + [origen]
    )
    print(
        "Distancia total:",
        calcular_distancia(mejor),
        "km"
    )

    # Curvas de distancia.
    eje_x = range(1, GENERACIONES + 1)
    plt.plot(eje_x, mejores, label="Mejor solución")
    plt.plot(eje_x, promedios, label="Promedio de la población")
    plt.title("Evolución del algoritmo genético")
    plt.xlabel("Generaciones")
    plt.ylabel("Distancia (km)")
    plt.grid(True)
    plt.legend()
    plt.show()

algoritmo_genetico()

