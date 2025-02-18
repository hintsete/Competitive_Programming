# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B


n, k, q = map(int, input().split())
temp_interval = []
min_temp = float("inf")
max_temp = float("-inf")

for _ in range(n):
    start, end = map(int, input().split())
    temp_interval.append((start, end))
    min_temp = min(min_temp, start)
    max_temp = max(max_temp, end)
queries = []
for _ in range(q):
    start, end = map(int, input().split())
    min_temp = min(min_temp, start)
    max_temp = max(max_temp, end)
    queries.append((start, end))
temp_range = max_temp - min_temp + 1
coffee = [0] * (temp_range + 1)


for start, end in temp_interval:
    coffee[start - min_temp] += 1
    if end - min_temp + 1 < len(coffee):
        coffee[end - min_temp + 1] -= 1
for i in range(1, temp_range):
    coffee[i] += coffee[i - 1]
valid_days = [0] * temp_range
if coffee[0] >= k:
    valid_days[0] = 1
for i in range(1, temp_range):
    valid_days[i] = valid_days[i - 1] + (1 if coffee[i] >= k else 0)
for start, end in queries:
    start_idx = start - min_temp
    end_idx = end - min_temp
    if start_idx > 0:
        print(valid_days[end_idx] - valid_days[start_idx - 1])
    else:
        print(valid_days[end_idx])
