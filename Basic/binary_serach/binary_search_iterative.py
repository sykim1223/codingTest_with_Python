#이진탐색 알고리즘
# - 순차탐색: 리스트 안에 있는 특정 데이터를 찾기 위해 "앞에서부터 데이터를 하나씩 확인"
# - 이진 탐색: "정렬되어 있는" 리스트에서 "탐색 범위를 절반씩 좁혀가며 테이터를 탐색"하는 방법 (O(logN))
#           -> 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정 



# ****** 이진탐색 반복문 구현 소스코드 ******
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start+end)//2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid-1
    else:
      start = mid+1

  return None


n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
  print("찾으시는 원소가 존재하지 않습니다.")
else:
  print(result+1)