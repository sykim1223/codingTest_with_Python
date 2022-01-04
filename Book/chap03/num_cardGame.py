#숫자 카드 게임_p96
'''nxm 개수의 카드가 있을 때, 먼저 뽑고자하는 카드가 포함된 행 선택.
이후 선택된 행에 포함된 카드 중 가장 숫자가 낮은 카드를 선택.
이렇게 뽑힌 카드는 각 행의 가장 작은 숫자 중 가장 큰 수이어야 함'''

#getting inputs n, m
n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_num = min(data)
  result = max(result, min_num)

print(result)
