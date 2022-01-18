#DFS & BFS
# 1. 스택 자료구조: 후입선출(LIFO) ===================================================#
# ****** 스택 구현 예제_O(1) ******
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) #최상단 원소부터 출력(후입선출) 
#  리스트 역순 출력 시, [::-1] 라고 입력. 
    #  [3:0:-1] 일 경우, 3번 인덱스부터 1번 인덱스까지 역순출력.
    #  [3::-1] 일 경우, 3번 인덱스부터 0번 인덱스까지 역순출력.
print(stack) #최하단 원소부터 출력(선입선출)
# ****** ******

