N = int(input())

A = []
for i in range(N):
    value = int(input())
    A.append(value)

for i in range(N):
    left = A[(i - 1 + N) % N]     
    right = A[(i + 1) % N]       

    greater_count = 0
    if left > A[i]:
        greater_count = greater_count + 1
    if right > A[i]:
        greater_count = greater_count + 1

    print(greater_count, end=" ")
print()