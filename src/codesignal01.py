from typing import List

def buyAndSellStock(prices: List[int]) -> int:
    buy = float('inf')
    sell = 0
    maxProfit = 0

    for price in prices:
      if price < buy:
        buy = price
        sell = price
      if price > sell:
        sell = price
        maxProfit = max(sell - buy, maxProfit)

    return maxProfit

print(buyAndSellStock([6, 3, 1, 2, 5, 4]))
print(buyAndSellStock([3, 100, 1, 97]))
print(buyAndSellStock([8, 5, 3, 1]))