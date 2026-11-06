<div align="center">

# 🧬 Algoritmos Genéticos

### Introducción · Dinamización · Optimización de rutas

Un laboratorio en Python para explorar cómo evoluciona una población de rutas hasta encontrar soluciones de menor distancia.

**Universidad de los Llanos · Ingeniería de Sistemas · Optimización**

[Parte 1](#parte-1--el-algoritmo-base) · [Parte 2](#parte-2--entrada-dinámica-y-visualización) · [Ejecución](#ejecución) · [Ejemplo](#ejemplo-de-entrada)

</div>

---

## El problema

Una empresa necesita salir de una bodega central, visitar cada ciudad una sola vez y regresar al origen, recorriendo la menor distancia posible. El laboratorio aborda una versión simplificada del **problema del viajante (TSP)** mediante un algoritmo genético.

Cada individuo representa un orden de visita. El origen permanece fijo y se añade al comienzo y al final al calcular la distancia:

```text
Cromosoma:      [B, C, D]
Ruta completa:  A → B → C → D → A
```

Las distancias son simétricas: viajar de A a B tiene el mismo costo que viajar de B a A.

## Dos partes, una misma base

| Característica | Parte 1 | Parte 2 |
| :--- | :--- | :--- |
| Ciudades y distancias | Definidas en el código | Ingresadas por consola |
| Población, generaciones y mutación | Parámetros fijos | Parámetros ingresados por el usuario |
| Seguimiento en consola | Población inicial, padres y generaciones | Población inicial, padres y generaciones |
| Resultado | Mejor ruta de la población final | Mejor ruta de la población final |
| Visualización | — | Mejor distancia y promedio por generación |

### Parte 1 · El algoritmo base

[`Parte1.py`](Parte1.py) sigue el código de ejemplo de la primera guía: conserva sus funciones, operadores genéticos y reemplazo de la población.

| Código | Ciudad |
| :---: | :--- |
| A | Bogotá — origen |
| B | Villavicencio |
| C | Granada |
| D | Acacías |

**Matriz del ejercicio, en kilómetros:**

| Desde / hacia | A | B | C | D |
| :---: | ---: | ---: | ---: | ---: |
| **A** | 0 | 30 | 50 | 40 |
| **B** | 30 | 0 | 25 | 35 |
| **C** | 50 | 25 | 0 | 15 |
| **D** | 40 | 35 | 15 | 0 |

La configuración inicial utiliza **6 individuos**, **10 generaciones** y una **tasa de mutación de 0.2**.

Para esta matriz, una ruta óptima es `A → B → C → D → A`, con **110 km**; su recorrido inverso tiene la misma distancia. Es una referencia para comprobar resultados, no una salida garantizada en cada ejecución.

### Parte 2 · Entrada dinámica y visualización

[`Parte2.py`](Parte2.py) adapta el algoritmo base a los dos requisitos funcionales de la segunda guía:

- **RF1 — Entrada dinámica:** solicita el origen, las ciudades intermedias, la distancia entre cada par y los parámetros del algoritmo.
- **RF2 — Monitoreo:** registra la menor distancia y el promedio de cada generación; al terminar, muestra ambas curvas con título, ejes, cuadrícula y leyenda.

Los códigos de ciudad deben ser únicos y distintos del origen. El programa admite al menos una ciudad intermedia, una población mínima de dos individuos y al menos una generación. La tasa de mutación debe estar entre `0.0` y `1.0`.

## Ejecución

Necesitas **Python 3**, `pip` y, para la Parte 2, **Matplotlib**. Ejecuta la versión gráfica en un entorno de escritorio que permita abrir ventanas.

**1. Clona el repositorio y entra en la carpeta:**

```bash
git clone https://github.com/Santiago17Corredor/Introduccion_y_dinamizacion_Algoritmos_Geneticos.git
cd Introduccion_y_dinamizacion_Algoritmos_Geneticos
```

**2. Instala la dependencia de la Parte 2:**

```bash
python -m pip install matplotlib
```

La Parte 1 utiliza únicamente la biblioteca estándar de Python.

**3. Ejecuta la parte que quieras explorar:**

```bash
python Parte1.py
```

```bash
python Parte2.py
```

En la Parte 2, responde las preguntas de la consola. La gráfica se abre al terminar las generaciones; cierra su ventana para finalizar la ejecución. Utiliza punto para los valores decimales, por ejemplo `0.2`.

## Ejemplo de entrada

Para ejecutar la Parte 2 con los mismos datos de la Parte 1, ingresa estos valores en el orden solicitado:

| Entrada | Valor |
| :--- | :--- |
| Ciudad origen | `A` |
| Número de ciudades a visitar, sin contar el origen | `3` |
| Códigos de las ciudades, uno por pregunta | `B`, `C`, `D` |
| Distancia A–B | `30` |
| Distancia A–C | `50` |
| Distancia A–D | `40` |
| Distancia B–C | `25` |
| Distancia B–D | `35` |
| Distancia C–D | `15` |
| Tamaño de la población | `6` |
| Número de generaciones | `10` |
| Tasa de mutación | `0.2` |

## Cómo evoluciona la población

1. **Crear individuos:** copiar la lista de ciudades y mezclarla con `random.shuffle`.
2. **Evaluar:** sumar las distancias del recorrido completo, incluido el regreso al origen. Menor distancia significa mejor aptitud.
3. **Seleccionar:** ordenar la población por distancia y elegir los dos mejores individuos.
4. **Cruzar:** conservar un prefijo del primer padre y completar el hijo con las ciudades del segundo, sin repetirlas.
5. **Mutar:** según la tasa indicada, elegir dos índices aleatorios e intercambiar sus posiciones. Los índices pueden coincidir; en ese caso, la ruta no cambia.
6. **Reemplazar:** formar una población nueva únicamente con los hijos y repetir hasta completar las generaciones.

> **Comportamiento del ejemplo:** no se conservan padres por elitismo. La mejor distancia puede aumentar entre generaciones y el resultado impreso corresponde a la mejor ruta de la última población, no al mejor individuo de toda la ejecución. Los resultados pueden variar porque el algoritmo utiliza aleatoriedad y no fija una semilla.

## Cómo leer la gráfica

| Curva | Qué representa |
| :--- | :--- |
| **Mejor solución** | Menor distancia de la población en cada generación. |
| **Promedio de la población** | Media de las distancias de todos los individuos de esa generación. |

Una reducción indica rutas más cortas. Una brecha pequeña indica distancias similares entre individuos, aunque sus rutas pueden ser diferentes. Una curva estable, por sí sola, no demuestra que se haya alcanzado el óptimo global.

## Estructura

```text
Introduccion_y_dinamizacion_Algoritmos_Geneticos/
├── Parte1.py    # Implementación base con datos fijos
├── Parte2.py    # Entrada interactiva y gráfica de evolución
└── README.md    # Descripción y guía de ejecución
```

## Material del laboratorio

- [Guía de la Parte 1: fundamentos y código base](https://drive.google.com/file/d/1DPygCdY0ttAwvtu81P-rExdGsWhzQ1bk/view)
- [Guía de la Parte 2: dinamización y monitoreo](https://drive.google.com/file/d/19gHmHFYh5FtsjeQQo0aS3eh2T4gKrFmR/view)

La Parte 1 reproduce la lógica del ejemplo de la guía. La Parte 2 mantiene esa base y añade las entradas y la visualización solicitadas; su guía especifica requisitos, no un segundo programa para transcribir.
