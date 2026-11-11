# Contractor Bid Board - Updated Version (weekly rebuild, Nov 4, 2026)
# Rebuilt from scratch with functions: finds the LOWEST bid (who wins the job).
#
# TODO 1: Make an empty bids dictionary before the loop, so later bids are not wiped out. (done)

# TODO 2: Write add_bid(bids, name, amount) with a docstring. It saves one bid as bids[name] = amount. (done)

# TODO 3: Use a while loop with a keep_going flag. Each round, ask for a name and a bid as a float (the prompt
#   shows a $), then call add_bid. Ask "Is there another bid? Type 'y' or 'n':". The flag flips to False only
#   when the answer is n. (done)

# TODO 4: Write find_lowest_bid(bids) with a docstring. Start the lowest bid at float("inf") so the first real
#   bid always counts. Loop through the dictionary and replace the lowest when a bid is smaller. Round that bid
#   to 2 decimal places. Don't add the bids up with +=. Return the winning bid, then the winner's name. (done)

# TODO 5: After the loop ends, call find_lowest_bid once. Unpack the bid and the name it returns, and print
#   "The winning bid is ${bid} from {name}!". (done)

# TODO 6: Run it after every step. When it works, clean up any repeated code. (done)

bids = {}
def add_bid(bids, name, amount):
    """Saves one bid into the dictionary."""
    bids[name] = amount
def find_lowest_bid(bids):
    """Return the winner's name and bid."""
    lowest_bidder = ""
    lowest_bid = float("inf")
    for lowest in bids:
        if lowest_bid > bids[lowest]:
            lowest_bid = round(bids[lowest], 2)
            lowest_bidder = lowest
    return lowest_bid, lowest_bidder


keep_going = True
while keep_going:
    name = input("Please enter your name: ")
    amount = float(input("Please enter your bid: $"))
    add_bid(bids, name, amount)
    another_bid = input("Is there another bid? Type 'y' or 'n': ")
    if another_bid == 'n':
        keep_going = False
lowest_bid, lowest_bidder = find_lowest_bid(bids)
print(f"The winning bid is ${lowest_bid} from {lowest_bidder}!")
