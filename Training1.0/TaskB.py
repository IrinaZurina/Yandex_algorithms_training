side1, side2, side3 = list(map(int, input().split()))
if side1 < side2 + side3 and\
    side2 < side1 + side3 and\
    side3 < side1 + side2:
    print('YES')
else:
    print('NO')
