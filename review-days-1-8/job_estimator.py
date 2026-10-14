import random

list_of_fittings = ['elbow', 'tailpiece', 'wastearm', 'ptrap', '45']
job_prices = [130, 40, 83, 67, 92]
game_not_over = True


def pipe_cost(length_feet, price_per_foot, fittings):
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
