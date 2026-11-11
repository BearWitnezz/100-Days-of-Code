# TODO 1: Start from the job prices 150, 1200, 250, 150, and 75.

# TODO 2: Start a day's total at 0 and a most-expensive tracker at 0.

# TODO 3: Loop through every price. Add it to the day's total.

# TODO 4: In that same loop, replace the most expensive price whenever the current price is higher.

# TODO 5: After the loop, print the day's total, then print the most expensive job.

job_prices = [150, 1200, 250, 150, 75]

days_total = 0
most_expensive = 0
for price in job_prices:
    days_total += price
    if price > most_expensive:
        most_expensive = price
print(days_total)
print(most_expensive)
