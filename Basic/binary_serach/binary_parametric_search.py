# 파이썬 이진 탐색 라이브러리 ============================================
#   - bisect_left(a, x): 정렬된 순서를 유지하면서 배열a에 x를 삽입할 가장 왼쪽 인덱스 반환
#   - bisect_right(a, x): 정렬된 순서를 유지하면서 배열a에 x를 삽입할 가장 오른쪽 인덱스를 반환

#  ****** 사용 예시 ******
# from bisect import bisect_left, bisect_right

# a = [1, 2, 4, 4, 8]
# x = 4 

# print(bisect_left(a, x))
# print(bisect_right(a, x))

# ****** ******


#해당 함수를 이용해서 값이 특정 범위에 속하는 데이터의 개수를 구할 수 있음
# ****** 소스코드 ******
# from bisect import bisect_left, bisect_right

# #값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
# def count_by_range(a, left_value, right_value):
#   right_index = bisect_right(a, right_value)
#   left_index = bisect_left(a, left_value)

#   return right_index-left_index


# a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# #값이 4인 데이터의 개수 출력
# print(count_by_range(a, 4, 4))

# #값이 [-1, 3] 범위에 있는 데이터 출력
# print(count_by_range(a, -1, 3))

# ****** ******





# 파라메트릭 서치(Parametric Search)
#   : "최적화 문제(어떤 함수의 값을 낮추거나 높이는 문제)를 결정문제(예 or 아니오)로 바꾸어 해결하는 기법"
#       ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제_ 즉, 이진탐색처럼 탐색범위를 좁혀가면서 해당 범위 내에서 조건을 만족하는 가장 알맞은 값 찾기
#   일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진탐새글 이용하여 해결할 수 있음
