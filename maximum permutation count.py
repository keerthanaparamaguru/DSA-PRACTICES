words = input().split()

most = 0
for w in words:
    count = 0
    for ch in w:
        if ch not in "aeiouAEIOU":
            count += 1
    if count > most:
        most = count

if most == 0:
    print(0)
else:
    f = 1
    for i in range(1, most + 1):
        f = f * i
    print(f)