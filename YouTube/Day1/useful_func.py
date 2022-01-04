#집합 자료형=========================================#  
#  - 중복을 허용하지 않음

#초기화방법 1_강제형변환
# data = set([1,1,2,2,3,3,4,4,5])
# print(data)

#초기화방법 2_{}괄호
# data2 = {1,1,2,3,3,4,5}
# print(data2)

#합집합/교집합/차집합 연산 가능 | & - 연산자로 가능


#빠르게 입력받기=====================================#
# -사용자로부터 입력을 최대한 빠르게 받을 때,  
#  sys 라이브러리의 sys.stdin.readline() 메서드 이용
#     단, 입력후 엔터가 줄바꿈 기호로 입력되므로 rstrip() 메서드 함께 이용하기

# import sys

# data = sys.stdin.readline().rstrip()
# print(data)


#f-String============================================#
# 파이썬 3.6부터 가용가능하며, 문자열 앞에 접두가 f를 붙여 사용
# answer, fau = 3,4
# print(f"정답은 {answer}입니다")
# print("두개의 값 {:1}과 {:2}을 넣을거얌".format(answer, fau))


#pass ===============================================#
# 실제 내용을 구체적으로 정하지 않았을 때, pass 입력하면 걍 지나감
# if a < 10:
#   pass
# elif:
#   print("hello")

#조건문의 간소화
#조건부 표현식(conditional Expression)은 is~els문을 한 줄에 작성하게 해줌
# 

#global 키워드==========================================#
#함수 밖의 전역 변수 사용하고 싶을 때
# a=10

# def func():
#   global a
#   a=a+1
#   print(a)

# func()


#람다 표현식=============================================#
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있음
#일반적인 add 메서드
# def add(a,b):
#   return a+b
# print(add(3,7))

#람다 표현식 이용시_함수 이름도 필요없어서 '이름없는 함수식'이라고도 함
# print((lambda a, b: a+b)(3,7))

#사용 예시1: 튜플형식으로 저장된 리스트를 특정 요소에 따라 정렬할 때
# arr = [("홍길동", 50), ("이순신", 32), ("아무개", 74)]

# def my_key(x):
#   return x[1]

# print(sorted(arr, key=my_key))
# print(sorted(arr, key=lambda x: x[1]))

#사용 예시2: 여러개의 리스트에 적용 _map 함수는 각각의 원소에 어떤 함수 적용할 때 이용
# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]

# result = map(lambda a,b:a+b, list1, list2)
# #    위 map 함수의 형태분석: map 함수의 원형이 map(A,B)일 때,
# #    A='lambda a,b:a+b'  이며, B = 'list1, list2' 임
# #    즉, B의 각각에 요소에 대해, A인 람다함수를 적용하는 것임

# print(list(result))


#순열 조합 라이브러리=======================================#
#순열
# from itertools import permutations

# data = ['A', 'B', 'C']

# result = list(permutations(data, 3))
# print(result)

#조합
# from itertools import combinations

# data = ['A', 'B', 'C']

# result = list(combinations(data, 3))
# print(result)

#중복순열 
# from itertools import product

# data = ['A', 'B', 'C']

# result = list(product(data, repeat=2)) #2개를 뽑는 모든 순열(중복허용)
# print(result)

# #중복조합
# from itertools import combinations_with_replacement

# data = ['A', 'B', 'C']

# result = list(combinations_with_replacement(data, 2)) #2개를 뽑는 모든 조합(중복허용)
# print(result)