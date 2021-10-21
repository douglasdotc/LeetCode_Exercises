# Write a function that return the number indicating the number of ways that target 
# can be constructed by concatenating elements of the workBank array. 
# The words in the wordBank can be reused.

def countConstruct(target:str, wordBank:list[str]) -> int:
    # [1,0,0,0,0,0,0] Each entry represents the possibility of constructing a prefix of the target up to that index
    #  a,b,c,d,e,f
    len_countConstructT = len(target) + 1
    countConstructT = [0]*len_countConstructT
    countConstructT[0] = 1

    for t_idx in range(len_countConstructT):
        for word in wordBank:
            if word == target[t_idx:t_idx+len(word)]:
                countConstructT[t_idx + len(word)] += countConstructT[t_idx]
    return countConstructT[len(target)]

print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('purple', ['purp','p','ur','le','purpl']))
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee']))

# Time Complexity: 
# Let m = length of target
# n = length of wordBank
# double for loop --> O(mn)
# checking if word == target[...] --> target is at most of length m --> O(m)
# Overall O(nm^2)

# Space Complexity:
# canConstructT --> O(m)