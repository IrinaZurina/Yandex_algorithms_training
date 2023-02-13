# def count_x_from_y(x, y):
#     return y % x, y // x


N, K, M = list(map(int, input().split()))
count_details = 0
# while N >= K:
#     N, num_of_K = count_x_from_y(K, N)
#     rest_of_K, num_of_M = count_x_from_y(M, K)
#     count_details += num_of_M * num_of_K
#     N += rest_of_K * num_of_K
# print(count_details)

while N >= K:
    num_of_K, N = N // K, N % K
    count_details += K // M * num_of_K
    N += (K % M) * num_of_K
print(count_details)
