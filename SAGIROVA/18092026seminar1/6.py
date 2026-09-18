import numpy as np
from typing import Union


def ols_numpy(x: Union[np.ndarray, list], y: Union[np.ndarray, list]) -> np.ndarray:
    """
    Вычисляет коэффициенты МНК с помощью матричного решения нормального уравнения.

    Матричная форма: beta = (X^T * X)^(-1) * X^T * y
    Для защиты от сингулярности используется псевдообратная матрица (pinv).

    Параметры:
        x: Массив или список значений x.
        y: Массив или список значений y.

    Возвращает:
        Numpy-массив array([beta_0, beta_1]).
    """
    x_arr = np.asarray(x, dtype=float)
    y_arr = np.asarray(y, dtype=float)

    if x_arr.shape != y_arr.shape:
        raise ValueError("Размеры входных массивов должны совпадать")
    if x_arr.size == 0:
        raise ValueError("Входные массивы не могут быть пустыми")

    # Создаем матрицу признаков X со столбцом единиц для свободного члена
    # shape будет (n_samples, 2)
    X = np.vstack([np.ones_like(x_arr), x_arr]).T

    # Решение через псевдообратную матрицу Мура-Пенроуза.
    # Это стандарт индустрии: pinv автоматически обрабатывает случаи,
    # когда (X^T * X) плохо обусловлена или сингулярна.
    coefficients = np.linalg.pinv(X.T @ X) @ X.T @ y_arr

    return coefficients


x_np = np.array([1, 2, 3, 4, 5])
y_np = np.array([2, 4, 5, 4, 5])
coeffs = ols_numpy(x_np, y_np)
print(f"Уравнение линии: y = {coeffs[1]:.2f}x + {coeffs[0]:.2f}")
# Вывод: Уравнение линии: y = 0.60x + 2.20