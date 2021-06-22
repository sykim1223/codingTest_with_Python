'''p118
답안 예시'''

#n, m 공백으로 구분하여 입력받기
n, m = map(int, input().split())

#방문한 위치 저장하기 위한 맵 생성 후 0으로 초기화
d = [[0]*m for _ in range(n)]
#현재 캐릭터의 x, y 좌표, 방향 입력받기
x, y, direction = map(int, input().split())
#현재 위치 방문 처리
d[x][y] = 1

#전체 맵 정보 받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

  #북,동,남,서 방향 정의
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]

  #왼쪽으로 회전
  def turn_left():
    global direction
    direction -= 1
    if direction == -1:
      direction = 3

  #시뮬레이션 시작
  count = 1 
  turn_time = 0
  while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
      d[nx][ny] = 1
      x = nx
      y = ny
      count += 1
      turn_time = 0
      continue
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else: 
      turn_time += 1
    
    if turn_time == 4:
      nx = x - dx[direction]
      ny = y - dy[direction]
      #뒤로 갈 수 있다면 이동하기
      if array[nx][ny] == 0:
        x = nx
        y = ny
      #뒤가 바다로 막혀있는 경우
      else:
        break
      turn_time = 0

#정답 출력
print(count)

'''나와의 차이점 및 배울점
1. 나는 뒤로가는 경우의 리스트도 생성했는데,
   -> 앞으로 가는 리스트만 만들어서 
   -> 앞으로 가는 경우에는 x + dx[dir]
   ->   뒤로 가는 경우에는 x - dx[dir]
   -> 즉, 중간 부호만 바꾸면 앞뒤가 달라져...!
2. 나는 count 를 위해 2중 for문을 돌리는데, 굳이 안그래도 됐어'''