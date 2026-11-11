# TODO 1: Import random. The fittings are elbow, tailpiece, wastearm, ptrap, and 45. The saved job prices are
#   130, 40, 83, 67, and 92.

# TODO 2: Start a flag at True so the estimator can run more than one job.

# TODO 3: Define pipe_cost(length_feet, price_per_foot, fittings) with a docstring. It prints (length times the
#   price per foot) plus (4 times the fittings count).

# TODO 4: Loop while another estimate is wanted. Each pass, reset the job total to 0 and pick one fitting at
#   random.

# TODO 5: Print "Welcome!". Ask for the customer's name, and ask how many feet of pipe as an int. Print both
#   answers back.

# TODO 6: Add every saved job price into the job total, then print that total.

# TODO 7: A total over 500 prints "Big job". Otherwise print "Quick job".

# TODO 8: A total divisible by 2 prints "Even". Otherwise print "Odd".

# TODO 9: Print the customer's name, the random fitting, and "Total: $" with the total rounded to 2 decimal places.

# TODO 10: Call pipe_cost with the feet of pipe, a price per foot of 4, and a fittings count of 6.
#   Nudge: pass them as keyword arguments.

# TODO 11: Ask "Do you want to continue? (y/n)" and lowercase the answer. y runs another estimate. n stops the loop.

import random

list_of_fittings = ['elbow', 'tailpiece', 'wastearm', 'ptrap', '45']
job_prices = [130, 40, 83, 67, 92]
game_not_over = True


def pipe_cost(length_feet, price_per_foot, fittings):
    """Print the cost of the pipe and fittings for the job."""
    print((length_feet * price_per_foot) + (4 * fittings))


while game_not_over:
    job_total = 0
    random_part = random.choice(list_of_fittings)
    print("Welcome!")
    name = input("What is the customer's name?\n")
    feet_of_pipe = int(input("How many feet of pipe do you need for the job?\n"))
    print(name)
    print(feet_of_pipe)
    for job in job_prices:
        job_total += job
    print(job_total)
    if job_total > 500:
        print("Big job")
    else:
        print("Quick job")
    if job_total % 2 == 0:
        print("Even")
    else:
        print("Odd")
    print(f"{name} {random_part} Total: ${round(job_total, 2)}")
    pipe_cost(length_feet=feet_of_pipe, price_per_foot=4, fittings=6)
    continue_or_not = input("Do you want to continue? (y/n)\n").lower()
    if continue_or_not == "y":
        game_not_over = True
    elif continue_or_not == "n":
        game_not_over = False
