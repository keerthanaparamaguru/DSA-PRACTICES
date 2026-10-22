N = int(input())

A = []
for i in range(N):
    value = int(input())
    A.append(value)

count = 0

for i in range(0, N - 2):
    first = A[i]
    second = A[i + 1]
    third = A[i + 2]

    if first + third == second:
        count = count + 1

print(count)