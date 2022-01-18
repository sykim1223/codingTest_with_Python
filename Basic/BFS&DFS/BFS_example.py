#[문제2]미로 탈출 문제
# 캐릭터가 NxM 크기의 직사각형 형태 미로에 갇혔다. 미로에는 여러마리의 괴물이 있어 이를 피해 탈출해야 한다.
# 캐릭터의 위치는 (1,1)이며 미로의 출구는 (N,M)의 위치에 존재하고, 한번에 한 칸씩 이동할 수 있다. 
# 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다.
# 이때 캐릭터가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작칸과 마지막 칸을 모두 포함한다.

# 입력) 첫째 줄에 N,M (4<=N, M<=200) 주어짐. 다음줄에는 N개의 줄에 각각 M개의 정수(0 or 1)로 미로 정보가 주어지며, 이때 각각의 수는 공백 없이 붙어서 제시됨. 또한 시작칸과 마지막 칸은 항상 1임
# 출력) 최소 이동 칸의 개수를 출력

#아이디어: BFS 사용_ 간선의 가중치가 같을 때 최단거리에 좋음
# 따라서 (1,1) 지점부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록
# 5, 6
# 101010
# 111111
# 000001
# 111111
# 111111


# ****** 소스코드 ******
from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()
    #해당 좌표에 대해 상하좌우로 bfs수행
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
    #만약 미로 공간을 벗어나면 무시
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
    #괴물 있으면 안 감
      if graph[nx][ny] == 0:
        continue
    #괴물 없으면 숫자 갱신하고 큐에 넣기
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx, ny))
  
  return graph[n-1][m-1]


n, m = map(int, input("N과 M을 입력해주세요: ").split())
graph = []
print("맵 정보를 입력해주세요: ")
for i in range(n):
  graph.append(list(map(int, input())))

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print("최단거리는", bfs(0,0), "입니다.")

# ****** ******