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


print(flatten([1, 2]))
print(flatten([1, [2, 3]]))
print(flatten([[1, 2], 3]))
print(flatten([[1, 2], [3, 4], [5, [6, 7]]]))
print(flatten([[1, 2], [3, 4], [5, 6, [7, 8]]]))
print(flatten([[[[[1]]]]]))
# print(flatten1([[[[[1]]]]]))
