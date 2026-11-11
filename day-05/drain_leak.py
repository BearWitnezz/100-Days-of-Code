# TODO 1: Make a list of the ticket numbers from 1 through 30.

# TODO 2: Loop through that list one ticket at a time.

# TODO 3: When a ticket is divisible by both 3 and 5, print "Drain & Leak".
#   Nudge: check both before you check 3 or 5 alone, or 15 never gets this message.

# TODO 4: Otherwise, a multiple of 3 prints "Drain".

# TODO 5: Otherwise, a multiple of 5 prints "Leak".

# TODO 6: Every other ticket prints the number itself.

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
