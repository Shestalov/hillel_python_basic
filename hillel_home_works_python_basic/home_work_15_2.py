import operator


def arithmetic(num1, num2, operations):
    """
    Given two integers and operation on them, return the result according to the operation.

    :param num1: int
    :param num2: int
    :param operations: str
    :return: int, According to the operation.
    """
    operators = {
        "addition": operator.add,
        "subtraction ": operator.sub,
        'multiply': operator.mul,
        'subtract': operator.sub,
    }
    return operators[operations](num1, num2)


res = arithmetic(2, 3)

print(res)
print(type(res))
