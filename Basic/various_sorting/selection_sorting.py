#선택정렬=================================================
#  : 처리되지 않은 데이터 중 "가장 작은 데이터를 선택하여 맨 앞에 있는 데이터와 바꾸는 방법"

# ****** 선택 정렬 소스코드 ******
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] #가장 작은 원소를 앞으로

print(array)
# ****** ******

#시간복잡도:
  # N번만큼 가장 작은 수를 맨 앞으로 보내야 함. 
  # 따라서 전체 연산 횟수는 O(N^2) = N+(N-1)+(N-2)+ ... + 2  _(상수가 2인 이유는 정렬되지 않은 마지막 요소에 대해 정렬을 수행할 필요가 없기 때문 )


