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
