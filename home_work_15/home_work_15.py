def arithmetic(num_1=None, num_2=None, operations=None):
    """
    Given two integers and operation on them, return the result according to the operation.

    :param num_1: int
    :param num_2: int
    :param operations: str
    :return: int, According to the operation.
    """
    operators = {"+": lambda num1, num2: num1 + num2,
                 "-": lambda num1, num2: num1 - num2,
                 "*": lambda num1, num2: num1 * num2,
                 "/": lambda num1, num2: num1 / num2,
                 }

    if operations not in operators:
        return "Unknown operation"
    else:
        return operators.get(operations)(num_1, num_2)


res = arithmetic(2, 2, "+")
print(res)
