N = int(input())
L = int(input())
R = int(input())

A = []
for i in range(N):
    value = int(input())
    A.append(value)

level = 0
highest = 0
lowest = 0

for x in A:
    if x >= L and x <= R:
        level = level + 1
    else:
        level = level - 1

    if level > highest:
        highest = level

    if level < lowest:
        lowest = level

print(highest, lowest)