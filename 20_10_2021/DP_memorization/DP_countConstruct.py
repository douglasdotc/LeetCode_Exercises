# Write a function that return the number indicating the number of ways that target 
# can be constructed by concatenating elements of the workBank array. 
# The words in the wordBank can be reused.


def countConstruct(target:str, wordBank:list[str], mem = {}) -> int:
    if target in mem:
        return mem[target]

    if target == '':
        return 1
    
    ways = 0
    for word in wordBank:
        length_word = len(word)
        if word == target[:length_word]:
            ways += countConstruct(target[length_word:], wordBank, mem)

    mem[target] = ways
    return mem[target]

print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('purple', ['purp','p','ur','le','purpl']))
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee']))

# Time Complexity
# m = length of target
# n = length of wordBank
# Tree structure, m layers, n times more nodes each --> O(n^m)
# but memorized subtree results --> O(mn)
# substring operation --> O(m)
# the variable ways is independent of the input sizes
# Overall O(nm^2)

# Space Complexity:
# Tree of depth m, every layer has a substring operation on the string target --> O(m^2)
# mem is a hashmap running over the whole process --> O(m)
# Overall O(m^2 + m) --> O(m^2)