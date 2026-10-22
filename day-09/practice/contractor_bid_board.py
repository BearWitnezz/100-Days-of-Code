print("Welcome to the Contractor Bid Board!")
bid = {}
bidding_done = False
while not bidding_done:
    name = input("What is your name?\n")
    bid_amount = int(input("How much would you like to bid?\n$"))
    bid[name] = bid_amount
    another_bid = input("Any other contractors? yes or no.\n")
    if another_bid == "no":
        bidding_done = True
        highest_amount = 0
        winners_name = ""
        for contractor in bid:
            if bid[contractor] > highest_amount:
                highest_amount = bid[contractor]
                winners_name = contractor
        print(f"The job goes to {winners_name} with a bid of ${highest_amount}.")
