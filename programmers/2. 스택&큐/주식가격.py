
def solution(prices):
    answer = []
    for i in range(len(prices)):
        cur_price = prices[i]
        j = i
        time = 0
        while j < (len(prices)-1):
            j += 1
            time += 1
            com_price = prices[j]
            if cur_price > com_price:
                break
        answer.append(time)

    return answer
