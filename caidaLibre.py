import numpy as np
import matplotlib.pyplot as plt

# Constantes gravitacionales (m/s^2)
gravedad_tierra = 9.8
gravedad_luna = 1.62

# Función para calcular la altura en función del tiempo (caída libre)
def calcular_altura(t, altura_inicial, gravedad):
    return altura_inicial - 0.5 * gravedad * t**2

# Función para calcular la velocidad en función del tiempo (caída libre)
def calcular_velocidad(t, gravedad):
    return -gravedad * t

# Función para determinar la altura inicial a partir del tiempo total de vuelo
def obtener_altura_por_tiempo(tiempo_total, gravedad):
    return 0.5 * gravedad * tiempo_total**2

# Función para calcular altura y velocidad en un instante dado
def obtener_datos_instante(t, altura_inicial, gravedad):
    altura = calcular_altura(t, altura_inicial, gravedad)
    velocidad = calcular_velocidad(t, gravedad)
    return altura, velocidad

# Función para simular caída libre en un planeta
def simular_caida_libre(altura_inicial, gravedad, nombre_planeta="Tierra"):
    # Tiempo hasta que toca el suelo
    tiempo_caida = np.sqrt(2 * altura_inicial / gravedad)
    # Generar un array de tiempos
    tiempos = np.linspace(0, tiempo_caida, num=500)
    # Calcular alturas y velocidades
    alturas = calcular_altura(tiempos, altura_inicial, gravedad)
    velocidades = calcular_velocidad(tiempos, gravedad)

    # Gráficos
    plt.figure(figsize=(10, 5))
    # Altura vs Tiempo
    plt.subplot(1, 2, 1)
    plt.plot(tiempos, alturas)
    plt.title(f"Altura vs Tiempo ({nombre_planeta})")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Altura (m)")
    # Velocidad vs Tiempo
    plt.subplot(1, 2, 2)
    plt.plot(tiempos, velocidades)
    plt.title(f"Velocidad vs Tiempo ({nombre_planeta})")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Velocidad (m/s)")
    plt.tight_layout()
    plt.show()

# Función para simular un lanzamiento vertical
def simular_lanzamiento_vertical(velocidad_inicial, gravedad):
    # Tiempo hasta la altura máxima
    tiempo_subida = velocidad_inicial / gravedad
    # Altura máxima
    altura_maxima = velocidad_inicial * tiempo_subida - 0.5 * gravedad * tiempo_subida**2
    # Tiempo total de vuelo
    tiempo_total = 2 * tiempo_subida

    print(f"Altura máxima alcanzada: {altura_maxima:.2f} metros")
    print(f"Tiempo total de vuelo: {tiempo_total:.2f} segundos")

    # Generar un array de tiempos
    tiempos = np.linspace(0, tiempo_total, num=500)
    # Calcular alturas y velocidades
    alturas = velocidad_inicial * tiempos - 0.5 * gravedad * tiempos**2
    velocidades = velocidad_inicial - gravedad * tiempos

    # Gráficos
    plt.figure(figsize=(10, 5))
    # Altura vs Tiempo
    plt.subplot(1, 2, 1)
    plt.plot(tiempos, alturas)
    plt.title("Altura vs Tiempo (lanzamiento vertical)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Altura (m)")
    # Velocidad vs Tiempo
    plt.subplot(1, 2, 2)
    plt.plot(tiempos, velocidades)
    plt.title("Velocidad vs Tiempo (lanzamiento vertical)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Velocidad (m/s)")
    plt.tight_layout()
    plt.show()

# Solicitar tiempo de vuelo y calcular la altura inicial
tiempo_vuelo_usuario = float(input("Ingrese el tiempo total de vuelo (en segundos): "))
altura_inicial_calculada = obtener_altura_por_tiempo(tiempo_vuelo_usuario, gravedad_tierra)
print(f"Altura calculada para un tiempo de vuelo de {tiempo_vuelo_usuario} segundos en la Tierra: {altura_inicial_calculada:.2f} metros")

# Calcular datos para un instante específico
instante_usuario = float(input("Ingrese un instante para calcular altura y velocidad (en segundos): "))
altura_en_instante, velocidad_en_instante = obtener_datos_instante(
    instante_usuario, altura_inicial_calculada, gravedad_tierra
)
print(f"Altura en t={instante_usuario} segundos: {altura_en_instante:.2f} metros")
print(f"Velocidad en t={instante_usuario} segundos: {velocidad_en_instante:.2f} m/s")

# Simular caída libre en la Tierra
simular_caida_libre(altura_inicial_calculada, gravedad_tierra, "Tierra")

# Simular caída libre en la Luna
simular_caida_libre(altura_inicial_calculada, gravedad_luna, "Luna")

# Simular un lanzamiento vertical con una velocidad inicial de 2 m/s
velocidad_inicial = 2.0
simular_lanzamiento_vertical(velocidad_inicial, gravedad_tierra)
