from itertools import combinations


def two_factors_naive(arr, n):
    for comb in combinations(arr, 2):
        print(comb)
        if comb[0] * comb[1] == n:
            return comb
    return None


def two_factors(arr, n):
    seen = set()
    for f1 in arr:
        f2 = int(n / f1)
        if f2 in seen:
            return f1, f2
        else:
            seen.add(f1)
    return None


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(two_factors_naive(arr, 72))

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(two_factors(arr, 72))

arr = [1000000 - i for i in range(1, 1000000)]
# print(arr)
# print(two_factors_naive(arr, 72))
print(two_factors(arr, 72))
