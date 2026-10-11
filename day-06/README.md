# Day 6: Reeborg's World, "Lost in a Maze"

The solution in `reeborg_maze.py` runs in [Reeborg's World](https://reeborg.ca/), not plain Python.

## Fixing the infinite loop

My first version followed the right wall but could spin forever in an open area with no walls. Because the right side was always clear, Reeborg kept turning right and moving, which traced a small square back to where it started.

The fix was to walk straight until hitting a wall (`while front_is_clear(): move()`), then `turn_left()` so that wall is on Reeborg's right before the main loop starts.

After that I simplified the branches: the two "right is clear" checks merged into one `if right_is_clear():`, and the `elif` only needs `wall_in_front()`, since by then the right side is known to be blocked. I tested it across different random start positions and it reached the goal.

## How the code changed

I kept each version so you can see how the solution evolved:

1. [`versions/v1_original.py`](versions/v1_original.py) is my first version. It spun in circles in open areas.
2. [`versions/v2_infinite_loop_fix.py`](versions/v2_infinite_loop_fix.py) adds the fix: walk to a wall and turn left before the main loop.
3. [`versions/v3_merged_branches.py`](versions/v3_merged_branches.py) merges the two "right is clear" branches into one. Only the main program is shown, because `turn_right()` and `change_direction()` are the same as in version 2.
4. [`reeborg_maze.py`](reeborg_maze.py) is the final version, where the `elif` only checks `wall_in_front()`.
