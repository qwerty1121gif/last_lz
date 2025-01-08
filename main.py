# Импортируем созданные модули
import func_graph
import pyramaid

def main():
    print("Выберите задачу:")
    print("1. Построить график функции")
    print("2. Найти объем усеченной пирамиды")
    choice = input("Какую зачу решим?: ")

    if choice == "1":
        try:
            min_x = float(input("Введите минимальное значение x: "))
            max_x = float(input("Введите максимальное значение x: "))
            
            # Вызываем функцию построения графика
            func_graph.plot_function(min_x, max_x)
        
        except ValueError:
            print("Ошибка ввода данных.")
    
    elif choice == "2":
        try:
            base_area = float(input("Введите площадь нижнего основания: "))
            top_area = float(input("Введите площадь верхнего основания: "))
            height = float(input("Введите высоту пирамиды: "))
            
            # Вычисляем объем пирамиды
            result = pyramaid.volume_pyramid(base_area, top_area, height)
            print(f"Объем пирамиды составляет: {result}")
        
        except ValueError:
            print("Ошибка ввода данных.")
    
    else:
        print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()