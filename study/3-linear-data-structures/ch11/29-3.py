import collections


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = collections.Counter(S)  # 돌(S) 빈도 수 계산
        count = 0

        # 비교 없이 보석(J) 빈도 수 합산
        for char in J:
            count += freqs[char]

        return count


def numJewelsInStones(J: str, S: str) -> int:
    # freqs = collections.Counter(S)  # 돌(S) 빈도 수 계산
    freqs = collections.Counter(['a', 'A', 'A', 'b', 'b', 'b', 'b'])  # 돌(S) 빈도 수 계산
    count = 0

    # 비교 없이 보석(J) 빈도 수 합산
    for char in J:
        count += freqs[char]

    return count


print(numJewelsInStones("aA", "aAAbbbb"))
