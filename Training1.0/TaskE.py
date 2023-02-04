# K - flat, P - block, N - floor
from math import ceil

K1, M, K2, P2, N2 = [int(i) for i in input().split()]

if K2 % ((P2 - 1) * M + N2) == 0:
    flats_per_floor_max = flats_per_floor_min = K2 // ((P2 - 1) * M + N2)
elif K2 % ((P2 - 1) * M + N2) != 0 and K2 / ((P2 - 1) * M + N2) < 1:
    flats_per_floor_max = flats_per_floor_min = K2 / ((P2 - 1) * M + N2)
else:
    flats_per_floor_max = ceil(K2 / ((P2 - 1) * M + N2))
    flats_per_floor_min = int((K2 - 1) / ((P2 - 1) * M + N2 - 1))

if flats_per_floor_max != flats_per_floor_min:
    P1_var = set()
    for i in range(flats_per_floor_min, flats_per_floor_max + 1):
        total_floor1 = (K1 // i) if (K1 % i == 0) else (K1 // i + 1)
        P1_var.add((total_floor1 // M) if (total_floor1 % M == 0) else (total_floor1 // M + 1))
    if len(P1_var) == 1:
        P1 = P1_var.pop()
        N1 = total_floor1 - (P1 - 1) * M
    else:
        P1, N1 = 0, 0
elif flats_per_floor_max < 1 or N2 > M:
    P1, N1 = -1, -1
elif N2 == P2 == 1 and M == 1:
    P1, N1 = 0, 1
elif N2 == P2 == 1 and M != 1:
    P1, N1 = 0, 0
# else:
#     total_floor1 = (K1 // flats_per_floor) if (K1 % flats_per_floor == 0) else (K1 // flats_per_floor + 1)
#     P1 = (total_floor1 // M) if (total_floor1 % M == 0) else (total_floor1 // M + 1)
#     N1 = total_floor1 - (P1 - 1) * M
print(P1, N1)


