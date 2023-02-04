# sqrt(ax + b) = c => ax + b = c ** 2
a, b, c = [int(input()) for _ in range(3)]
if (a == 0 and (b == c ** 2 and c > 0)) or a == b == c == 0:
    answer = 'MANY SOLUTIONS'
elif (a == 0 and b == 0 and c != 0) \
        or (a == 0 and b != c ** 2) or c < 0:
    answer = 'NO SOLUTION'
else:
    x = (c ** 2 - b) / a
    if int(x) == x:
        answer = int(x)
    else:
        answer = 'NO SOLUTION'
print(answer)

