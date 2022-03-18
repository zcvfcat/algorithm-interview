class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)


def numJewelsInStones(J: str, S: str) -> int:
    a = [s in J for s in S]
    print(a)
    return sum(s in J for s in S)


print(numJewelsInStones("aA", "aAAbbbb"))
