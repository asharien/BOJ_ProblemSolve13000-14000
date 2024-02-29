import sys
def DIVISOR(N):
    DIV = set()
    for i in range(1, N+1):
        if N%i == 0: DIV.add(i)
    return list(DIV)
def main():
    print(sum(DIVISOR(int(sys.stdin.readline()))))
if __name__ == "__main__":
    main()
