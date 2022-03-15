import copy


def solution(tickets):
    answer = []
    ways = {}
    ticket_count = len(tickets)
    for t in tickets:
        if t[0] in ways:
            ways[t[0]].append(t[1])
        else:
            ways[t[0]] = [t[1]]

    for arrival in ways['ICN']:
        temp = copy.deepcopy(ways)
        temp['ICN'].pop(temp['ICN'].index(arrival))
        answer += dfs('ICN', arrival, temp, 0, ticket_count)

    return sorted(answer)[0].split(',')


def dfs(history, departure, ways, count, ticket_count):
    histories = []
    history += ','+departure
    count += 1
    if count == ticket_count:
        return [history]
    if departure in ways:
        for arrival in ways[departure]:
            temp = copy.deepcopy(ways)
            temp[departure].pop(temp[departure].index(arrival))
            histories += dfs(history, arrival, temp, count, ticket_count)

    return histories


def test1():
    assert solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == [
        "ICN", "JFK", "HND", "IAD"]


def test2():
    assert solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], [
                    "ATL", "SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
