B = (2, 0)
C = (7, 7)
D = (3, 9)
E = (9, 1)
F = (5, 8)
min = 1000000
for i in range(10):
    for j in range(10):
        l = abs((i-B[0])) + abs((j-B[1])) + 3 * (abs((i-C[0])) + abs((j-C[1]))) + 2 * (abs((i-D[0])) + abs((j-D[1]))) + abs((i-E[0])) + abs((j-E[1])) + abs((i-F[0])) + abs((j-F[1]))
        if l < min or min == 0:
            min = l
            x = i
            y = j
print("The point that minimizes the sum of distances is:", (min, x, y))

i = 5
j = 6
l = abs((i-B[0])) + abs((j-B[1])) + 3 * (abs((i-C[0])) + abs((j-C[1]))) + 2 * (abs((i-D[0])) + abs((j-D[1]))) + abs((i-E[0])) + abs((j-E[1])) + abs((i-F[0])) + abs((j-F[1]))
print(l)
