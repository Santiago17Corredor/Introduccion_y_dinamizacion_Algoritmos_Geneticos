import random

# Distancias en km.
distancias = {
    ('A', 'B'): 30,
    ('A', 'C'): 50,
    ('A', 'D'): 40,
    ('B', 'C'): 25,
    ('B', 'D'): 35,
    ('C', 'D'): 15
}

# Distancia simétrica.
def obtener_distancia(ciudad1, ciudad2):
    if ciudad1 == ciudad2:
        return 0
    if (ciudad1, ciudad2) in distancias:
        return distancias[(ciudad1, ciudad2)]
    return distancias[(ciudad2, ciudad1)]

# Parámetros del algoritmo.
ciudades = ['B', 'C', 'D']
TAM_POBLACION = 6
GENERACIONES = 10
TASA_MUTACION = 0.2

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
    ruta_completa = ['A'] + ruta + ['A']
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
    print("\nPOBLACIÓN INICIAL\n")
    for individuo in poblacion:
        print(
            ['A'] + individuo + ['A'],
            "Distancia:",
            calcular_distancia(individuo)
        )

    for generacion in range(GENERACIONES):
        print("\n==============================")
        print(f"GENERACIÓN {generacion + 1}")
        print("==============================")
        padre1, padre2 = seleccionar_padres(poblacion)
        print("\nMEJORES PADRES:")
        print("Padre 1:", ['A'] + padre1 + ['A'])
        print("Padre 2:", ['A'] + padre2 + ['A'])
        nueva_poblacion = []
        # Reemplazo sin elitismo.
        while len(nueva_poblacion) < TAM_POBLACION:
            hijo = cruce(padre1, padre2)
            hijo = mutacion(hijo)
            nueva_poblacion.append(hijo)
        poblacion = nueva_poblacion
        for individuo in poblacion:
            print(
                ['A'] + individuo + ['A'],
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
        ['A'] + mejor + ['A']
    )
    print(
        "Distancia total:",
        calcular_distancia(mejor),
        "km"
    )

algoritmo_genetico()

