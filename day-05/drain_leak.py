# TODO 1: Loop through the ticket numbers from 1 to 30.
# TODO 2: Print "Drain & Leak" when a number is divisible by both 3 and 5.
# TODO 3: Print "Drain" for multiples of 3, "Leak" for multiples of 5, otherwise the number.

tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

for ticket in tickets:
    if ticket % 3 == 0 and  ticket % 5 == 0:
        print("Drain & Leak")
    elif ticket % 3 == 0:
        print("Drain")
    elif ticket % 5 == 0:
        print("Leak")
    else:
        print(ticket)
