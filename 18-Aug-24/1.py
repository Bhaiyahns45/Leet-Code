s = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i, j = 4, 5
i, j = 4, 7
i, j = 2, 3

sum = 0

for i in range(i, j + 1):
    sum += s[i]


print(sum)
