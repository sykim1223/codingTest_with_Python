

# 재귀함수 ===================================================#
# DFS 함수 구현 시 유용함
# ****** 재귀함수 예시 ******
def recursive_function():
  print('재귀함수를 호출합니다.')
  recursive_function()

recursive_function()
# ****** ******
#파이썬에서는 재귀함수 호출 시, 최대 재귀 깊이가 고정되어 있어 오류메시지 출려과 동시에 중단됨





# ****** 종료조건을 추가한 재귀함수 예시 ******
def recursive_function(i):
  if i == 10:
    print('10번째 재귀함수가 호출되어 종료됩니다.')
    return
  print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
  recursive_function(i+1)
  print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)
# ****** ******





# ****** 재귀함수를 이용한 팩토리얼 구현 예제 ******
# 반복적으로 구현한 팩토리얼
def factorial_iterative(n):
  result = 1
  # 1-n까지 수를 차례대로 곱하기
  for i in range(1,n+1): #1-n까지 범위
    result = result*i
  return result

# 재귀함수로 구현한 팩토리얼 
def fac_recursive(n):
  if n<= 1:
    return 1
  return n*fac_recursive(n-1)

print('반복적으로 구현: ', factorial_iterative(5))
print('재귀적으로 구현: ', fac_recursive(5))
# ****** ******
