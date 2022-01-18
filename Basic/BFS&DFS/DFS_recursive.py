# ****** DFS로 그래프 탐색 예제 ******

#DFS 메서드 정의
def dfs(graph, v, visited):
  visited[v] = True #시작 노드는 즉시 방문처리
  print(v, end=' ')
  #현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)


# #각 노드가 연결된 정보를 표현(2차원 리스트)
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
visited = [False]*9 #인덱스 0은 사용하지 않기 위해, 일부러 노드보다 하나 더 많은 공간을 할당

dfs(graph, 1, visited)
****** ******

