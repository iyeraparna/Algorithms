if __name__ == "__main__":
    n = 3
    power = 6
    ans = 1
    base = n
    while power>0:
        if n & 1 == 1:
            ans = ans * base
        n = n >> 1
        base = base * base
    print("answer")
    print(ans)