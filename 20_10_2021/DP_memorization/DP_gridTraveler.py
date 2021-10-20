# given a grid of size mxn, 
# return the number of ways to reach the lower right corner from the upper left corner

def gridTraveller(m:int, n:int, mem = {}) -> int:
    if (m,n) in mem:
        return mem[(m,n)]
    if (n,m) in mem:
        return mem[(n,m)]

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    mem[(m,n)] = gridTraveller(m - 1, n, mem) + gridTraveller(m, n - 1, mem)
    return mem[(m,n)]

print(gridTraveller(250, 250))

# Time complexity:
# Since we have a mem to memorize the results of smaller grid, many sub trees in the grand
# tree can be ignored. Given a pair of m and n, the total combination of results in mem are mn
# So time complexity is O(mn)

# Space Complexity:
# the deepest node of the tree should be at m+n --> O(m+n)