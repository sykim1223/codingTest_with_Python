#[문제2] 시각_완전탐색 문제
# 정수 N이 입력되면 00시00분00초 부터 N시59분59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.
# 입력조건)첫번째 줄에 정수 N이 입력(0 <= N <= 23)
# 출력조건) 모든 경우의 수 출력

# ***소스코드1 ***
# N = int(input("시각을 입력하세요: "))
# cnt = 0


# for h in range(0, N+1):
#   if h == 3: 
#     cnt = cnt + 3600
#     continue
#   else:
#     for m in range(0, 60):
#         for s in range(0, 60):
#           if m//10 == 3 or m%10 == 3 or s//10 == 3 or s%10 == 3:
#             cnt = cnt + 1

# print(f"총 {cnt}회 입니다")
#******

#***소스코드2***
h = int(input("시각을 입력하세요: "))

cnt =0

for i in range(h+1):
  for j in range(60):
    for k in range(60):
      #매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i)+str(j)+str(k):
        cnt = cnt+1

print(f"총 {cnt}회 입니다.")
#*** 현재 시간을 string 형식으로 변환하여 수행!