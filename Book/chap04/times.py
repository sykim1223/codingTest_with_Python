
#getting a input n
n = int(input())

cnt = 0

for hour in range(n+1): #0시간이더라도 0시59분59초까지는 카운트하므로 +1 필요
  for minute in range(60):
    for sec in range(60):
      if '3' in str(hour)+str(minute)+str(sec):
        cnt += 1

print(cnt)