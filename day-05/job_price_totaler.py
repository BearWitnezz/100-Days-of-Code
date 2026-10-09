job_prices = [150, 1200, 250, 150, 75]

days_total = 0
most_expensive = 0
for price in job_prices:
    days_total += price
    if price > most_expensive:
        most_expensive = price
print(days_total)
print(most_expensive)
