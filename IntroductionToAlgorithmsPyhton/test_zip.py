L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in zip(L):
    print(i)

for i in zip(*L):
    print(i)