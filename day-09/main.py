# TODO 1: Save each bidder's name and bid in a dictionary.
# TODO 2: Ask if anyone else is bidding, and clear the screen between bidders.
# TODO 3: After the last bid, find the highest one and print the winner and the amount.

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
