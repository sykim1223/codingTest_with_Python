#순열 조합 라이브러리=======================================#
#순열
from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)

#조합
from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 3))
print(result)

#중복순열 
from itertools import product

data = ['A', 'B', 'C']

result = list(product(data, repeat=2)) #2개를 뽑는 모든 순열(중복허용)
print(result)

# #중복조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2)) #2개를 뽑는 모든 조합(중복허용)
print(result)


#예제문제====================================#
# 문자열이 입력되었을 때 문자를 하나씩 확인
#   - 숫자인 경우, 따로 합계를 계산
#   - 알파벳인 경우, 별도의 리스트에 저장
# 결과적으로 리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력하면 정답

data = input()
list_alph = []
value = 0

for i in data:
  if i.isalpha():
    list_alph.append(i)
  else:
    value = value+int(i)

if value != 0:
  list_alph.append(str(value))

print(''.join(list_alph)) 
#join함수는 리스트의 요소들을 하나의 문자열로 변환해주며, ''안의 문자를 리스트요소 사이의 구분자로 이용함