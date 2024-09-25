import numpy as np
import matplotlib.pyplot as plt

# Constante de gravedad (m/s^2)
g_tierra = 9.8
g_luna = 1.62

# Función para calcular la posición en función del tiempo (caída libre)
def posicion(t, y0, g):
    return y0 - 0.5 * g * t**2

# Función para calcular la velocidad en función del tiempo (caída libre)
def velocidad(t, g):
    return -g * t

# Tiempo máximo de vuelo en función de la altura inicial
def tiempo_vuelo(y0, g):
    return np.sqrt(2 * y0 / g)

# Función para simular caída libre en la Tierra o en la Luna
def simulacion_caida_libre(y0, g, planeta="Tierra"):
    # Tiempo de vuelo hasta que la partícula llegue al suelo
    t_vuelo = tiempo_vuelo(y0, g)

    # Generar un array de tiempos
    tiempos = np.linspace(0, t_vuelo, num=500)

    # Calcular posiciones y velocidades
    posiciones = posicion(tiempos, y0, g)
    velocidades = velocidad(tiempos, g)

    # Gráficos
    plt.figure(figsize=(10, 5))

    # Posición vs Tiempo
    plt.subplot(1, 2, 1)
    plt.plot(tiempos, posiciones)
    plt.title(f"Posición vs Tiempo ({planeta})")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Posición (m)")

    # Velocidad vs Tiempo
    plt.subplot(1, 2, 2)
    plt.plot(tiempos, velocidades)
    plt.title(f"Velocidad vs Tiempo ({planeta})")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Velocidad (m/s)")

    plt.tight_layout()
    plt.show()

# Función para lanzar una partícula hacia arriba
def simulacion_lanzamiento_arriba(v0, g):
    # Tiempo hasta alcanzar la altura máxima
    t_subida = v0 / g

    # Altura máxima
    altura_maxima = v0 * t_subida - 0.5 * g * t_subida**2

    # Tiempo total de vuelo (doble del tiempo de subida)
    t_total_vuelo = 2 * t_subida

    print(f"Altura máxima alcanzada: {altura_maxima:.2f} metros")
    print(f"Tiempo total de vuelo: {t_total_vuelo:.2f} segundos")

    # Generar un array de tiempos hasta que regrese al suelo
    tiempos = np.linspace(0, t_total_vuelo, num=500)

    # Calcular posiciones y velocidades para el lanzamiento hacia arriba
    posiciones = v0 * tiempos - 0.5 * g * tiempos**2
    velocidades = v0 - g * tiempos

    # Gráficos
    plt.figure(figsize=(10, 5))

    # Posición vs Tiempo
    plt.subplot(1, 2, 1)
    plt.plot(tiempos, posiciones)
    plt.title("Posición vs Tiempo (lanzamiento hacia arriba)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Posición (m)")

    # Velocidad vs Tiempo
    plt.subplot(1, 2, 2)
    plt.plot(tiempos, velocidades)
    plt.title("Velocidad vs Tiempo (lanzamiento hacia arriba)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Velocidad (m/s)")

    plt.tight_layout()
    plt.show()

# Simulación de caída libre en la Tierra
y0 = float(input("Ingrese la altura inicial de la caída libre (metros): "))
simulacion_caida_libre(y0, g_tierra, "Tierra")

# Simulación de caída libre en la Luna
simulacion_caida_libre(y0, g_luna, "Luna")

# Lanzamiento hacia arriba con rapidez de 2 m/s en la Tierra
v0 = 2.0
simulacion_lanzamiento_arriba(v0, g_tierra)
