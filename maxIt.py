# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

numbers = {}
S = 0

K, M = map(int, input().split())

for i in range(K):
    _, *numbers[i] = map(int, input().split())

S = max(S, max(sum(x ** 2 for x in combo) % M for combo in product(*numbers.values())))

print(S)
