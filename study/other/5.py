import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            print(anagrams[''.join(sorted(word))])
            anagrams[''.join(sorted(word))].append(word)

        return [v for v in anagrams.values()]


print(Solution.groupAnagrams("", ["eat", "tea", "tan", "ate", "nat", "bat"]))

# def test():
#     assert Solution.groupAnagrams(
#         "", ["eat", "tea", "tan", "ate", "nat", "bat"]) == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
