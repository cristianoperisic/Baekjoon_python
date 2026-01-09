# 2885 초콜릿 식사
import sys

input = sys.stdin.readline

K = int(input())
oldK = K
n = 0
l = 0


if K == 1:
    print(1, 0)

else:
    while K > 0:
        K = K // 2
        n = n + 1  # 2**n이 가장 작은 초콜릿 크기
    minValue = 2**n

    while oldK > 0:
        n = n - 1
        l = l + 1
        if oldK - 2**n >= 0:
            oldK = oldK - 2**n

    print(minValue, l)
