# TODO 1: Add up every price in the job list.
# TODO 2: Keep the highest price seen while looping.
# TODO 3: Print the day's total and the most expensive job.

job_prices = [150, 1200, 250, 150, 75]

days_total = 0
most_expensive = 0
for price in job_prices:
    days_total += price
    if price > most_expensive:
        most_expensive = price
print(days_total)
print(most_expensive)
