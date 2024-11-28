A = []
A=list(map(int,input().split()))

def unique_elements(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]==A[j]:
                return False
    return True

print(unique_elements(A))