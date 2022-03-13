from tkinter import N


def findSetBits(n):
    count = 0
    while n > 0:
        count+=1
       # n = n & (n-1)
        n -= n&(-n)

    return count
if __name__ == "__main__":
    n = 234567
    print(findSetBits(n))


