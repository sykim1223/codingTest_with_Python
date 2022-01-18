# 퀵 정렬 ========================================================
#  : "기준 데이터를 설정"하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
      # 가장 기본 적은 퀵 정렬은 첫번째 데이터를 기준데이터(Pivot)로 설정

# 동작 방법: 
  #   - 왼쪽에서부터 피벗보다 "큰" 데이터 선택, 오른쪽에서부터 피벗보다 "작은" 데이터 선택
  #   - 두 데이터의 위치를 서로 변경
  #   - 해당 과정을 반복하다가 "큰" 데이터와 "작은" 데이터의 위치가 엇갈리게 되면(위치를 변경할 필요 없이, 이미 작은 데이터가 큰 데이터의 왼편에 위치하게 되면) -> "작은" 데이터와 피벗의 위치를 변경
  #   - 이제 피벗을 기준으로 "왼쪽"에는 피벗보다 작은 값만 존재하고 "오른쪽"에는 피벗보다 큰 값만 존재하게 됨 (분할된 상태)
  #   - ["왼쪽" 데이터 묶음 정렬] 왼쪽에 대해 위의 과정을 수행
  #   - ["오른쪽" 데이터 묶음 정렬] 오른쪽에 대해 위의 과정을 수행
  # => 재귀적으로 수행! (재귀적으로 수행될 때 마다 작업의 크기가 작아지는 것을 확인)

# 시간 복잡도: 평균의 경우, O(NlogN) 임. 단, 최악의 경우 O(N^2)임. _ 피벗을 정하는 방법에 따라 최악의 경우가 될 수 있음

# ****** 기본 소스코드 ******
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: #원소가 1개인 경우 종료
    return
  pivot = start #피벗은 첫 번째 원소
  left = start + 1
  right = end

  while(left <= right): #엇갈릴 때 까지 반복
    #피벗보다 큰 데이터를 찾을 때 까지 반복
    while(left <= end and array[left] <= array[pivot]):
      left += 1
    #피벗보다 작은 데이터를 찾을 때 까지 반복
    while(right > start and array[right] >= array[pivot]):
      right -= 1
    if(left > right): #엇갈렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
      array[left], array[right] = array[right], array[left]
  #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right-1) #right가 교체된 후 피벗이 위치한 인덱스임
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

# ****** ******

# ******파이썬의 장점을 살린 퀵 정렬 소스코드 ******
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
#리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array
  pivot = array[0] #피벗은 첫 번째 원소
  tail = array[1:] #피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분_pivot보다작은 것을 넣은 리스트
  right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분_리스트 컴프레션 이용

  #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))

# ****** ******


