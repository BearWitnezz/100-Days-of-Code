Day 6 proof project — Drain Snake Simulator. A clog sits a random 1-10 feet down the drain. Each round you push (snake moves 1 foot) or twist (clears the clog only if you're at it). A while loop with a clog_cleared flag keeps going until the drain is clear. Uses def functions, while loops, flags, random.randint, and nested if/elif/else.

## Rebuild (Oct 19, 2026)
`drain_snake_simulator_rebuild.py` is John’s next-day from-memory rebuild. It moves the clog check into twist() and uses one flat if/elif/else chain in the main loop.
