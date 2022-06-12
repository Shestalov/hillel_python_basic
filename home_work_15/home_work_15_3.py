def arithmetic(number_1, number_2, operations=None):
    """
    Given two integers and operation on them, return the result according to the operation.

    :param number_1: int
    :param number_2: int
    :param operations: + or - or * or /
    :return: int (+, -, *), float (/)
    """
    if operations == "+":
        return number_1 + number_2
    elif operations == "-":
        return number_1 - number_2
    elif operations == "/":
        return number_1 / number_2
    elif operations == "*":
        return number_1 * number_2
    else:
        return "Unknown operation"


res = arithmetic(2, 4)
print(res)
print(type(res))
