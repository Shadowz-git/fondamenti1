A = []

for i in range(26):
    A.append(input())

N = int(input())
B = []

for i in range(N):
    B.append(int(input()))

for X in B:
    if X < 26:
        print(A[X], end="")
