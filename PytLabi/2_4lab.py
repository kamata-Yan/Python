def count_divisors(N):
    count = 0
    for i in range(1, N + 1):
        if N % i == 0:
            count += 1
    return count

N = 12
print(f"Количество делителей у числа {N}: {count_divisors(N)}")
