# Write a function that return a 2D array that contain all the ways that target 
# can be constructed by concatenating elements of the workBank array. 
# The words in the wordBank can be reused.
# Each element of the 2D array should represent one combination that constructs the target.

import copy
def allConstruct(target:str, wordBank:list[str]) -> list[list[str]]:
    len_allConstructT = len(target) + 1
    allConstructT = [[]]*len_allConstructT
    allConstructT[0] = [[]]

    for t_idx in range(len_allConstructT):
        for word in wordBank:
            if word == target[t_idx:t_idx + len(word)]:
                # append new word to every entry of target[t_idx]
                newWays = appendWord(word, allConstructT[t_idx])
                # append new ways to target[t_idx + len(word)]
                allConstructT[t_idx + len(word)].append(newWays)
    
    return allConstructT[len(target)]

def appendWord(word:str, com:list[list[str]]) -> list[list[str]]:
    new_com = com
    for c_idx in range(len(new_com)):
        new_com[c_idx].append(word)
    return copy.deepcopy(new_com)

print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
# print(allConstruct('purple', ['purp','p','ur','le','purpl']))
# print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
# print(allConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
# print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee']))

# Time Complexity
