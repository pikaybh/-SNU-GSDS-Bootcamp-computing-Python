def fibonacci(n, cnt0, cnt1):
    if n == 0:
        cnt0 += 1
        return 0, cnt0, cnt1

    elif n == 1:
        cnt1 += 1
        return 1, cnt0, cnt1

    else:
        a = fibonacci(n - 1, cnt0, cnt1)
        b = fibonacci(n - 2, cnt0, cnt1)
        result = []

        for i in range(3):
            result.append(a[i] + b[i])

        return tuple(result)


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        result = fibonacci(N, 0, 0)
        print(result[1], result[2])