#다이나믹 프로그래밍
  # : 메모리를 적절히 사용하여 수행시간 효율성을 비약적으로 향상시키는 방법
  #   이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 함
  #   다이나믹 프로그래밍의 구현은 일반적으로 두가지 방법(탑다운 & 보텀업)으로 구성됨
  # 일반적인 프로그래밍 분야에서 동적이란?
  #   자료구조에서 동적 할당은 "프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법"을 의미
  #   반면 다이나믹 프로그래밍에서 다이나믹은 별다른 의미 없이 사용된 단어임

# 다이나믹 프로그래밍의 조건: 문제가 다음의 조건을 만족할 때 사용할 수 있음
  # - 최적 부분 구조(Optimal Substructure)
  #   : 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있음
  # - 중복되는 부분 문제
  #   : 동일한 작은 문제를 반복적으로 해결해야 함

#피보나치 수열: 점화식으로 인접한 항들 사이의 관계식을 표현할 수 있음
    # -> 트리형태로 구조화해보면 f(4)를 구함에 있어서 f(3)과 f(2)가 필요하며, f(3)에도 f(2)가 필요함

# ****** 피보나치 수열: 단순 재귀 소스코드 ******
# def fibo(x):
#   if x == 1 or x == 2:
#     return 1
#   return fibo(x-1) + fibo(x-2)

# print(fibo(4))
# ****** ******
#시간복잡도: 단순재귀함수로 구현할 경우, 지수시간 복잡도를 가지게 됨. f(2)가 여러번 호출되는 것을 확인할 수 있음(중복되는 부분 문제)

# 피보나치 수열의 효율적 해법: 다이나믹 프로그래밍
  # 다이나믹 프로그래밍의 사용 조건을 만족하는지 확인
  #   - 최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있다
  #   - 중복되는 부분 문제: 동일한 작은 문제를 반복적으로 해결한다
  # => 피보나치 수열은 다이나믹 프로그래밍의 사용 조건을 만족한다

#메모이제이션(Memoization)
  # 다이나믹 프로그래밍을 구현하는 방법 중 하나
  # "한 번 계산한 결과를 메모리 공간에 메모모하는 기법
  #   - 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옴
  #   - 값을 기록해 놓는다는 점에서 캐싱(caching)이라고도 함

# 탑다운 VS 보텀업
  # 탑다운(메모이제이션) 방식은 하향식이라고도 하며, 보텀법은 상향식이라고도 함
  # 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식임.(보텀업은 반복문을 사용함)
  #   - 결과 저장용 리스트는 DP테이블 이라고 부름
  # 엄밀히 말하면 메모이제이션은 "이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념"을 의미함
  #   - 따라서 메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아님
  #   - 한 번 계산된 결과를 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수 있음

# ****** 피보나치 수열: 탑다운 다이나믹 프로그래밍 소스코드 ******
#한번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d= [0]*100

#피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
# def fibo(x):
#   #종료 조건(1 혹은 2일 때 1을 반환)
#   if x == 1 or x == 2:
#     return 1
#   #이미 계산한 적 있는 문제라면 그대로 반환
#   if d[x] != 0:
#     return d[x]
#   #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
#   d[x] = fibo(x-1) + fibo(x-2)
#   return d[x]

# print(fibo(99))
# ****** ******

# ****** 피보나치 수열: 보텀업 다이나믹 프로그래밍 소스코드 ******
#앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d= [0]*100

#첫번째 피보나치 수와 두번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

#피보나치 함수를 반복문으로 구현
for i in range(3, n+1):
  d[i] = d[i-1] + d[i-2]

print(d[n])

# ****** ******

#다이나믹 프로그래밍 VS 분할 정복
  # 다이나믹 프로그래밍과 분할 정복은 모두 "최적 부분 구조"를 가질 때 사용할 수 있음
  #   - 큰 문제를 작은 문제로 나눌 수 있으며, 작은 문제의 답을 모아서 큰 문제를 해결할 수 있는 상황
  # 다이나믹 프로그래밍과 분할 정복의 차이점은 "부분 문제의 중복"임
  #   - 다이나믹 프로그래밍 문제에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복됨
  #   - 분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않음


#다이나믹 프로그래밍 문제에 접근하는 방법
  # 주어진 문제가 다이나믹 프로그래밍 유형임을 파악하는 것이 중요
  # 가장 먼저 "그리디, 구현, 완전 탐색" 등의 아이디어로 문제를 해결할 수 있는지 검토
  #   - 다른 알고리즘으로 풀이 방법이 떠오르지 않으면 다이나믹 프로그래밍을 고려
  # 일단 재귀함수로 비효율적인 완전 탐색 프로그램을 작성한 뒤에(탑다운) 작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있으면, 코드를 개선하는 방법을 사용할 수 있음
  # "일반적인 코딩 테스트 수준에서는 기본 유형의 다이나믹 프로그래밍 문제가 출제"되는 경우가 많음