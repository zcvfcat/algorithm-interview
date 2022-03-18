import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)


def removeDuplicateLetters(s: str) -> str:
    counter = collections.Counter(s)
    stack = []
    seen = set()

    for c in s:
        counter[c] -= 1

        if c in seen:
            continue

        while stack and c < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(c)
        seen.add(c)

    return ''.join(stack)


removeDuplicateLetters('acbacdcbc')
