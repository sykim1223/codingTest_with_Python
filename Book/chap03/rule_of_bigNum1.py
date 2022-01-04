# 큰수의 법칙_p93
# N개의 숫자 주어졌을 때, 주어진 수들을 M번 더하여 가장 큰 수 만들기. 단, 특정 인덱스의 수가 연속해서 K번 초과하여 더할 수 없음

#getting input n, m, k
n, m, k = map(int, input().split())

#getting n data
data = list(map(int, input().split()))

#sorting a data list
data.sort()
s_num = max_num = data[n-1]
scd_num = data[n-2]

print(max_num, scd_num, s_num)

result = 0

while m != 0:
  for i in range(k):
    result += s_num
    m -= 1
    if m == 0:
      break
  if s_num == max_num:
    s_num = scd_num
  else:
    s_num = max_num

print(result)

#내 풀이의 문제는 다음과 같다.
# '가장 큰 수'를 구한 것이 아니라는 것 -> 문제를 정확히 읽고 인지할 필요 있음