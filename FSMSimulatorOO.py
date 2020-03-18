class FSM:
    def __init__(self):
        self.initial_state = None
        self.states_count = 0
        self.edges_count = 0
        self.states_dict = {}
        self.edges_dict = {}

    def add_state(self, state_name, accepting=False):
        # self.states_list.append({state_name : accepting})
        self.states_dict[state_name] = accepting
        self.states_count += 1

    def set_initial_state(self, initial_state):
        self.initial_state = initial_state

    def add_edge(self, curr_state, input, next_state):
        self.edges_dict[curr_state, input] = next_state
        self.edges_count += 1

    def print_states(self):
        print('\n***** List of States in the Finite State Machine *****')
        for state in self.states_dict:
            print
            state, self.states_dict[state]
        print('No of states : ' + str(self.states_count))

    def print_edges(self):
        print('\n***** List of Edges in the Finite State Machine *****')
        for edge in self.edges_dict:
            print(edge[0], edge[1], self.edges_dict[edge])
        print('No of edges : ' + str(self.edges_count))

    def run(self, input):
        curr_state = self.initial_state
        for ch in input:
            if (curr_state, ch) in self.edges_dict:
                curr_state = self.edges_dict[curr_state, ch]
            else:
                return False
        else:
            print(self.edges_dict)
            return bool(self.states_dict[curr_state])


fsm = FSM()

fsm.add_state('S1', accepting=True)
fsm.add_state('S2', accepting=True)
fsm.set_initial_state('S1')

fsm.add_edge('S1', '0', 'S2')
fsm.add_edge('S1', '1', 'S2')
fsm.add_edge('S2', '0', 'S1')
fsm.add_edge('S2', '1', 'S1')

# print ' '
# fsm.print_states()
# fsm.print_edges()

print(fsm.run('0'))
print(fsm.run('1'))
print(fsm.run('01'))
print(fsm.run('10'))
print(fsm.run('101'))
print(fsm.run('010'))
print(fsm.run('111'))
print(fsm.run('0000'))
print(fsm.run('1111'))
print(fsm.run('1010'))
print(fsm.run('0101'))
print(fsm.run('11111010100010'))
print(fsm.run('10001111010100001'))
fsm.print_states()
fsm.print_edges()
