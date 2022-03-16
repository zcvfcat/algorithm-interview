from typing import List
from itertools import product


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out


def productExceptSelf(nums: List[int]) -> List[int]:
    out = []

    p = 1
    for v in nums:
        out.append(p)
        p = p * v

    p = 1

    for i in range(len(nums) - 1, -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out


print(productExceptSelf([1, 2, 3, 4]))
