from itertools import product 

def solution(numbers, target):
 ans = 0
 cases = product([1,-1], repeat=len(numbers))
 for case in cases:
  if target == sum(map(lambda a:a[0]*a[1] ,zip(case, numbers))):
   ans += 1
 return ans

def dfs(result, numbers, target):
    if len(numbers) == 1:
        if result + numbers[0] == target or result - numbers[0] == target:
            return 1
        else:
            return 0
    else:
        return dfs(result + numbers[0], numbers[1:], target) + dfs(result - numbers[0], numbers[1:], target)


def solution(numbers, target):
    answer = dfs(0, numbers, target)
    return answer


def test1():
    assert solution([1, 1, 1, 1, 1], 3) == 5


def test2():
    assert solution([4, 1, 2, 1], 4) == 2
