def binary_digits(n):
    count=1
    if n<=1:
        return 1
    else:
        return 1+binary_digits(n//2)


n = int(input())


print(binary_digits(n))