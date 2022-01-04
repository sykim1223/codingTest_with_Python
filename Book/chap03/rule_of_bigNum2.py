#큰수의 법칙 문제 재풀이

#getting inputs n, m, k
n, m, k = map(int, input().split())

#getting n data
data = list(map(int, input().split()))

data.sort()
max_num = data[n-1]
scd_num = data[n-2]

#calc the time that max number is multiplied
quot = m // (k+1)
rmd = m % (k+1)

result = 0

result = quot*(k*max_num + scd_num)
result += rmd * max_num

print(result)

'''
접근법
적용 알고리즘: 그리디 알고리즘
1. 동일한 인덱스의 수는 연속k번 더해지지만 않으면 몇번이고 더할 수 있음
2. 가장 큰 수(max)가 연속k번을 초과하여 더해지지 않도록 하는 장치는 두번째 큰수(scd)
3. 따라서 수가 더해지는 양상은 [max, max, max, scd] 수열의 반복임(k=3일 때)
4. 수열의 크기는 k+1이고 수열은 q번 반복됨( m = q*(k+1)+r 이므로) 
5. r의 범위는 0<= r <= 3 이므로 수열이 반복된 후 더해져야 할 값은 모두 max임
6. 따라서 결과 값은 다음과 같이 계산됨을 알 수 있음
    (수열 속한 값)을 q회 : q(max+max+max+scd)=q(k*max + scd) --- A
    (수열 아닌 값)을 r회 : r * max --- B
7. 따라서 (정답)= A+B
'''