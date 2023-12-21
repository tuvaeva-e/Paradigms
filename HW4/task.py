import numpy as np

def pearson_correlation(x, y):
    # Расчет среднего значения
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Расчет ковариации
    cov = np.sum((x - x_mean) * (y - y_mean))

    # Расчет стандартных отклонений
    x_std = np.sqrt(np.sum((x - x_mean)**2))
    y_std = np.sqrt(np.sum((y - y_mean)**2))

    # Расчет коэффициента корреляции Пирсона
    corr = cov / (x_std * y_std)

    return corr

# Пример использования
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
corr = pearson_correlation(x, y)
print("Коэффициент корреляции Пирсона:", corr)