'''1이 될때까지_p99
'''
import time

#getting inputs n, m
n, m = map(int, input().split())

#start TimeoutError
start_time = time.time()

cnt = 0

while n != 1 :
  if n%m == 0:
    n //= m
  else:
    n -= 1
  cnt += 1

print(cnt)

end_time = time.time()
print("Perform: ", end_time - start_time)