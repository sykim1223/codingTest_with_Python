#모든 원소의 값이 0보다 크거나 같은 정수라고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) +1)

for i in range(len(array)):
  count[array[i]] += 1 #각 데이터에 해당하는 인덱스의 값을 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보만큼 출력
  for j in range(count[i]): #해당 인덱스의 값 만큼 반복 출력
    print(i, end=' ') #띄어쓰기 구분으로 출력