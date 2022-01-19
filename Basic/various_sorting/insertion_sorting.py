
#삽입 정렬 =================================================
#  : 처리되지 않은 데이터를 하나씩 골라 "적절한 위치에 삽입"_ 해당 요소가 어느 위치에 적절한지 매번 계산하여 정렬하는 방식
#선택 정렬에 비해 구현 난이도가 높지만, 보다 빠르게 동작함

#동작 방식:
  # - 앞쪽의 원소는 이미 정렬되어 있다고 가정하고, 뒤쪽의 원소를 앞쪽의 원소 중 한 곳으로 들어가도록 정렬

# ****** 삽입 정렬 소스코드 ******
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): #첫번째 요소는 0번 인덱스의 요소는 이미 정렬된 상태이기 때문에, 1부터 시작
  for j in range(i, 0, -1): #인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
    if array[j] < array[j-1]: #한 칸씩 왼쪽으로 이동
      array[j], array[j-1] = array[j-1], array[j]
    else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
      break

print(array)
# ****** ******

#시간복잡도 : O(N^2).
  # 그러나 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작함.
  # 최선의 경우 O(N)의 시작 복잡도를 가짐




