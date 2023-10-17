def solve(n, s, e, a):
    assert n > 1
    assert n <= 100000
    s = s - 1
    e = e - 1
    count = 0
    temp = 0
    
    if s <= e:
        for i in range(s, e):
            count += a[i]
        
        for i in range(0, s):
            temp += a[i]
        
        for i in range(e, len(a)):
            temp += a[i]
        
        return min(temp, count)
    
    for i in range(e, s):
        count += a[i]
    
    for i in range(0, e):
        temp += a[i]
    
    for i in range(s, len(a)):  # Added missing parenthesis here
        temp += a[i]
    
    return min(temp, count)

if __name__ == "__main__":
    N = int(input())
    start = int(input())
    finish = int(input())
    Ticket_cost = list(map(int, input().split()))

    out_ = solve(N, start, finish, Ticket_cost)
    print(out_)
