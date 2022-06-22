nested_list = [11, 22, [33, 44, [55, 66, [77]]]]


def make_list_flat(_nested_list, tmp=None):
    if tmp is None:
        tmp = []

    tmp.append(len(_nested_list))

    for i in _nested_list:
        if isinstance(i, list):
            make_list_flat(i, tmp)

    return sum(tmp)


if __name__ == '__main__':
    print(make_list_flat(nested_list))
