# given a grid of size mxn, 
# return the number of ways to reach the lower right corner from the upper left corner

import numpy as np
def gridTraveler(m:int, n:int) -> int:
    table = np.zeros((m+1, n+1))
    # table[1][1] = 1

    for m_idx in range(1, m+1):
        for n_idx in range(1, n+1):
            table[m_idx][n_idx] = table[m_idx-1][n_idx] + table[m_idx][n_idx-1]
            if m_idx == 1 and n_idx == 1:
                table[m_idx][n_idx] = 1
    
    return table[m][n]

print(gridTraveler(3, 3))
print(gridTraveler(18, 18))
print(gridTraveler(500, 500))

# 2D array, time and space complexity --> O(mn)

# Can we get rid of double for loop?
