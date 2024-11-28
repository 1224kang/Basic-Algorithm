def compute_square_C(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += 1
    return sum

n = int(input())

print(compute_square_C(n))