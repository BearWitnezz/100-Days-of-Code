# TODO 1: Start an empty bids dictionary. Start reset as True, the winner as an empty string, and the highest
#   amount at 0.

# TODO 2: Print "Welcome to the Contractor Bid Board!".

# TODO 3: Loop while reset is True. Ask for a name and a whole-number bid. Lowercase the name, then save the bid
#   under that name.

# TODO 4: Ask "Any other bids? (y/n)" and lowercase the answer.

# TODO 5: "y" clears the screen by printing 20 blank lines, then the loop asks for the next bid.

# TODO 6: Any other answer stops the loop. Walk the dictionary and keep the name with the higher bid.

# TODO 7: Print "The winner is {name} with a bid of ${amount}!".

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
