import matplotlib.pyplot as plt
import numpy as np

# 1. Definición del modelo agrícola
k = 10  # Asignamos un valor constante positivo a k para la simulación gráfica
N = np.linspace(0, 4, 100)
P = np.linspace(0, 4, 100)
N_grid, P_grid = np.meshgrid(N, P)

# Función de rendimiento: Y(N, P) = k * N * P * e^(-N - P)
Y = k * N_grid * P_grid * np.exp(-N_grid - P_grid)

# Punto crítico / Máximo absoluto
N_max, P_max = 1.0, 1.0
Y_max = k * N_max * P_max * np.exp(-N_max - P_max)

# 2. Configuración de la figura en 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")

# Graficar la superficie
surf = ax.plot_surface(
    N_grid, P_grid, Y, cmap="viridis", alpha=0.85, edgecolor="none"
)

# Graficar el punto máximo absoluto
ax.scatter(
    [N_max],
    [P_max],
    [Y_max],
    color="red",
    s=120,
    zorder=5,
    label=f"Máximo Absoluto (N=1, P=1, Y={Y_max:.2f})",
)

# 3. Anotaciones y señales visuales
# Líneas de proyección hacia las coordenadas del máximo
ax.plot([N_max, N_max], [P_max, P_max], [0, Y_max], color="red", linestyle="--")
ax.plot([N_max, N_max], [0, P_max], [0, 0], color="red", linestyle="--")
ax.plot([0, N_max], [P_max, P_max], [0, 0], color="red", linestyle="--")

# Texto explicativo en el gráfico
ax.text(
    N_max,
    P_max,
    Y_max + 0.05,
    "  Máximo Absoluto (1, 1)",
    color="red",
    fontsize=11,
    weight="bold",
)

# 4. Etiquetas y títulos
ax.set_title(
    "Modelo de Rendimiento Agrícola $Y(N, P) = k N P e^{-N-P}$",
    fontsize=14,
    pad=20,
)
ax.set_xlabel("Nivel de Nitrógeno ($N$)", fontsize=11, labelpad=10)
ax.set_ylabel("Nivel de Fósforo ($P$)", fontsize=11, labelpad=10)
ax.set_zlabel("Rendimiento ($Y$)", fontsize=11, labelpad=10)

# Barra de colores para la escala de rendimiento
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label="Rendimiento Y")
ax.legend(loc="upper right")

# Ajuste del ángulo de visión
ax.view_init(elev=25, azim=135)

plt.tight_layout()
plt.show()