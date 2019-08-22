n=int(input())
candles=list(map(int, input().split()))
candles.sort()
print(candles.count(candles[n-1]))