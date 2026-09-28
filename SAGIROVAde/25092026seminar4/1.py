import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# Данные лабы (число частиц за 10с и число случаев)
n_impulses = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
cases = np.array([0, 3, 9, 15, 30, 59, 49, 53, 62, 45, 28, 20, 14, 7, 2, 3, 0, 1])

# Расчет среднего значения
total_counts = np.sum(n_impulses * cases)
total_measurements = np.sum(cases)
mean_n = total_counts / total_measurements
sigma_theory = np.sqrt(mean_n)

plt.figure(figsize=(8, 5))
plt.bar(n_impulses, cases, width=0.8, alpha=0.7, color='skyblue', edgecolor='black', label='Эксперимент (10с)')

# Кривая Пуассона
x_poisson = np.arange(0, 18)
poisson_prob = (mean_n**x_poisson / np.array([factorial(i) for i in x_poisson])) * np.exp(-mean_n)
poisson_counts = poisson_prob * total_measurements
plt.plot(x_poisson, poisson_counts, 'ro--', linewidth=2, markersize=8, label=f'Пуассон ($\lambda$={mean_n:.2f})')

plt.title('Упражнение 1: Счётчик Гейгера', fontsize=12)
plt.xlabel('Число частиц за 10 с', fontsize=10)
plt.ylabel('Число случаев (из 400)', fontsize=10)
plt.legend(fontsize=9)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()