class LogicGate:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class UnaryGate(LogicGate):
    def __init__(self, name):
        LogicGate.__init__(self, name)
        self.inp = None
        self.source = None

    def input(self, inp):
        self.inp = inp

    def set_source(self, source_gate):
        self.source = source_gate

    def check_unary_gate_input(self):
        if self.inp is None:
            if self.source is None:
                print 'No in input for Unary Gate:', self.name
            else:
                self.inp = self.source.output()

class Inverter(UnaryGate):
    def __init__(self, name):
        UnaryGate.__init__(self, name)

    def output(self):
        self.check_unary_gate_input()

        if self.inp == 0:
            return 1
        else:
            return 0


class BinaryGate(LogicGate):
    def __init__(self, name):
        LogicGate.__init__(self, name)
        self.inp1 = None
        self.inp2 = None
        self.source1 = None
        self.source2 = None

    def input1(self, inp1):
        self.inp1 = inp1

    def input2(self, inp2):
        self.inp2 = inp2

    def set_source(self, source_gate):
        if self.source1 is None:
            self.source1 = source_gate
        elif self.source2 is None:
            self.source2 = source_gate

    def check_binary_gate_input(self):
        if self.inp1 is None or self.inp2 is None:
            if self.source1 is None and self.source2 is None:
                print 'No in input for Binary Gate:', self.name
                return

        if self.inp1 is None:
            if self.source1 is not None:
                self.inp1 = self.source1.output()

        if self.inp2 is None:
            if self.source2 is not None:
                self.inp2 = self.source2.output()


class AndGate(BinaryGate):
    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def output(self):
        self.check_binary_gate_input()
        if self.inp1 == 1 and self.inp2 == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def output(self):
        self.check_binary_gate_input()
        if self.inp1 == 1 or self.inp2 == 1:
            return 1
        else:
            return 0


class Connector:
    def __init__(self):
        self.connector_dict = {}

    def add_connection(self, source_gate, target_gate):
        self.connector_dict[source_gate] = target_gate
        target_gate.set_source(source_gate)

    def show(self):
        print "\nConnector Definition for Logic Gates"
        for key, value in self.connector_dict.iteritems():
            print key, '==>',  value


# truth table values
import math

num_of_inputs = 2
num_rows_in_truth_table = int(math.pow(2, num_of_inputs))
bin_str_length = len('{0:b}'.format(num_rows_in_truth_table - 1))

format_str = '{0:0' + str(bin_str_length) + 'b}'
print [format_str.format(i) for i in range(num_rows_in_truth_table)]


# inv1 = Inverter('Inverter1')
# inv2 = Inverter('Inverter2')
# inv3 = Inverter('Inverter3')
#
# conn = Connector()
# conn.add_connection(inv1, inv2)
# conn.add_connection(inv2, inv3)
#
# inv1.input(1)
# print inv3.output()


# and1 = AndGate('AndGate1')
# and2 = AndGate('AndGate2')
# and3 = AndGate('AndGate3')
#
# conn = Connector()
# conn.add_connection(and1, and3)
# conn.add_connection(and2, and3)
#
# and1.input1(1)
# and1.input2(1)
# and2.input1(1)
# and2.input2(1)
#
# print and3.output()

or1 = OrGate('OrGate1')
or2 = OrGate('OrGate2')
or3 = OrGate('OrGate3')

conn = Connector()
conn.add_connection(or1, or3)
conn.add_connection(or2, or3)

or1.input1(0)
or1.input2(0)
or2.input1(0)
or2.input2(0)

print or3.output()
conn.show()

print isinstance(or1, UnaryGate)
print isinstance(or1, LogicGate)
print isinstance(or1, BinaryGate)
print isinstance(or1, OrGate)


