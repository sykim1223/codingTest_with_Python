#파이썬은 퀵 정렬과 비슷한 원리의 sorted 기본 함수 제공
array = [8, 3, 6, 1, 0, 2, 9, 4, 5]

result = sorted(array)
print(result)

# 리스트 객체의 내장 함수로 사용가능->별도의 정렬된 리스트 반환x, 내부원소 정렬
array2 = [8, 3, 6, 1, 0, 2, 9, 4, 5]

array2.sort()
print(array2)

#key 매개변수를 이용하여, 정렬 기준을 설정. key는 하나의 함수.
array3 = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
  return data[1]

result = sorted(array3, key=setting)
print(result)


"""해당 정렬 라이브러리는 최악의 경우에도 O(NlogN)을 보장.
따라서 문제에서 별도로 요구하지 않는다면 sorted 함수를 이용하고,
데이터의 범위가 한정되어있고 더 빠른 속도를 요한다면 계수정렬 이용"""