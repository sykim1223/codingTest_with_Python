'''p118
내가 구현한 것'''

#맵의 크기
print('#Input map size by row column: ')
n, m = map(int, input().split())

#현위치 좌표값, 방향
print('#Input current location, direction: ')
a, b, direction = map(int, input().split())

#방문한 칸의 수
cnt = 0

#맵 정보 입력
print('#Input map information: ')
map_inf = []
for i in range(n):
  map_inf.append(list(map(int, input().split())))


#현위치 왔다감을 표시
map_inf[a][b] = 2

#몇개의 방향을 확인했는지 나타내는 변수
canGo = 4

#북, 동, 남, 서 별 이동방향
ahead = [(-1, 0), (0, 1), (1, 0), (0, -1)]
back = [(1, 0), (0, -1), (-1, 0), (0, 1)]

while True:
  while True:
#왼쪽으로 회전
    direction = (direction-1)%4
#앞으로 한칸 이동
    da = a+ahead[direction][0]
    db = b+ahead[direction][1]
#이동이 가능한지 확인
    if da >= 0 and da < n and db >= 0 and db < m and map_inf[da][db] == 0 :
      a = da
      b = db
      map_inf[a][b] = 2
      canGo = 4
      continue
#이동할 수 없는 곳이면 원래 좌표값 유지
    else: 
      canGo -=1
    
#4방향 모두 간 곳이거나, 바다이면 바라보는 방향 유치한채 한칸 뒤로가고 처음으로
    if canGo == 0:
      break
#이때 뒤쪽이 바다이면 종료
  da = a+back[direction][0]
  db = b+back[direction][1]

  if da >= 0 or da < n or db >= 0 or db < m or map_inf[da][db] == 1:
    break
  else:
    a = da
    b = db
    map_inf[a][b] = 2
    canGo = 4

for mapRow in map_inf:
  for mapCnt in range(len(mapRow)):
    if mapRow[mapCnt] == 2:
      cnt+=1

print(cnt) 

