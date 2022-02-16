import heapq
import sys

"""
Dijkstra 문제
"""

input = sys.stdin.readline #빠른 입력
INF = int(1e9)

# 노드 수, 간선 수, 시작점 입력
n,m,x = map(int,input().split())

# 경로 입력
graph= [[] for i in range(n+1)]

for _ in range(m):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))



# 기본적인 다익스트라 알고리즘
def dijkstra(start):
    # 최단거리 배열 초기화
    distance = [INF]*(n+1)
    q = []
    
    # 시작노드 설정
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 현재 노드의 최단 거리(distance[now])가 현재 힙에서 뺀? 노드의 거리(dist)보다 작다면,
        # 이후 코드는 skip하고 반복문 처음으로 돌아감
        if distance[now]<dist:
            continue

        # 인접 노드 탐색
        for j in graph[now]:
            cost = dist + j[1]
            if distance[j[0]] > cost:
                distance[j[0]] = cost
                heapq.heappush(q,(cost,j[0]))
    return distance


result = [0 for i in range(n+1)]

# 각각의 마을에서 파티까지 가는 최단 경로 
route_party = dijkstra(x)


for i in range(1,n+1):
    # 파티에서 마을로 돌아가는 최단 경로
    route_home = dijkstra(i)
    result[i] = route_party[i] + route_home[x]

print(max(result))
