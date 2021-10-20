# Problem link: https://leetcode.com/problems/find-the-town-judge/
# Tags: Google, Apple, Amazon

"""
In a town, there are n people labeled from 1 to n. 
There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing 
that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, 
or return -1 otherwise.


Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:
Input: n = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:
Input: n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3


Constraints:
1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
"""

# Idea:
# Every row of the given array represents a one way directed trustbond
# We can turn the problem into a hashmap to record the trustworthyness 
# of each person

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        num_people = n
        trust_hash = {}
        for t in trust:
            if t[1] not in trust_hash:
                trust_hash[t[1]]  = 1
            else:
                trust_hash[t[1]] += 1

        max_trust    = 0
        max_trust_ID = 0
        for key in trust_hash:
            if trust_hash[key] > max_trust:
                max_trust = trust_hash[key]
                max_trust_ID = key
        
        if max_trust == num_people - 1:
            # Check if this guy trust no person:
            for t in trust:
                if t[0] == max_trust_ID:
                    return -1
        return max_trust_ID