#n, k값 입력받기
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() #배열 A는 오름차순 정렬
b.sort(reverse=True) #배열 B는 내림차순 정렬

#첫 번째 인덱스부터 확인하여 두 배열의 원소를 최대 k번 비교
for i in range(k):
  #A의 원소가 B보다 작은경우 교체
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  #A의 원소가 크거나 같은 경우, 반복문 탈출
  else:
    break

#A 배열의 모든 값을 합하여 출력
print(sum(a))