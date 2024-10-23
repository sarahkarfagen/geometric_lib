import math


def area(r):
    """
    Функция считает площадь круга.

    Параметры
    ----------
    r : int
        Радиус круга

    Возвращает
    -------
    int
        Площадь круга

    Пример
    --------

    .. code-block:: python

    res = area(1)
    print(res)        # 3.141592653589793

    """
    return math.pi * r * r


def perimeter(r):
    """
    Функция считает периметр круга.

    Параметры
    ----------
    r : int
        Радиус круга

    Возвращает
    -------
    int
        Периметр круга

    Пример
    --------

    .. code-block:: python

    res = perimeter(1)
    print(res)        # 6.283185307179586

    """
    return 2 * math.pi * r

