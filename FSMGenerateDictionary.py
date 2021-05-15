def generate_fsm_dict(elist):
    d = {}
    for start, end, chars in elist:
        for c in chars:
            d[(start, c)] = end
    return d


elist = [(0, 1, '+-'),
         (0, 2, '0123456789'),
         (0, 3, '.'),
         (1, 2, '0123456789'),
         (1, 3, '.'),
         (2, 2, '0123456789'),
         (2, 4, '.'),
         (2, 5, 'eE'),
         (3, 4, '0123456789'),
         (4, 4, '0123456789'),
         (4, 5, 'eE'),
         (5, 6, '+-'),
         (5, 7, '0123456789'),
         (6, 7, '0123456789'),
         (7, 7, '0123456789'),
         ]

print(generate_fsm_dict(elist))
