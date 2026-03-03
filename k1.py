import random
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import sys


class Isotropic:
    """
    Класс для генерации изотропного излучения из одной точки
    """

    def __init__(self, n):
        """
        Инициализация векторов

        Переменные на вход
        n: количество векторов
        """

        self.n = n
        if n <= 0:
            raise ValueError(f"Неположительное значение количества векторов")


    def vectors(self):
        """
        Генерация изотропно распределенных векторов на сфере.

        Переменные на выход:
        numpy.ndarray: массив векторов размером (n, 3)
        """
        vectors_array_norm = np.zeros((self.n, 3))

        for i in range(self.n):
            while True:
                l = random.uniform(-1, 1)
                m = random.uniform(-1, 1)
                n = random.uniform(-1, 1)

                length = sqrt(l ** 2 + m ** 2 + n ** 2)

                if (length <= 1) and (length > 0):
                    break

            vectors_array_norm[i] = np.array([l, m, n]) / length

        return vectors_array_norm

    def plot(self):
        """
        Построение 3D графика векторов на сфере.
        """
        vectors = self.vectors()

        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        x = vectors[:, 0]
        y = vectors[:, 1]
        z = vectors[:, 2]

        ax.scatter(x, y, z, c='blue', marker='o', alpha=0.6, s=30)

        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)
        sphere_x = np.outer(np.cos(u), np.sin(v))
        sphere_y = np.outer(np.sin(u), np.sin(v))
        sphere_z = np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_wireframe(sphere_x, sphere_y, sphere_z, color='gray', alpha=0.2)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Изотропное распределение {self.n} векторов на сфере')

        plt.show()


