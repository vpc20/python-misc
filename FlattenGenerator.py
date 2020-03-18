def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            for i in flatten(item):
                yield i
        else:
            yield item


# list_of_lists = [1, 2]
# list_of_lists = [[1, 2], 3]
#list_of_lists = [[1, 2], [3, 4], [5, [6, 7]]]
list_of_lists = [[1, 2], [3, 4], [5, 6, [7,8]]]

for x in flatten(list_of_lists):
    print(x)