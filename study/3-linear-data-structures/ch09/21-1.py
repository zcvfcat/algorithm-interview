# 이해 안됨 ㅠㅠㅠㅜ
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 집합으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 전체 집합과 접미사 집합이 일치할때 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''


def removeDuplicateLetters(s: str) -> str:
    print('s : ', s)
    seen = set(s)
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        print("char : ", char)
        print("suffix : ", suffix)
        print('seen : ', seen)
        print('set(suffix) : ', set(suffix))
        # if set(s) == set(suffix):
        # return char + removeDuplicateLetters(suffix.replace(char, ''))
    return ''


print(removeDuplicateLetters("bcabc"))
