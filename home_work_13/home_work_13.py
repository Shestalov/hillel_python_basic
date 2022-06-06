def sum_digits(number):
    """
    Given a positive integer, return the multiplication of all digits by skipping zero.

    :param number: int
    :return: int, Multiplication of all digits by skipping zero.
    """
    res = 1
    for digit in str(number):
        if int(digit) > 0:
            # print(res, '*', num, '=', res * int(num))
            res *= int(digit)
    return res


result = sum_digits(999)
print(result)

if __name__ == '__main__':
    help(sum_digits)
