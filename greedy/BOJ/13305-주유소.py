N = int(input())
distances = list(map(int, input().split()))
cities = list(map(int, input().split()))
min_price = 10 ** 9
to_go = 0
result = 0
for i, price in enumerate(cities[:N-1]):
    if min_price > price:
        result += min_price * to_go
        to_go = distances[i]
        min_price = price
    else:    
        to_go += distances[i]
print(result + min_price * to_go)