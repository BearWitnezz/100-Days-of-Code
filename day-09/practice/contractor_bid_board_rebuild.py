bids = {}
reset = True
winner = ""
highest_amount = 0
print("Welcome to the Contractor Bid Board!")
while reset:
    name = input("What is your name?\n").lower()
    bid_amount = int(input("How much would you like to bid?\n$"))
    bids[name] = bid_amount
    another = input("Any other bids? (y/n)\n").lower()
    if another == "y":
        print("\n" * 20)
    else:
        reset = False
        for bidder in bids:
            if bids[bidder] > highest_amount:
                highest_amount = bids[bidder]
                winner = bidder
print(f"The winner is {winner} with a bid of ${highest_amount}!")
