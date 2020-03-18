# edges = {(1, 'a'): 2,
#          (2, 'a'): 2,
#          (2, '1'): 3,
#          (3, '1'): 3}
# accepting = [3]
edges = {(1, 'a'): 2,
         (2, '1'): 2}
accepting = [2]


def FSMSimulator(string, current_state, edges, accepting):
    if string == '':
        return current_state in accepting
    else:
        letter = string[0]
        if (current_state, letter) in edges:
            next_state = edges[current_state, letter]
            remaining_string = string[1:]
            return FSMSimulator(remaining_string, next_state, edges, accepting)
        else:
            return False


print(FSMSimulator('a1', 1, edges, accepting))
