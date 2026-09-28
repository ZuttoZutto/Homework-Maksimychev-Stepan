import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
sample_sizes = [50, 500, 5000]
data_norm = np.random.normal(0, 1, max(sample_sizes))

fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=True)
x_theory = np.linspace(-4, 4, 200)
y_theory = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x_theory**2)

for i, n in enumerate(sample_sizes):
    axes[i].hist(data_norm[:n], bins=25, density=True, alpha=0.7, color='mediumpurple', edgecolor='black')
    axes[i].plot(x_theory, y_theory, 'r--', lw=2, label='N(0,1)')
    axes[i].set_title(f'N = {n}', fontsize=11)
    axes[i].set_xlabel('Значение', fontsize=10)
    axes[i].legend(fontsize=9)

axes[0].set_ylabel('Плотность вероятности', fontsize=10)
fig.suptitle('Сходимость гистограммы к нормальному закону', fontsize=12)
plt.tight_layout()
plt.show()