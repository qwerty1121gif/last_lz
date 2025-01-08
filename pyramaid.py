from math import sqrt

def volume_pyramid(base_area, top_area, height):
    """
    Функция вычисляет объем пирамиды по площади оснований и высоте.
    
    :param base_area: Площадь нижнего основания
    :param top_area: Площадь верхнего основания
    :param height: Высота пирамиды
    :return: Объем пирамиды
    """
    return (base_area + top_area + sqrt(base_area * top_area)) / 3 * height