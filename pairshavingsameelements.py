def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    ans = 0
    ct = 1
    ctdis = 1

    for i in range(1, n):
        if a[i] == a[i - 1]:
            ct += 1
        elif a[i] == (a[i - 1] + 1):
            ct += 1
            ctdis += 1
        else:
            if ct >= 2 and ctdis >= 2:
                ans += (ct * (ct - 1)) // 2
            ct = 1
            ctdis = 1

    if ct >= 2 and ctdis >= 2:
        ans += (ct * (ct - 1)) // 2

    print(ans)

if __name__ == "__main__":
    main()
