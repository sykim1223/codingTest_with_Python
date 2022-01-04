#N값 입력받기
print('Input a number n: ')
n = int(input())

#N개의 정수를 입력받아 리스트에 저장
array = []
print('Input the number array: ')
for i in range(n):
  array.append(int(input()))

#파이썬 기본 정렬 라이브러리 이용
array = sorted(array, reverse=True)

#정렬 결과 출력
for i in array:
  print(i, end=' ')