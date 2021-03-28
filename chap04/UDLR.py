
#getting a input n
n = int(input())

moving = input().split()

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for move in moving:
  for m_type in range(len(move_type)):
    if move == move_type[m_type]:
      nx = x + dx[m_type]
      ny = y + dy[m_type]
  if ny < 1 or ny> n or nx <1 or nx >n:
    continue
  x = nx
  y = ny

print(x ,y)