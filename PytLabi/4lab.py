import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Задание 1: График двух функций с разными осями Y
x = np.linspace(0, 5, 100)
y1 = np.sin(x)  # Первая функция
y2 = np.exp(x)  # Вторая функция

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()  # Создаем вторую ось Y
ax1.plot(x, y1, 'g-', label='sin(x)')
ax2.plot(x, y2, 'b-', label='exp(x)')

ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)', color='g')
ax2.set_ylabel('exp(x)', color='b')

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('График двух функций с разными осями Y')
plt.savefig('functions_plot.png')
plt.savefig('functions_plot.pdf')
plt.show()

# Задание 2: Точечная диаграмма для трех кластеров данных
x1 = np.random.normal(2, 0.5, 50)
y1 = np.random.normal(2, 0.5, 50)

x2 = np.random.normal(4, 0.5, 50)
y2 = np.random.normal(4, 0.5, 50)

x3 = np.random.normal(3, 0.5, 50)
y3 = np.random.normal(1, 0.5, 50)

plt.figure()
plt.scatter(x1, y1, color='red', label='Кластер 1')
plt.scatter(x2, y2, color='green', label='Кластер 2')
plt.scatter(x3, y3, color='blue', label='Кластер 3')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Точечная диаграмма трех кластеров')
plt.legend()
plt.savefig('scatter_plot.png')
plt.savefig('scatter_plot.pdf')
plt.show()

# Задание 3: Круговая диаграмма
labels = ['Категория A', 'Категория B', 'Категория C', 'Категория D', 'Категория E']
sizes = [15, 30, 25, 20, 10]

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Равные оси для круга
plt.title('Круговая диаграмма предпочтений пользователей')
plt.savefig('pie_chart.png')
plt.savefig('pie_chart.pdf')
plt.show()

# Задание 4: Тепловая карта
data = np.random.rand(10, 10)
plt.figure()
sns.heatmap(data, cmap='viridis')
plt.title('Тепловая карта случайных чисел')
plt.savefig('heatmap.png')
plt.savefig('heatmap.pdf')
plt.show()

# Задание 5: Столбчатая диаграмма с горизонтальными столбцами
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.figure()
plt.barh(categories, values)
plt.xlabel('Значения')
plt.title('Горизонтальная столбчатая диаграмма')
plt.savefig('horizontal_bar_chart.png')
plt.savefig('horizontal_bar_chart.pdf')
plt.show()

# Задание 6: Трехмерный график поверхности
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis (sin(sqrt(x^2 + y^2)))')
plt.title('Трехмерный график поверхности')
plt.savefig('surface_plot.png')
plt.savefig('surface_plot.pdf')
plt.show()
