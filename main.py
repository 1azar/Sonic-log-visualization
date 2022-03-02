import numpy as np
import lasio
import matplotlib.pyplot as plt


# ============================================================= DESCRIPTION
"""
Создаёт 3д точечный график для las файлов, содержащих только данные спектральной шумометрии.

Пример:
~ASCII Log Data
#DEPTH    SVMF1    SVMF2    SVMF3    SVMF4    ...    SVMF20
2563.80  81.6000  82.7000  84.1000  82.8000   ...   78.7000  
2563.90  81.6000  82.7000  84.1000  82.8000   ...   78.7000  
2564.00  81.6000  82.7000  84.1000  82.8000   ...   78.7000  
2564.10  81.6000  82.7000  84.1000  82.8000   ...   78.7000  
2564.20  81.6000  82.7000  84.1000  82.8000   ...   78.7000  
2564.30  81.6000  82.7000  84.1000  82.8000   ...   78.7000
 ...      ...      ...      ...      ...      ...    ...
3000.10  81.6000  82.7000  84.1000  82.8000   ...   78.7000 
"""
# =============================================================

# -------------------------------------------------------------------- SETTING
# Плотность точек поверхности. чем меньше, тем реже
GRID_DENS = 100

# Подписи к осям
X_LABEL = "DEPTH.M"
Y_LABEL = "SVMF NUM"
Z_LABEL = "SVMF.dB"

# Размер фигуры. чем больше, тем выше разрешение
FIG_height = 9
FIG_width = 6

# Путь до las файла
LAS_PATH = "my_las.las"

DPI_SAVE = 300 # dpi для сохранения фигуры
SAVE_NAME = "3d_contour_SonicLog.png" # имя при сохранении
# --------------------------------------------------------------------

las = lasio.read(LAS_PATH)
x = las.data[:,0]
y = np.linspace(0, 100, len(las.data[0,1:]));
X, Y = np.meshgrid(x, y)
Z=las.data[:,1:].transpose()

# Создание контейнера для фигуры
fig = plt.figure(figsize=(9, 6))
ax = plt.axes(projection = '3d')

# contour3D создание
ax.contour3D(X, Y, Z, GRID_DENS, cmap = 'viridis')

# set labels
ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_zlabel(Z_LABEL)

# показать фигуру
plt.show()
plt.savefig(SAVE_NAME, dpi = DPI_SAVE)