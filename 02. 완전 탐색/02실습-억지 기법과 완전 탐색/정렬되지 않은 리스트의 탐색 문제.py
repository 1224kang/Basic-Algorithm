def sequential_search(A, key):
    for i in range(len(A)):
        if A[i]==key:
            return i
    return -1

A = []
A=list(map(int,input().split()))

key = None
key=int(input())

# 출력합니다!
print(sequential_search(A, key))