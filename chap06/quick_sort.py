array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):#배열, 피벗위치,배열의크기-1
  if start >= end:#원소가 하나인 경우, 종료
    return
  pivot = start #피벗은 첫번째 원소
  left = start+1 #왼쪽부터 피벗보다 큰 원소 찾기위한 인덱스
  right = end #오른쪽부터 피벗보다 작은 원소 찾기위한 인덱스
  while left <=right: #피벗이 작은 데이터와 교체되지 않았다면
    #피벗보다 큰 데이터 찾을때까지 반복
    while left <= end and array[left]<=array[pivot]:
      left += 1
    #피벗보다 작은 데이터를 찾을때까지 반복
    while right > start and array[right]>=array[pivot]:
      right -= 1
    if left >right: #엇가렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: #엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
      array[left], array[right] = array[right], array[left]
  #분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
