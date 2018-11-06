"""
Hello,

this program goes over for loops and working with list comprehension.

for list comprehension look at new_prices or cuts_under_30

you can also see iteration of prices into total_price
"""

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 1]

total_price=0
for i in prices:
  total_price += i
print(total_price)
average_price=total_price/len(prices)
print("Average Price: $" + str(average_price))
new_prices=[i-5 for i in prices]
print(new_prices)
total_revenue=0
for i in range(len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
print("Total Revenue: $" + str(total_revenue))
average_daily_revenue = total_revenue/7
print("Average Daily Revenue: $" + str(average_daily_revenue))
cuts_under_30=[hairstyles[i] for i in range(len(new_prices)) if new_prices[i]<30]
print(cuts_under_30)