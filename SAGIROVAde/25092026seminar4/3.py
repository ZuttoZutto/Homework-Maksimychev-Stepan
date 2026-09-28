import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных
iris_raw = np.genfromtxt('iris_data.csv', delimiter=',', dtype=str, skip_header=1)
species = iris_raw[:, 4]
petal_lengths = iris_raw[:, 2].astype(float)

# 1. Доля разных видов
unique_species, counts_species = np.unique(species, return_counts=True)

# 2. Доля по длине лепестка
bins_petal = [-np.inf, 1.2, 1.5, np.inf]
labels_petal = ['<= 1.2 см', '1.2 - 1.5 см', '> 1.5 см']
digitized = np.digitize(petal_lengths, bins_petal) - 1
bin_counts = np.bincount(digitized, minlength=3)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].pie(counts_species, labels=unique_species, autopct='%1.1f%%', startangle=90, colors=['#66c2a5', '#fc8d62', '#8da0cb'])
axes[0].set_title('Доля видов Iris', fontsize=12)

axes[1].pie(bin_counts, labels=labels_petal, autopct='%1.1f%%', startangle=90, colors=['#e5c494', '#b3b3b3', '#8dd3c7'])
axes[1].set_title('Доля по длине лепестка', fontsize=12)

fig.suptitle('Упражнение 3: Круговые диаграммы датасета Iris', fontsize=12)
plt.tight_layout()
plt.show()