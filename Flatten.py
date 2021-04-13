from collections import deque


def flatten(lst):
    flat_list = []
    for e in lst:
        if type(e) is list:
            flat_list += flatten(e)
        else:
            flat_list.append(e)
    return flat_list


# def flatten(lst):
#     def _flatten(lst):
#         for e in lst:
#             if type(e) is list:
#                 _flatten(e)
#             else:
#                 flat_list.append(e)
#
#     flat_list = []
#     _flatten(lst)
#     return flat_list


def flatten2(lst):
    flat = []
    dq = deque(lst)
    while dq:
        e = dq.popleft()
        if type(e) is list:
            for item in reversed(e):
                dq.appendleft(item)
        else:
            flat.append(e)
    return flat


print(flatten([1, 2]))
print(flatten([1, [2, 3]]))
print(flatten([[1, 2], 3]))
print(flatten([[1, 2], [3, 4], [5, [6, 7]]]))
print(flatten([[1, 2], [3, 4], [5, 6, [7, 8]]]))
print(flatten([[[[[1]]]]]))
# print(flatten1([[[[[1]]]]]))

print(flatten2([1, 2]))
print(flatten2([1, [2, 3]]))
print(flatten2([[1, 2], 3]))
print(flatten2([[1, 2], [3, 4], [5, [6, 7]]]))
print(flatten2([[1, 2], [3, 4], [5, 6, [7, 8]]]))
print(flatten2([[[[[1]]]]]))
