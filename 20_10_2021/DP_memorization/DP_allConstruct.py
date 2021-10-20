# Write a function that return a 2D array that contain all the ways that target 
# can be constructed by concatenating elements of the workBank array. 
# The words in the wordBank can be reused.
# Each element of the 2D array should represent one combination that constructs the target.

def allConstruct(target:str, wordBank:list[str], mem = {}) -> list[list[str]]:
    if target in mem:
        return mem[target]

    if target == '':
        return [[]]
    
    allWays = []
    for word in wordBank:
        length_word = len(word)
        if word == target[:length_word]:
            ways    = allConstruct(target[length_word:], wordBank, mem)
            ways    = insertWord(word, ways)
            allWays = appendResults(allWays, ways)

    mem[target] = allWays
    return mem[target]

def insertWord(word:str, ways:list[list[str]]) -> list[list[str]]:
    for w_idx in range(len(ways)):
        ways[w_idx] = [word] + ways[w_idx]
    return ways

def appendResults(allWays:list[list[str]], ways:list[list[str]]) -> list[list[str]]:
    for w_idx in range(len(ways)):
        allWays.append(ways[w_idx])
    return allWays

print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], {}))
print(allConstruct('purple', ['purp','p','ur','le','purpl'], {}))
print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
print(allConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee'], {}))

# Time Complexity
# m = length of target
# n = length of wordBank
# Tree structure, m layers, n times more nodes each --> O(n^m)
# but memorized subtree results --> O(mn)
# substring operation and inserting --> O(m)
# the variable ways is independent of the input sizes
# Overall O(nm^2)

# Space Complexity:
# Tree of depth m, every layer has a substring operation on the string target --> O(m^2)
# mem is a hashmap running over the whole process --> O(m)
# Overall O(m^2 + m) --> O(m^2)