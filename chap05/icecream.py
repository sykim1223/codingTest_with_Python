
from collections import deque

#얼음틀 사이즈
print('#Input n, m: ')
n, m = map(int, input().split())

#얼음틀 정보 입력
print('#Input the information: ')
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

#DFS 메소드 정의
def dfs(x, y):
  #범위 처리
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  
  #미방문 노드라면(연결된 아이스크림이면)
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False
  

#얼음틀에서 생성되는 아이스크림 개수 세기
res = 0 #아이스크림 개수 변수

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      res += 1

print('#The number of icecream: ', res)

"""연결되어 있는 모든 구성을 찾는 것이므로, 탐색을 이용하여 하나의 덩어리를 찾아내는 것이 핵심 아이디어. 

따라서 탐색만 한다면, bfs/dfs 무관함.

만약 그저 '전체 덩어리를 찾는 것'뿐 아니라, '하나의 덩어리 내에서도 탐색 순서 등의 조건'이 달린다면 탐색 방법도 고려해야 함"""