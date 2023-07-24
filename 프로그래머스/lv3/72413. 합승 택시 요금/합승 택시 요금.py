def solution(n, s, a, b, fares):
    INF = int(1e9)   
    answer = INF 

    # 2차원 리스트(그래프)를 만들고, 무한으로 초기화
    graph=[[INF]*(n) for _ in range(n)]


    # 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화
    for i in range (n):
         graph[i][i]=0


    # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
    for info in fares:
        # c - d 사이 요금을 f라고 설정
        c,d,f= info
        graph[c-1][d-1]=f
        graph[d-1][c-1]=f

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


    # 노드 s에서 출발해 a,b각각에 대한 최소 요금 경로를 계산
    # 최종 요금 = a+b 합동요금 + a 요금 + b 요금
    for i in range(n):
        cost = graph[s-1][i] + graph[i][a-1] + graph[i][b-1]
        answer = min(answer, cost)

    return answer
