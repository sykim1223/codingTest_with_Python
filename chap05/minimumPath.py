from collections import deque

# N,M 입력받기
n, m = map(int, input().split())

#2d로 맵 정보 받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

#이동할 방향 정의(상,하,좌,우 순서)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS 코드
def bfs(x, y):
  #큐 구현
  queue = deque()
  queue.append((x, y))
  #큐가 빌 때까지 아래 탐색 반복
  while queue:
    x, y = queue.popleft()
    #현재 위치에서 상하좌우 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      #맵 벗어난 경우 제외
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      #벽인 경우 무시
      if graph[nx][ny]==0:
        continue
      #해당 노드 처음 방문하는 경우, 이동횟수 추가
      if graph[nx][ny]==1:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx, ny))
  return graph[n-1][m-1]

#BFS 수행 결과
print(bfs(0,0))


"""핵심 2가지
  핵심1: BFS를 이용하여 탐색하는 것. BFS는 가장 가까운 노드부터 탐색한다는 특징이 있음. 따라서 가장 먼 곳부터 탐색을 시작하는 DFS와 달리, 현재 노드에서 가까운 다음노드를 순차적으로 탐색하므로 해당 문제 해결에 적합함
  
  핵심2: 35줄의 (다음탐색 노드의 값)=(현재 노드의 값)+1. 탐색을 하다보면 의미없는 노드까지 탐색해야 하고, 이 과정에서 이동횟수가 적절치않게 증가할 수 있음. 35줄과 같이 노드의 값을 처리함으로써, 실제 이동횟수 증가에 유의미한 이동만 더함으로써 올바른 해답을 구할 수 있음"""