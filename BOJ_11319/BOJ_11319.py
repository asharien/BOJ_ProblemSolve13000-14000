import sys
V = list("AEIOUaeiou")
for _ in range(int(sys.stdin.readline())):
    X = str(sys.stdin.readline().rstrip())
    C, B = 0, 0
    for i in X:
        if i in V: C += 1
        elif i == ' ': B += 1
    print(len(X)-C-B, C)
