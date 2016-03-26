stocks = {
    'GOOG': 523.12,
    'FB': 123.32,
    'AAPL': 5232.12,
    'EWD': 52.12
}


print min(zip(stocks.values(),stocks.keys()))
print max(zip(stocks.values(),stocks.keys()))
print sorted(zip(stocks.values(),stocks.keys()))
print sorted(zip(stocks.keys(),stocks.values()))
