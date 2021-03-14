import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [-1 for _ in range(N)]

stack.append(array[-1])

for i in range(N-2, -1, -1):
    while len(stack) != 0:
        if array[i] >= stack[-1]:
            stack.pop()
        else:
            answer[i] = stack[-1]
            break
    stack.append(array[i])

print(*answer)