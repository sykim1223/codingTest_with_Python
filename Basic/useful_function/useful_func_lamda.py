#람다 표현식=============================================#
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있음
#일반적인 add 메서드
def add(a,b):
  return a+b
print(add(3,7))

#람다 표현식 이용시_함수 이름도 필요없어서 '이름없는 함수식'이라고도 함
# print((lambda a, b: a+b)(3,7))

#사용 예시1: 튜플형식으로 저장된 리스트를 특정 요소에 따라 정렬할 때
arr = [("홍길동", 50), ("이순신", 32), ("아무개", 74)]

def my_key(x):
  return x[1]

print(sorted(arr, key=my_key))
print(sorted(arr, key=lambda x: x[1]))

#사용 예시2: 여러개의 리스트에 적용 _map 함수는 각각의 원소에 어떤 함수 적용할 때 이용
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

result = map(lambda a,b:a+b, list1, list2)
# #    위 map 함수의 형태분석: map 함수의 원형이 map(A,B)일 때,
# #    A='lambda a,b:a+b'  이며, B = 'list1, list2' 임
# #    즉, B의 각각에 요소에 대해, A인 람다함수를 적용하는 것임

print(list(result))


