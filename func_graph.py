import numpy as np
import matplotlib.pyplot as plt

def plot_function(min_x, max_x):
    #Функция строит график функции y = x * sin(x) в пределах от min_x до max_x.
    # Создаем массив значений x
    x = np.linspace(min_x, max_x, 1000)
    
    # Вычисляем соответствующие значения y
    y = x * np.sin(x)
    
    # Строим график
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'График функции $f(x) = x \\cdot \\sin(x)$ на отрезке [{min_x}, {max_x}]')
    plt.grid(True)
    plt.show()
    