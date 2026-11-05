# Day 9: Blind Auction

Run `main.py` to collect secret bids from each bidder. When bidding ends, it announces who won and how much they bid. The ASCII logo is in `art.py`.

## Bugs I fixed along the way

- The loop never ran, because I started with `game_over = True` and then looped on `while not game_over`. I switched to `game_not_over = True`.
- I moved `price[name] = bid` outside the if/else so every bid gets saved.
- To find the highest bid, I now compare each bid with the highest one so far instead of adding them together with `+=`. The winner is saved by their dictionary key, `bidder`.
- I unindented the winner check so it runs once, after the loop ends.

## Updated Version (Nov 4, 2026)

[`practice/bid_board_updated.py`](practice/bid_board_updated.py) is a from-scratch weekly rebuild of the Contractor Bid Board. It uses functions (`add_bid`, `find_lowest_bid`), finds the lowest bid instead of the highest, and uses tuple unpacking.
