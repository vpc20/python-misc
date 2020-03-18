def rsplitx(s, sep, maxsplit):
    a1 = s.split(sep)
    if maxsplit == 0:
        return [s]
    elif maxsplit < 0 or maxsplit > len(a1) - 1:
        return a1
    else:
        return [sep.join(a1[:-maxsplit]) if i == 0 else a1[-maxsplit + i - 1] for i in range(maxsplit + 1)]


print(rsplitx('a,b,c,d,e', ',', -1))
print(rsplitx('a,b,c,d,e', ',', 0))
print(rsplitx('a,b,c,d,e', ',', 1))
print(rsplitx('a,b,c,d,e', ',', 2))
print(rsplitx('a,b,c,d,e', ',', 3))
print(rsplitx('a,b,c,d,e', ',', 4))
print(rsplitx('a,b,c,d,e', ',', 5))
print(rsplitx('a,b,c,d,e', ',', 6))
