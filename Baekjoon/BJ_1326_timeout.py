# 문제1326)
# 개구리가 일렬로 놓여 있는 징검다리 사이를 폴짝폴짝 뛰어다니고 있다. 징검다리에는 숫자가 각각 쓰여 있는데, 이 개구리는 매우 특이한 개구리여서 어떤 징검다리에서 점프를 할 때는 그 징검다리에 쓰여 있는 수의 배수만큼 떨어져 있는 곳으로만 갈 수 있다.

# 이 개구리는 a번째 징검다리에서 b번째 징검다리까지 가려고 한다. 이 개구리가 a번째 징검다리에서 시작하여 최소 몇 번 점프를 하여 b번째 징검다리까지 갈 수 있는지를 알아보는 프로그램을 작성하시오.

# 입력)
# 첫째 줄에 징검다리의 개수 N(1≤N≤10,000)이 주어지고, 이어서 각 징검다리에 쓰여 있는 N개의 정수가 주어진다. 그 다음 줄에는 N보다 작거나 같은 자연수 a, b가 주어지는 데, 이는 개구리가 a번 징검다리에서 시작하여 b번 징검다리에 가고 싶다는 뜻이다. 징검다리에 쓰여있는 정수는 10,000보다 작거나 같은 자연수이다.

# 출력)
# 첫째 줄에 개구리가 a번 징검다리에서 b번 징검다리로 최소 몇 번 점프하여 갈 수 있는 지를 출력하시오. a에서 b로 갈 수 없는 경우에는 -1을 출력한다.


def frog_jump(arr, n, a, b):
  d = 0
  arr[b] = pivot = 2*n
  
  for i in range(n):
    for j in range(len(arr)):
      if arr[j] < pivot:
        continue
      for k in range(len(arr)):
        d = abs(j-k)
        if arr[k] < pivot and d % arr[k] == 0:
          arr[k] = pivot + i + 1
    if arr[a] > pivot:
        return arr[a]-pivot
  
  return -1

n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

print(frog_jump(arr, n, a-1, b-1))

