#DFS & BFS
# 1. 스택 자료구조: 후입선출(LIFO) ===================================================#
# ****** 스택 구현 예제_O(1) ******
# stack = []

# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()

# print(stack[::-1]) #최상단 원소부터 출력(후입선출) 
#  리스트 역순 출력 시, [::-1] 라고 입력. 
#      [3:0:-1] 일 경우, 3번 인덱스부터 1번 인덱스까지 역순출력.
#      [3::-1] 일 경우, 3번 인덱스부터 0번 인덱스까지 역순출력.
# print(stack) #최하단 원소부터 출력(선입선출)
# ****** ******



# 2. 큐 자료구조: 선입선출 (FIFO) ===================================================#
# ****** 큐 구현 예제_O(1) ******
# from collections import deque #효율을 위해 반드시 해당 라이브러리 사용!

# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(queue) #선입선출
# queue.reverse() #역순으로 바꾸기
# print(queue) # 나중에 들어온 원소부터 출력
# ****** ******



# 재귀함수 ===================================================#
# DFS 함수 구현 시 유용함
# ****** 재귀함수 예시 ******
# def recursive_function():
#   print('재귀함수를 호출합니다.')
#   recursive_function()

# recursive_function()
# ****** ******
#파이썬에서는 재귀함수 호출 시, 최대 재귀 깊이가 고정되어 있어 오류메시지 출려과 동시에 중단됨

# ****** 종료조건을 추가한 재귀함수 예시 ******
# def recursive_function(i):
#   if i == 10:
#     print('10번째 재귀함수가 호출되어 종료됩니다.')
#     return
#   print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
#   recursive_function(i+1)
#   print(i, '번째 재귀함수를 종료합니다.')

# recursive_function(1)
# ****** ******

# ****** 재귀함수를 이용한 팩토리얼 구현 예제 ******
# 반복적으로 구현한 팩토리얼
# def factorial_iterative(n):
#   result = 1
#   # 1-n까지 수를 차례대로 곱하기
#   for i in range(1,n+1): #1-n까지 범위
#     result = result*i
#   return result

# # 재귀함수로 구현한 팩토리얼 
# def fac_recursive(n):
#   if n<= 1:
#     return 1
#   return n*fac_recursive(n-1)

# print('반복적으로 구현: ', factorial_iterative(5))
# print('재귀적으로 구현: ', fac_recursive(5))
# ****** ******

# 최대공약수 계산(유클리드 호제법) 예제 #
# 두 자연수 A,B에대해 (A>B) A를 B로 나눈 나머지를 R이라고 하자.
# 이때, A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
# ****** 재귀함수로 구현한 소스코드 ******
# def gcd(a, b):
#   if a%b == 0:
#     return b
#   else:
#     return gcd(b, a%b)

# a, b =192, 162
# print(a, '\b와', b, '\b의 최대공약수는', gcd(a, b), '입니다.')
# ****** ******
# 재귀 함수가 반복문보다 유리한 경우도, 불리한 경우도 있음.
# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택프레임에 쌓임.
#     -> 스택을 사용해야 할 때, 구현상 "스택라이브러리 대신 재귀 함수를 이용"하는 경우가 많음