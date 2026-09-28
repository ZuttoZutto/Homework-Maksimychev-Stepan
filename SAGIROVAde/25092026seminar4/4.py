import numpy as np
import matplotlib.pyplot as plt

# 1. Загрузка данных (КЛЮЧЕВОЕ ИСПРАВЛЕНИЕ)
# Используем dtype=float, чтобы принудительно считать всё как числа,
# а затем отдельно обработаем текстовый столбец.
# Но так как в CSV есть текст, лучше использовать usecols для чисел.

# Читаем только числовые столбцы (с 1 по 4 индекс, т.е. 2,3,4,5 колонки файла)
features = np.genfromtxt('iris_data.csv', delimiter=',', usecols=(1, 2, 3, 4), dtype=float, skip_header=1)

# Читаем только текстовый столбец (5-я колонка файла, индекс 5)
species = np.genfromtxt('iris_data.csv', delimiter=',', usecols=(5,), dtype=str, skip_header=1)

# 2. Создаем числовые метки для цветов
unique_species = np.unique(species)
color_map = {name: i for i, name in enumerate(unique_species)}
numeric_colors = np.array([color_map[s] for s in species])

col_names = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
axes = axes.flatten()
plot_idx = 0

for i in range(4):
    for j in range(i + 1, 4):
        x = features[:, i]  # Теперь features точно 2-мерный, это работает
        y = features[:, j]

        # МНК
        A = np.vstack([x, np.ones(len(x))]).T
        a, b = np.linalg.lstsq(A, y, rcond=None)[0]

        x_line = np.linspace(x.min(), x.max(), 100)
        y_line = a * x_line + b

        scatter = axes[plot_idx].scatter(x, y, alpha=0.6, c=numeric_colors, cmap='viridis', s=50)

        axes[plot_idx].plot(x_line, y_line, 'r--', lw=2, label=f'y = {a:.2f}x + {b:.2f}')

        residuals = y - (a * x + b)
        r_squared = 1 - (np.sum(residuals ** 2) / np.sum((y - np.mean(y)) ** 2))

        axes[plot_idx].set_xlabel(col_names[i], fontsize=10)
        axes[plot_idx].set_ylabel(col_names[j], fontsize=10)
        axes[plot_idx].set_title(f'{col_names[j]} vs {col_names[i]}\n$R^2$ = {r_squared:.3f}', fontsize=11)
        axes[plot_idx].legend(fontsize=9)

        cbar = fig.colorbar(scatter, ax=axes[plot_idx], ticks=[0, 1, 2])
        cbar.ax.set_yticklabels(unique_species)

        plot_idx += 1

fig.delaxes(axes[5])
fig.suptitle('Упражнение 4: Матрица парных зависимостей (Iris)', fontsize=16)
plt.tight_layout()
plt.show()