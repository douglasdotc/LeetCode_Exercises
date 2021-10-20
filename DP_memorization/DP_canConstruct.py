# Write a function that return a boolean indicating whether the target can be constructed 
# by concatenating elements of the workBank array. The words in the wordBank can be reused.


def canConstruct(target:str, wordBank:list[str], mem = {}) -> bool:
    if target in mem:
        return mem[target]

    if target == '':
        return True

    for word in wordBank:
        word_len = len(word)
        if word == target[:word_len]:
            if canConstruct(target[word_len:], wordBank, mem):
                mem[target] = True
                return mem[target]
    
    mem[target] = False
    return mem[target]

print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee'], {}))

# Time Complexity
# m = length of target
# n = length of wordBank
# Tree structure, m layers, n times more nodes each --> O(n^m)
#  but memorized subtree results --> O(mn)
# substring operation --> O(m)
# Overall O(nm^2)

# Space Complexity:
# Tree of depth m, every layer has a substring operation on the string target --> O(m^2)
# mem is a hashmap running over the whole process --> O(m)
# Overall O(m^2 + m) --> O(m^2)