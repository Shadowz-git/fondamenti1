x = int(input())
y = int(input())
somma = 0

if x % 2 == 0:
    x += 1

for i in range(x, y+1, 2):
    somma += i

print(somma, end="")
