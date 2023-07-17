def solution(id_list, report, k): 
    hack = {id: [] for id in id_list}

    for case in report:
        a, b = case.split(' ')

        if a not in hack[b]:
            hack[b].append(a)

    result = [0] * len(id_list)
    for idx, user in enumerate(id_list):
        for reported_users in hack.values():
            if user in reported_users and len(reported_users) >= k:
                result[idx] += 1

    return result

