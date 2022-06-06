def square(square_side):
    """
    Given an int, return the perimeter, area, diagonal of the square.

    :param square_side: int
    :return: tuple, Perimetr, Area, Diagonal of the square.
    """
    return square_side * 4, square_side * square_side, square_side * (2 ** 0.5)


print(square(16))
