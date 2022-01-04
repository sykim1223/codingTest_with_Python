array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  #리스트가 하나 이하의 원소를 담고 있다면 종료
  if len(array) <= 1:
    return array

  pivot = array[0] #피벗은 첫번째 원소로 지정
  tail = array[1:] #피벗을 제외한 리스트가

#피벗을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽에 몰아넣기
  left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
  right_side = [x for x in tail if x> pivot] #분할된 오른쪽 부분

  #분할 이후 왼쪽, 오른쪽 각 부분에서 정렬을 수행하고 전체리스트 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


"""왼쪽 오른쪽 부분으로 몰아넣는 것을 반복하여 정렬을 가능케 함.
해당 코드가 가능한 것은 'x for x in tail if' 문법과 
return의 리스트 합치기가 가능한 덕분임
"""