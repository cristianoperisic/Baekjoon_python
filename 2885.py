# 2885 초콜릿 식사
import sys

input = sys.stdin.readline

K = int(input())
oldK = K
n = 0
l = 0


while K > 0 and K != 1:
    check = K % 2
    K = K // 2
    if check == 1:
        break

K = oldK  # K가 2의 거듭제곱이 아님

if check == 1:
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

else:
    print(K, 0)
