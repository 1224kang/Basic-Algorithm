def selection_sort(A):
    n=len(A)
    for i in range(n-1):
        least=i
        for j in range(i+1,n):
            if(A[j]<A[least]):
                least=j
        A[i],A[least]=A[least],A[i]
        printStep(A,i+1);
    return None

def printStep(arr, val):
    print("  Step %2d = " %val, end='')
    print(arr)


A = []
A=list(map(int,input().split()))

# 출력합니다!
print("Original  :", A)
selection_sort(A)
print("Selection :", A)