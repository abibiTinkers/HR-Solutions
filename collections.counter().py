# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
sizes = Counter(map(int, input().split()))

n = int(input())
amount = 0
for _ in range(n):
    ct_size, price = list(map(int, input().split()))
    
    if ct_size in sizes.keys() and sizes[ct_size] != 0:
        sizes[ct_size] -= 1
        amount += price

print(amount)
