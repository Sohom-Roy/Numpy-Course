prices = [100,200,300,400,500]
discount = 10 # %
final_prices = []
for price in prices:
    final_price = price - (price*(discount/100))
    final_prices.append(int(final_price))


print("INITIAL PRICES:",prices)
print("PRICE AFTER DISCOUNT:",final_prices)


#lopps are very slow in nature now appropriate for large data, so broadcasting comes into play