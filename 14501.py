import sys

input = sys.stdin.readline

N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)  # 인덱스 0부터 N까지 존재
ScoreArray = [0] * (N + 1)

for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

if T[N] == 1:
    ScoreArray[N] = P[N]
else:
    ScoreArray[N] = 0

for n in range(N - 1, 0, -1):
    if n + T[n] - 1 > N:
        ScoreArray[n] = ScoreArray[n + 1]
    elif n + T[n] - 1 == N:
        ScoreArray[n] = max(ScoreArray[n + 1], P[n])
    else:
        ScoreArray[n] = max(ScoreArray[n + 1], ScoreArray[n + T[n]] + P[n])

print(max(ScoreArray))
