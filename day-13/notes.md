# Day 13 — Debugging

## 1. Describe the problem
- Untangle it: what is the code doing, what should happen, what assumptions are you making?
- Example: `for i in range(1, 20): if i == 20: print("You got it")` never prints. The assumption that i reaches 20 is false, because range stops before the end number. Fix: `range(1, 21)`.

## 2. Reproduce the bug
- A bug that only happens sometimes is hard to fix, so find when it happens and make it happen every time.
- Example: `dice_images[dice_num]` with `dice_num = randint(1, 6)`. randint includes both ends, so 6 gives `IndexError: list index out of range` (indexes are 0 to 5). Fix: `randint(0, 5)`, or `dice_images[dice_num - 1]`.

## 3. Play computer
- Go line by line with a real value and work out what each condition evaluates to.
- Example: year 1994 with `year > 1980 and year < 1994` / `elif year > 1994`. Both are False, so nothing prints. Fix: `year <= 1994`.

## 4. Fix the errors
- Editor errors are underlined (e.g. "expected an indented block").
- Console errors: copy the general part of the message (not your own values) and Google it with "Python".
- New: try / except catches an error so the program doesn't crash:
  - put the risky line (`age = int(input(...))`) under `try:`
  - under `except ValueError:` print a helpful message and ask again.
- Some bugs have no error at all, like a missing `f` on an f-string printing the variable name instead of its value.

## 5. Print is your friend
- Print variables before the final result to see which one is wrong.
- Example: `word_per_page == int(input(...))` used `==` (comparison, gives True/False, changes nothing) instead of `=` (assignment), so the total was 0.

## 6. Use a debugger
- Breakpoint: click the gutter by a line number. Debug run pauses there.
- Step Over: run the next line. Step Into: go into a function, even library ones like randint. Step Into My Code: only your own functions. Step Out: go back up.
- Watch the Variables tab change as you step. The Console tab shows prints.
- Example: `b_list.append(new_item)` was outside the for loop, so only the last item was added. Fix: indent it into the loop.

## 7–10. Final tips
- Take a break: rest or sleep, then come back.
- Ask a friend: fresh eyes don't share your assumptions.
- Run often: test after every small change, and fix bugs one at a time.
- Stack Overflow: search it first, and only ask when your problem seems truly unique.
- Every bug you fix is one rep.
