####리스트 컴프리헨션_ : 문자가 없음
arr = [i for i in range(20) if i%2 !=0 ]
print(arr)




###2차원 리스트 컴프리헨션 NxM
#----좋은 예시----
m, n = 2,5
arr = [[0]*m for _ in range(n)]
print(arr, arr[0] is arr[2], sep='\n')
# -> is 함수로 비교시, 배열 요소가 서로 다른 객체임

#----나쁜예시----
arr = [[0]*m]*n
print(arr, arr[0] is arr[2], sep='\n')
# -> is 함수로 비교시, 배열 요소가 동일한 객체임(참조값을 복사하는 하기 때문)
# -> 이 경우, !!임의의 배열 요소 변경 시 다른 배열의 값도 같이 변경됨!!


