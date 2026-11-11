# TODO 1: Import the logo from art and print it.

# TODO 2: Start the auction as still open, and start an empty dictionary for the bids.

# TODO 3: Loop while the auction is open. Ask "What is your name?" and "What is your bid?". Save the bid as an int.

# TODO 4: Store that bid in the dictionary under the bidder's name.
#   Nudge: save it for every bidder, not only inside one branch of the next question.

# TODO 5: Ask "Are there any other bidders? Type 'yes' or 'no'.". "no" closes the auction. Any other answer prints
#   20 blank lines so the next bidder cannot see the last bid.

# TODO 6: After the loop, start the winner as an empty string and the highest bid at 0.

# TODO 7: Loop through the dictionary. When a bid is higher than the highest so far, save that amount and that
#   bidder's name.
#   Nudge: compare each bid with the highest one so far. Don't add the bids together.

# TODO 8: Print "The winner is {name} with a bid of ${amount}!".

from art import logo
print(logo)
game_not_over = True
price = {}

while game_not_over:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    price[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == 'no':
        game_not_over = False
    else:
        print("\n" * 20)
winner = ""
highest_bid = 0
for bidder in price:
    bid_amount = price[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}!")
