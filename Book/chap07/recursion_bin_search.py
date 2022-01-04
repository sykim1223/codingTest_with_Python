#재귀함수로 이진 탐색 구현

def binary_search(arr, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  #찾은 경우, 중간점 인덱스 반환
  if arr[mid] == target:
    return mid
  #중간점보다 작은 경우, 왼쪽 확인
  elif arr[mid] > target:
    return binary_search(arr, target, start, mid-1)
  else:
    return binary_search(arr, target, mid+1, end)


#n(원소의 개수), target(찾고자 하는 숫자 입력)
n, target = list(map(int, input().split()))
#전체 원소 입력받기
arr = list(map(int, input().split()))

#이진 탐색 수행 결과
result = binary_search(arr, target, 0, n-1)

if result == None:
  print('(-)찾고자 하는 원소가 없습니다.')
else:
  print(result + 1)
  
