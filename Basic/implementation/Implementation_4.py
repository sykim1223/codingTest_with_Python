# [문제4]문자열 재정렬
# 알파벳 대문자와 숫자(0-9)로만 구성된 문자열이 입력으로 주어짐. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤, 그 뒤에 모든 숫자를 더한 값을 이어서 출력하라.

s = input("재정렬할 문자를 입력하세요: ")

result = []
sum = 0

for i in s:
  if i.isalpha():
    result.append(i)
  else:
    sum = sum + int(i)

result.sort()

if sum !=0:
  result.append(str(sum))


print(f"{''.join(result)}입니다.")