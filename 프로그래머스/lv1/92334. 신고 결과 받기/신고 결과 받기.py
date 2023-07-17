def solution(id_list, report, k):
    answer = {id: 0 for id in id_list}
    hack = {id: [] for id in id_list}

    for case in report:
        a, b = case.split(' ')

        if a not in hack[b]:
            answer[b] += 1
            hack[b].append(a)

    result = [0] * len(id_list)
    for idx, user in enumerate(id_list):
        for reporter, reported_users in hack.items():
            if user in reported_users and len(reported_users) >= k:
                result[idx] += 1
                
    return result