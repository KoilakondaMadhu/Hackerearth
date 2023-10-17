def minimum_length(n, a, b):
    l = n + 1
    r = -1

    for i in range(n):
        if a[i] != b[i]:
            l = min(l, i)
            r = max(r, i)

    if r == -1:
        return 0
    else:
        return r - l + 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        result = minimum_length(n, a, b)
        print(result)
