# BFS: 너비우선 탐색. 큐 자료구조 이용 ===========================================
# 각 간선의 가중치가으 동일할 때, 최단 경로 구하기에 사용되기도 함.

# ****** BFS소스코드 예제 ******
from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
  #큐 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  visited[start] = True
  #큐가 빌 때까지 복
  while queue:
    #큐에서 하나의 원소를 뽑아 출력하기
    v = queue.popleft()
    print(v, end=' ')
    #아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

#각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
  [], #그래프 문제의 첫 인덱스는 일반적으로 '1'임. 따라서 0번 인덱스는 비워두도록 함.
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False]*9

bfs(graph, 1, visited)
# ****** ******

