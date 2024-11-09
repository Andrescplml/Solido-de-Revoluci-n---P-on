import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir las funciones por tramos
def funcion(x):
    if np.isscalar(x):
        if 0 <= x <= 0.57:
            return -3.82 * x**2 + 4.96 * x
        elif 0.57 <= x <= 2.18:
            return -0.37 * x**2 + 1.58 * x + 0.81
        elif 2.18 <= x <= 3.24:
            return -0.13 * x**2 + 0.6 * x + 1.82
        elif 3.23 <= x <= 3.9:
            return -0.25 * x**2 + 1.25 * x + 0.94
        elif 3.9 <= x <= 4.28:
            return -0.99 * x + 5.89
        elif 4.28 <= x <= 4.59:
            return -0.86 * x**2 + 10.58 * x - 27.86
        elif 4.59 <= x <= 5.71:
            return -3.17 * x**2 + 31.65 * x - 75.91
        elif 5.69 <= x <= 6.01:
            return 0.04 * x + 1.25
        elif 6.01 <= x <= 7.17:
            return 0.1 * x + 0.89
        elif 7.17 <= x <= 8.27:
            return 0.19 * x + 0.25
        elif 8.27 <= x <= 8.94:
            return 0.28 * x - 0.53
        elif 8.94 <= x <= 9.67:
            return 0.36 * x - 1.23
        elif 9.67 <= x <= 9.93:
            return -0.36 * x**2 + 7.6 * x - 37.58
        elif 9.93 <= x <= 10.03:
            return 0.23 * x + 0.18
        elif 10.03 <= x <= 10.15:
            return -14.31 * x**2 + 290.88 * x - 1475.51
        elif 10.15 <= x <= 10.63:
            return -1.97 * x**2 + 40.87 * x - 209.16
        elif 10.63 <= x <= 10.74:
            return -15.69 * x**2 + 338.04 * x - 1817.81
        elif 10.74 <= x <= 10.94:
            return -3.45 * x**2 + 75.7 * x - 412.16
        elif 10.94 <= x <= 11.37:
            return -0.33 * x**2 + 7.92 * x - 44
        elif 11.37 <= x <= 11.61:
            return -0.58 * x**2 + 13.96 * x - 80.34
        elif 11.61 <= x <= 12:
            return 0.88 * x**2 - 19.99 * x + 117
        elif 12 <= x <= 12.22:
            return 0.67 * x**2 - 15.09 * x + 88.35
        elif 12.22 <= x <= 12.37:
            return -0.92 * x**2 + 23.37 * x - 144.17
        elif 12.37 <= x <= 12.67:
            return 0.49 * x - 1.86
        elif 12.67 <= x <= 12.94:
            return -0.99 * x**2 + 25.56 * x - 160.59
        elif 12.94 <= x <= 13.26:
            return -0.37 * x**2 + 9.57 * x - 57.51
        elif 13.26 <= x <= 13.68:
            return -0.76 * x**2 + 19.69 * x - 123.09
        elif 13.68 <= x <= 13.7:
            return 7.25 * x - 95.2
        elif 13.7 <= x <= 13.85:
            return -4.46 * x**2 + 124.77 * x - 868.16
        elif 13.85 <= x <= 14.04:
            return -2.24 * x**2 + 63.53 * x - 445.73
        elif 14.04 <= x <= 14.37:
            return -0.78 * x**2 + 22.67 * x - 159.88
        elif 14.37 <= x <= 14.61:
            return -1.37 * x**2 + 39.59 * x - 281.21
        elif 14.61 <= x <= 14.98:
            return -6.12 * x**2 + 178.55 * x - 1297.57
        elif 14.97 <= x <= 15.03:
            return 25.99 * x**2 - 786.21 * x + 5949
        elif 15.03 <= x <= 15.16:
            return -10.75 * x + 164.99
        elif 15.16 <= x <= 15.19:
            return -61 * x + 926.56
        else:
            return np.nan  # Fuera de los límites
    else:
        return np.array([funcion(xi) for xi in x])  # Para arreglos

# Crear listas para almacenar x e y por tramos
x_vals = []
y_vals = []

# Definir los intervalos de las funciones para asegurarnos de que se concatenen correctamente
intervalos = [
    (0, 0.57), (0.57, 2.18), (2.18, 3.24), (3.23, 3.9), (3.9, 4.28), 
    (4.28, 4.59), (4.59, 5.71), (5.69, 6.01), (6.01, 7.17), (7.17, 8.27),
    (8.27, 8.94), (8.94, 9.67), (9.67, 9.93), (9.93, 10.03), (10.03, 10.15),
    (10.15, 10.63), (10.63, 10.74), (10.74, 10.94), (10.94, 11.37),
    (11.37, 11.61), (11.61, 12), (12, 12.22), (12.22, 12.37), (12.37, 12.67),
    (12.67, 12.94), (12.94, 13.26), (13.26, 13.68), (13.68, 13.7),
    (13.7, 13.85), (13.85, 14.04), (14.04, 14.37), (14.37, 14.61),
    (14.61, 14.98), (14.97, 15.03), (15.03, 15.16), (15.16, 15.19)
]

# Generar los valores de x e y para cada intervalo
for intervalo in intervalos:
    x_tramo = np.linspace(intervalo[0], intervalo[1], 100)
    y_tramo = funcion(x_tramo)
    x_vals.append(x_tramo)
    y_vals.append(y_tramo)

# Concatenar todos los tramos
x_total = np.concatenate(x_vals)
y_total = np.concatenate(y_vals)

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la función original
ax.plot(x_total, y_total, np.zeros_like(x_total), 'b-')

# Crear la malla de revolución sobre el eje X
theta = np.linspace(0, 2 * np.pi, 100)
theta_grid, y_grid = np.meshgrid(theta, y_total)

# Rotación sobre el eje X
x_grid = np.tile(x_total, (100, 1)).T  # Repetir x_total
z_grid = y_grid * np.sin(theta_grid)
y_grid = y_grid * np.cos(theta_grid)

# Graficar la superficie de revolución
ax.plot_surface(x_grid, y_grid, z_grid, color='b', alpha=0.5)

# Ajustar los ejes para mejorar la visualización
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Sólido de Revolución - Peón")

# Mostrar la figura
plt.show()
