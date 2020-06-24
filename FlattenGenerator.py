# def flatten(lst):
#     for item in lst:
#         if isinstance(item, list):
#             for i in flatten(item):
#                 yield i
#         else:
#             yield item


def flatten(lst):
    for e in lst:
        if isinstance(e, list):
            yield from flatten(e)
        else:
            yield e


# list_of_lists = [1, 2]
# list_of_lists = [[1, 2], 3]
# list_of_lists = [[1, 2], [3, 4], [5, [6, 7]]]
list_of_lists = [[1, 2], [3, 4], [5, 6, [7, 8]]]

print(list(flatten(list_of_lists)))
