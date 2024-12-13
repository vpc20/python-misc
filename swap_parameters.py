s = '''
        stack = Stack()
        self.assertEqual(None, stack.peek())

        stack.push(1)
        self.assertEqual([1], stack.to_array())
        self.assertEqual(1, stack.peek())
        stack.push(2)
        self.assertEqual([2, 1], stack.to_array())
        self.assertEqual(2, stack.peek())
        stack.push(3)
        self.assertEqual([3, 2, 1], stack.to_array())
        self.assertEqual(3, stack.peek())
        stack.push(4)
        self.assertEqual([4, 3, 2, 1], stack.to_array())
        self.assertEqual(4, stack.peek())
        stack.push(5)
        self.assertEqual([5, 4, 3, 2, 1], stack.to_array())
        self.assertEqual(5, stack.peek())

        stack.pop()
        self.assertEqual([4, 3, 2, 1], stack.to_array())
        self.assertEqual(4, stack.peek())
        stack.pop()
        self.assertEqual([3, 2, 1], stack.to_array())
        self.assertEqual(3, stack.peek())
        stack.pop()
        self.assertEqual([2, 1], stack.to_array())
        self.assertEqual(2, stack.peek())
        stack.pop()
        self.assertEqual([1], stack.to_array())
        self.assertEqual(1, stack.peek())
        stack.pop()
        self.assertEqual([], stack.to_array())
        self.assertEqual(None, stack.peek())
        stack.pop()
        self.assertEqual([], stack.to_array())
        self.assertEqual(None, stack.peek())
'''
# lines = s.split('\n')
# for line in lines:
#     i = line.find('assertEqual')
#     if i != -1:
#         parms = line[i + 11:].strip('(').strip(')')
#         j = parms.find('),')
#         p1 = parms[:j + 1]
#         p2 = parms[j + 3:]
#         new_line = line[:i + 12] + p2 + ', ' + p1 + ')'
#         print(new_line)
#     else:
#         print(line)

open_parens = ['(', '[', '{']
close_parens = [')', ']', '}']
parens_stack = []

lines = s.split('\n')
for line in lines:
    i = line.find('assertEqual')
    if i != -1:
        parms = line[i + 11:]
        parms = parms[1:-1]
        for idx, c in enumerate(parms):
            if c == ',' and not parens_stack:
                p1 = parms[:idx]
                p2 = parms[idx + 2:]
                new_line = line[:i + 12] + p2 + ', ' + p1 + ')'
                # new_line = f'{line[:i + 12]}{p2}, {p1})'
                print(new_line)
            elif c in open_parens:
                parens_stack.append(c)
            elif c in close_parens:
                parens_stack.pop()
    else:
        print(line)

