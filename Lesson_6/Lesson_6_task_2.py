stock = {"banana": 6,
         "apple": 0,
         "orange": 32,
         "pear": 15}
prices = {"banana": 4,
          "apple": 2,
          "orange": 1.5,
          "pear": 3}
print("Total cost:", sum(stock[key] * prices[key] for key in stock.keys() & prices.keys()))
