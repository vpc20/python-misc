def head(lst):
    return lst[0]


def tail(lst):
    return lst[1:]


def initial(lst):
    return lst[:-1]


def last(lst):
    return lst[-1]


def square(x):
    return x * x


def map_list(func, lst):
    if lst:
        return [func(head(lst))] + map_list(func, tail(lst))
    else:
        return []


def filter_list(func, lst):
    if lst:
        if func(head(lst)):
            return [head(lst)] + filter_list(func, tail(lst))
        else:
            return filter_list(func, tail(lst))
    else:
        return []


def reduce_list(func, lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return func(reduce_list(func, initial(lst)), last(lst))


def print_item(x):
    print(x)


def for_each(func, lst):
    if lst:
        func(head(lst))
        for_each(func, tail(lst))


def mapi(func, arr):
    result = []
    for e in arr:
        result.append(func(e))
    return result


def filteri(func, arr):
    result = []
    for e in arr:
        if func(e):
            result.append(e)
    return result


def reducei(func, arr):
    if len(arr) == 1:
        return arr[0]
    result = arr[0]
    for i in range(1, len(arr)):
        result = func(result, arr[i])
    return result


def map_indexed(func, arr):
    result = []
    for i, e in enumerate(arr):
        result.append(func(i, e))
    return result


def take(n, arr):
    result = []
    for i in range(n):
        result.append(arr[i])
    return result


def take_last(n, arr):
    # result = []
    # for i in range(-n, 0, 1):
    #     result.append(arr[i])
    # return result
    return [arr[i] for i in range(-n, 0, 1)]


def take_while(func, arr):
    result = []
    for e in arr:
        if func(e):
            result.append(e)
        else:
            break
    return result


def drop_while(func, arr):
    i = 0
    for i, e in enumerate(arr):
        if not func(e):
            break
    return arr[i:]


list1 = [1, 2, 3, 4, 5]
list2 = [-3, -2, -1, 0, 1, 2, 3]

list3 = [-3, -2, -1, 0, 1]

print(map(square, list1))
print(map(lambda x: x * x, list1))

print(map_list(lambda x: x * x, list1))

print(map(lambda x, y: x * y, list1, list3))

print(filter(lambda x: x > 0, list2))
print(filter_list(lambda x: x > 0, list2))

print(reducei(lambda x, y: x + y, list1))
print(reduce_list(lambda x, y: x + y, list1))

for_each(print_item, list1)

print(map_indexed(lambda i, e: (i, e), list1))
print(take_while(lambda e: e < 4, list1))
print([e for e in list1 if e < 4])
print(drop_while(lambda e: e < 3, list1))
print(take(2, list1))
print(take_last(2, list1))
