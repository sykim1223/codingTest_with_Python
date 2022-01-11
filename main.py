# ‘쩰리’는 점프하는 것을 좋아하는 젤리다. 단순히 점프하는 것에 지루함을 느낀 ‘쩰리’는 새로운 점프 게임을 해보고 싶어 한다. 새로운 점프 게임의 조건은 다음과 같다.

#   1. ‘쩰리’는 가로와 세로의 칸 수가 같은 정사각형의 구역 내부에서만 움직일 수 있다. ‘쩰리’가 정사각형 구역의 외부로 나가는 경우엔 바닥으로 떨어져 즉시 게임에서 패배하게 된다.
#   2. ‘쩰리’의 출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸이다. 다른 출발점에서는 출발하지 않는다.
#   3. ‘쩰리’가 이동 가능한 방향은 오른쪽과 아래 뿐이다. 위쪽과 왼쪽으로는 이동할 수 없다.
#   4. ‘쩰리’가 가장 오른쪽, 가장 아래 칸에 도달하는 순간, 그 즉시 ‘쩰리’의 승리로 게임은 종료된다.
#   5. ‘쩰리’가 한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼이다. 칸에 쓰여 있는 수 초과나 그 미만으로 이동할 수 없다.

# 새로운 게임이 맘에 든 ‘쩰리’는, 계속 게임을 진행해 마침내 최종 단계에 도달했다. 하지만, 게임을 진행하는 구역이 너무 넓어져버린 나머지, 이 게임에서 이길 수 있는지 없는지 가늠할 수 없어졌다. ‘쩰리’는 유능한 프로그래머인 당신에게 주어진 구역에서 승리할 수 있는 지 알아봐 달라고 부탁했다. ‘쩰리’를 도와 주어진 게임 구역에서 끝 점(오른쪽 맨 아래 칸)까지 도달할 수 있는지를 알아보자!

# 입력) 첫 번째 줄에는 게임 구역의 크기 N (2 ≤ N ≤ 3)이 주어진다.
#       두 번째 줄부터 마지막 줄까지 게임판의 구역(맵)이 주어진다.
# 게임판의 승리 지점(오른쪽 맨 아래 칸)에는 -1이 쓰여있고, 나머지 칸에는 0 이상 100 이하의 정수가 쓰여있다.

# 출력) ‘쩰리’가 끝 점에 도달할 수 있으면 “HaruHaru”(인용부호 없이), 도달할 수 없으면 “Hing” (인용부호 없이)을 한 줄에 출력합니다.

from collections import deque

def path_find(x, y):
  #큐 생성하고 시작 위치 삽입
  queue = deque()
  queue.append((x,y))
  #큐가 빌 때 까지 탐색
  while queue:
  #현 좌표의 이동횟수 만큼 이동
    x, y = queue.popleft() #현재 좌표
    print(x, y)
    m = map_info[x][y] #현재 좌표에 적힌 이동횟수
    if m == -1:
      return -1
    if m == 0:
      continue
  # #가능한 이동 경로 확인
    for i in range(m+1): #이동경우의 수는 m+1만큼 이니까
  #각 경우에 대해 이동후 좌표 계산
      nx = x + (i*dx[0]) + ((m-i)*dx[1])
      ny = y + (i*dy[0]) + ((m-i)*dy[1])   
 
  # 이동한 좌표가 범위를 벗어나면 스킵
      if 0 <= nx < n and 0 <= ny < n:
        queue.append((nx, ny))

  return 0

n = int(input())

map_info = []
for i in range(n):
  map_info.append(list(map(int, input().split())))

  #이동좌표_우 하
dx = [0, 1] #행
dy = [1, 0] #열

if path_find(0,0) == -1:
  print('HaruHaru')
else:
  print('Hing')





n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))


def finder(x, y, gap):

    if gap == -1:
        print("HaruHaru")
        exit(0)
    if gap == 0:
      print("Hing")
      exit(0)
    if 0 <= x+gap < n:
      print("down: 현재 좌표", x+gap, y)
      finder(x+gap, y, l[x+gap][y])  # down
    if 0 <= y+gap < n:
      print("right: 현재 좌표", x, y+gap)
      finder(x, y+gap, l[x][y+gap])  # right

x = 0
y = 0
gap = l[x][y]
finder(x, y, gap)
print("Hing")