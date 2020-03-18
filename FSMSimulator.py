# indexes for the fsm list
CURR_STATE_IDX = 0
LABEL_IDX = 1
NEXT_STATE_IDX = 2

# definition of the finite state machine
# fsm = [[1, 'a', 2],
#        [2, 'b', 3]]

accepting = [3]
fsm = [[1, '1', 2],
       [1, '0', 1],
       [2, '0', 1],
       [2, '1', 2]]
accepting = [1,2]


def fsm_simulator(string, fsm_def, accept_state):
    current_state = 1
    if string == '':
        return current_state in accept_state

    for i in range(len(string)):  # go through each of the characters in string
        for j in range(len(fsm_def)):  # search for current_state and letter in fsm
            if current_state == fsm_def[j][CURR_STATE_IDX] and string[i] == fsm_def[j][LABEL_IDX]:
                current_state = fsm_def[j][NEXT_STATE_IDX]
                break
        else:
            return False  # not found after going through all elements of fsm
    else:
        if current_state in accept_state:  # string ok
            return True
        else:
            return False


# print "True", fsm_simulator('ab', fsm, accepting)
# print "False", fsm_simulator('a', fsm, accepting)
# print "False", fsm_simulator('b', fsm, accepting)
# print "False", fsm_simulator('ba', fsm, accepting)
# print "False", fsm_simulator('ca', fsm, accepting)
# print "False", fsm_simulator('abc', fsm, accepting)
# print "False", fsm_simulator('bac', fsm, accepting)
# print "False", fsm_simulator('cab', fsm, accepting)
# print "False", fsm_simulator('abcc', fsm, accepting)

print "False", fsm_simulator('abcc', fsm, accepting)
print "False", fsm_simulator('1x', fsm, accepting)
print "False", fsm_simulator('x1', fsm, accepting)
print "False", fsm_simulator('11a', fsm, accepting)
print "False", fsm_simulator('a10', fsm, accepting)
print "True", fsm_simulator('0', fsm, accepting)
print "True", fsm_simulator('1', fsm, accepting)
print "True", fsm_simulator('10', fsm, accepting)
print "True", fsm_simulator('01', fsm, accepting)
print "True", fsm_simulator('101', fsm, accepting)
print "True", fsm_simulator('111', fsm, accepting)
