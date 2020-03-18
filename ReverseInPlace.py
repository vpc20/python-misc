def reverse_in_place(arr):
    for i in range(int(len(arr) / 2)):
        arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]


arr1 = [1, 2, 3, 4, 5]
reverse_in_place(arr1)
print(arr1)
