# Day 13 – Bugs Fixed (Debugging lesson)

1. **Describe the problem.** `for i in range(1, 20): if i == 20:` never printed. range stops before the end number. Fix: `range(1, 21)`.
2. **Reproduce the bug.** `dice_images[dice_num]` with `randint(1, 6)` sometimes crashed with IndexError, because indexes only go 0 to 5. Fix: `randint(0, 5)` or `dice_num - 1`.
3. **Play computer.** Year 1994 failed both `year < 1994` and `year > 1994`, so nothing printed. Fix: `year <= 1994`.
4. **Fix the errors.** `int(input())` crashed on bad input. Fix: wrap it in `try` / `except ValueError`. Also, a missing `f` on an f-string printed the variable name instead of its value.
5. **Print is your friend.** `word_per_page == int(input())` used `==` instead of `=`, so the total was 0. Fix: use `=`.
6. **Use a debugger.** `b_list.append(new_item)` sat outside the for loop, so only the last item got added. Fix: indent it into the loop.
