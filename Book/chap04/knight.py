
#사용자에게 현재 위치를 입력받기
pos = input()

column = int(ord(pos[0])) - int(ord('a'))+1
row = int(pos[1])

cnt = 0

#움직임의 종류를 정의 
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

#현재위치에서 가능한 움직임의 종류를 판단
for step in steps:
  dc = column + step[0]
  dr = row + step[1]
  
  if dc <= 8 and dc >= 1 and dr <= 8 and dr >= 1:
    cnt +=1

print(cnt)