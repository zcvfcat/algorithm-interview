def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge = [truck_weights.pop(0)]
    bridge_weight = bridge[0]
    bridge_check = [1]

    while len(bridge) != 0:
        answer += 1
        if len(bridge_check) != 0 and answer - bridge_check[0] == bridge_length:
            bridge_weight -= bridge[0]
            bridge.pop(0)
            bridge_check.pop(0)

        if len(truck_weights) != 0 and bridge_weight + truck_weights[0] <= weight:
            next_truck = truck_weights.pop(0)
            bridge.append(next_truck)
            bridge_check.append(answer)
            bridge_weight += next_truck

    return answer
