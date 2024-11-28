
def sequential_search(A, key):
    for i in range(len(A)):
        if A[i]==key:
            return i
    return -1


A = []
key = 0
A=list(map(int,input().split()))
key=int(input())

# 출력합니다!
print("%d찾기:" %(key), sequential_search(A, key))