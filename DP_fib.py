import numpy as np

def fib(n:int) -> int:
    table = np.zeros(n + 1)
    table[1] = 1
    for idx in range(2,n+1):
        table[idx] = table[idx - 1] + table[idx - 2]
    
    return table[n]

print(fib(6))
print(fib(1000))

# Time and Space complexity both O(n), just one array