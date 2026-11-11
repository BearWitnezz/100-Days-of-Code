# TODO 1: Print "Welcome to the Contractor Bid Board!".

# TODO 2: Start an empty dictionary for the bids, and start bidding_done as False.

# TODO 3: Loop while bidding is not done. Ask for the contractor's name and a whole-number bid.

# TODO 4: Save that bid in the dictionary under the contractor's name.

# TODO 5: Ask "Any other contractors? yes or no.". "no" marks bidding as done.

# TODO 6: Once bidding is done, start the highest amount at 0 and the winner's name as an empty string.

# TODO 7: Loop through the dictionary. Keep the name whose bid is higher than the highest so far.
#   Nudge: compare the bids. Don't add them together.

# TODO 8: Print "The job goes to {name} with a bid of ${amount}."

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
