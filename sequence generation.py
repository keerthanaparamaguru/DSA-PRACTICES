N = int(input())

seq = []
for item in input().split():
    seq.append(int(item))

for i in range(6, N):
    next_value = seq[i - 1] + seq[i - 2]
    seq.append(next_value)

for i in range(N):
    print(seq[i], end=" ")
print()