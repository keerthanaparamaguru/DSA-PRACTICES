N = int(input())

A = []
for i in range(N):
    value = int(input())
    A.append(value)

count = 0

for split in range(1, N):
    left_sum = 0
    for i in range(0, split):
        left_sum = left_sum + A[i]

    right_sum = 0
    for i in range(split, N):
        right_sum = right_sum + A[i]

    difference = abs(left_sum - right_sum)

    if difference % 2 == 0:
        count = count + 1

print(count)