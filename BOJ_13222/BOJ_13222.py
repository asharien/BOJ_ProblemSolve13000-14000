import sys
N, W, H = map(int, sys.stdin.readline().split())
SIDE = (W**2+H**2)**0.5
L = max(W, H, SIDE)
for _ in range(N):
    X = int(sys.stdin.readline())
    print("YES" if X<=L else "NO")


