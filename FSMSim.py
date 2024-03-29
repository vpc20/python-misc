edges = {(0, '+'): 1, (0, '-'): 1, (0, '0'): 2, (0, '1'): 2, (0, '2'): 2, (0, '3'): 2, (0, '4'): 2, (0, '5'): 2,
         (0, '6'): 2, (0, '7'): 2, (0, '8'): 2, (0, '9'): 2, (0, '.'): 3, (1, '0'): 2, (1, '1'): 2, (1, '2'): 2,
         (1, '3'): 2, (1, '4'): 2, (1, '5'): 2, (1, '6'): 2, (1, '7'): 2, (1, '8'): 2, (1, '9'): 2, (1, '.'): 3,
         (2, '0'): 2, (2, '1'): 2, (2, '2'): 2, (2, '3'): 2, (2, '4'): 2, (2, '5'): 2, (2, '6'): 2, (2, '7'): 2,
         (2, '8'): 2, (2, '9'): 2, (2, '.'): 4, (2, 'e'): 5, (2, 'E'): 5, (3, '0'): 4, (3, '1'): 4, (3, '2'): 4,
         (3, '3'): 4, (3, '4'): 4, (3, '5'): 4, (3, '6'): 4, (3, '7'): 4, (3, '8'): 4, (3, '9'): 4, (4, '0'): 4,
         (4, '1'): 4, (4, '2'): 4, (4, '3'): 4, (4, '4'): 4, (4, '5'): 4, (4, '6'): 4, (4, '7'): 4, (4, '8'): 4,
         (4, '9'): 4, (4, 'e'): 5, (4, 'E'): 5, (5, '+'): 6, (5, '-'): 6, (5, '0'): 7, (5, '1'): 7, (5, '2'): 7,
         (5, '3'): 7, (5, '4'): 7, (5, '5'): 7, (5, '6'): 7, (5, '7'): 7, (5, '8'): 7, (5, '9'): 7, (6, '0'): 7,
         (6, '1'): 7, (6, '2'): 7, (6, '3'): 7, (6, '4'): 7, (6, '5'): 7, (6, '6'): 7, (6, '7'): 7, (6, '8'): 7,
         (6, '9'): 7, (7, '0'): 7, (7, '1'): 7, (7, '2'): 7, (7, '3'): 7, (7, '4'): 7, (7, '5'): 7, (7, '6'): 7,
         (7, '7'): 7, (7, '8'): 7, (7, '9'): 7}

accepting = [2, 4, 7]


def fsm(s, curr_state):
    for c in s:
        if (curr_state, c) in edges:
            curr_state = edges[curr_state, c]
        else:
            return False
    return curr_state in accepting


print(fsm('123', 0))
print(fsm('+123', 0))
print(fsm('.123', 0))
print(fsm('+.123', 0))
print(fsm('+123e1', 0))
print(fsm('.123E2', 0))
print(fsm('+.123e3', 0))

print(fsm('+123', 0))
print(fsm('-123', 0))
print(fsm('123', 0))

print(fsm('+123.', 0))
print(fsm('-123.', 0))
print(fsm('123.', 0))

print(fsm('+123.456', 0))
print(fsm('-123.456', 0))
print(fsm('123.456', 0))

print(fsm('+123.456e789', 0))
print(fsm('-123.456e789', 0))
print(fsm('123.456e789', 0))

print(fsm('+123.456E789', 0))
print(fsm('-123.456E789', 0))
print(fsm('123.456E789', 0))
