import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최소값과 최대값 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


def maxProfit(prices: List[int]) -> int:
    p = 0
    m_p = sys.maxsize

    for price in prices:
        m_p = min(m_p, p)
        profit = max(p, p - m_p)

    return p
