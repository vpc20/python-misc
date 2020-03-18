import random


# def random_walk(steps):
#     x, y = 0, 0
#     for i in range(steps):
#         if random.choice(('x', 'y')) == 'x':
#             x += random.choice((1, -1))
#         else:
#             y += random.choice((1, -1))
#     # print(x,y)
#     return x, y


def random_walk(steps):
    x, y = 0, 0
    for i in range(steps):
        dx, dy = random.choice(((1, 0), (-1, 0), (0, 1), (0, -1)))
        x += dx
        y += dy
    return x, y


no_trials = 100000
steps = 2
count = 0

for i in range(no_trials):
    x, y = random_walk(steps)
    dist = abs(x) + abs(y)
    if dist == 0:
        count += 1

# chances of ending up back to (0, 0) with specified number of steps
print(count / no_trials)
