def fib(n:int, mem = {}) -> int:
    if n in mem:
        return mem[n]
    if n <= 2:
        return 1
    mem[n] = fib(n - 1, mem) + fib(n - 2, mem)
    return mem[n]


print(f"F(50): {fib(50)}")
print(f"F(500): {fib(500)}")
print(f"F(1000): {fib(1000)}")

# Normal Fib recurrsion has a time complexity O(2^n) 
# (n levels, twice more then the last layer as we go deeper into the tree)
# Dynamic programming - memorization memorize results of subtrees and reuse later
# bringing O(2^n) --> O(n)

# Space complexity O(n), n numbers in mem