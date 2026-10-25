s = input()

count = 0
for ch in s:
    if ch not in "aeiouAEIOU":
        count += 1

if count == 0:
    print(0)
else:
    f = 1
    for i in range(1, count + 1):
        f = f * i
    print(f)