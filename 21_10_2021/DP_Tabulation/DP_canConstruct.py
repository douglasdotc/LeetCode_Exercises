# Write a function that return a boolean indicating whether the target can be constructed 
# by concatenating elements of the workBank array. The words in the wordBank can be reused.

def canConstruct(target:str, wordBank:list[str]) -> bool:
    # [T,F,F,F,F,F,F] Each entry represents the possibility of constructing a prefix of the target up to that index
    #  a,b,c,d,e,f

    len_canConstructT = len(target) + 1
    canConstructT = [False]*len_canConstructT
    canConstructT[0] = True
    for t_idx in range(len_canConstructT):
        if canConstructT[t_idx]:
            for word in wordBank:
                if word == target[t_idx:t_idx+len(word)]:
                    canConstructT[t_idx + len(word)] = True
    
    return canConstructT[len(target)]

print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee']))

# Time Complexity:
# Let m = length of target
# n = length of wordBank
# double for loop --> O(mn)
# checking if word == target[...] --> target is at most of length m --> O(m)
# Overall O(nm^2)

# Space Complexity:
# canConstructT --> O(m)
