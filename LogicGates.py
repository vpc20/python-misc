class LogicGate:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class UnaryGate(LogicGate):
    def __init__(self, name):
        LogicGate.__init__(self, name)
        self.input = None

    def get_input(self):
        if self.input == 0 or self.input == 1:
            return self.input
        else:
            if isinstance(self.input, LogicGate):
                return self.input.output()
            else:
                raise ValueError("Invalid input for UnaryGate " + self.name)


class Inverter(UnaryGate):
    def __init__(self, name):
        UnaryGate.__init__(self, name)

    def output(self):
        return int(self.get_input() == 0)


class BinaryGate(LogicGate):
    def __init__(self, name):
        LogicGate.__init__(self, name)
        self.input1 = None
        self.input2 = None

    def get_input1(self):
        if self.input1 == 0 or self.input1 == 1:
            return self.input1
        else:
            if isinstance(self.input1, LogicGate):
                return self.input1.output()
            else:
                raise ValueError("Invalid input for BinaryGate " + self.name)

    def get_input2(self):
        if self.input2 == 0 or self.input2 == 1:
            return self.input2
        else:
            if isinstance(self.input2, LogicGate):
                return self.input2.output()
            else:
                raise ValueError("Invalid input for BinaryGate " + self.name)


class AndGate(BinaryGate):
    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def output(self):
        return self.get_input1() and self.get_input2()
        # return int(not bool(self.get_input1() and self.get_input2())) #nand


class OrGate(BinaryGate):
    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def output(self):
        return self.get_input1() or self.get_input2()


print('')
inv1 = Inverter('Inverter1')
for i in range(2):
    inv1.input = i
    print("Not {} = {}".format(inv1.input, inv1.output()))

print('')
and1 = AndGate('AndGate1')
for i in range(2):
    for j in range(2):
        and1.input1 = i
        and1.input2 = j
        print("{} and {} = {}".format(and1.input1, and1.input2, and1.output()))

print('')
or1 = OrGate('OrGate1')
for i in range(2):
    for j in range(2):
        or1.input1 = i
        or1.input2 = j
        print("{} or {} = {}".format(or1.input1, or1.input2, or1.output()))

# inv1 = Inverter('Inverter1')
# inv2 = Inverter('Inverter2')
# inv1.input = 1
# inv2.input = inv1
# print(inv2.output())

print('')
and1 = AndGate('and1')
and2 = AndGate('and2')
or1 = OrGate('or1')
inv1 = Inverter('inv1')

inv1.input = and1
and2.input1 = inv1
and2.input2 = or1

for i in range(2):
    for j in range(2):
        and1.input1 = i
        and1.input2 = j
        or1.input1 = i
        or1.input2 = j
        print("{} xor {} = {}".format(and1.input1, and1.input2, and2.output()))
