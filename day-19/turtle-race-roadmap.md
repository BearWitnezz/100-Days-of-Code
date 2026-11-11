# Turtle Race Roadmap

Follow the stages in order. Finish and test one stage before you start the next, and only build what that stage asks for.

This program opens a turtle window and a popup. Run it on a desktop Python that can show a GUI.

## The big picture

```mermaid
flowchart TD
    start([Start]) --> popup[Ask which color will win]
    popup --> printbet[Print that bet]
    printbet --> line[Line up one turtle of each color]
    line --> bet{Did they enter a bet?}
    bet -- no --> click[Wait for a click]
    bet -- yes --> step[Move every turtle forward by a small random amount]
    step --> finish{Any turtle past the finish line?}
    finish -- no --> step
    finish -- yes --> won{Is it the color they bet?}
    won -- yes --> yesmsg[Say they won and name the color]
    won -- no --> nomsg[Say they lost and name the color]
    yesmsg --> click
    nomsg --> click
    click --> stop([Stop])
```

**One stage at a time:** write a stage, run it, and make sure it works before you touch the next one. If something breaks, it is almost always in the stage you just wrote.

## Stage 1: Take the bet
1. **Import `Turtle` and `Screen`,** and import `random`.
2. **A race flag starts false.** The race does not run until there is a bet.
3. **Make a screen and set it up** at width 500 and height 400.
4. **A popup asks which turtle will win.** Which screen method asks with a title and a prompt?
5. **Print whatever they typed,** including when they cancel the popup.

Test it: enter `red` and confirm the terminal prints `red`. Run it again and cancel the popup. What gets printed?

## Stage 2: Line up the turtles
1. **The colors, in this order,** are red, orange, yellow, green, blue, and violet.
2. **An empty list** will hold the turtles.
3. **For each color,** make a turtle with the turtle shape, set its color, and pick the pen up.
4. **Send them all to x -230.** The first one starts at y -100, and each next one is 50 higher. Which method moves a turtle to a coordinate without drawing?
5. **Append each turtle** to the list.

Test it: run it and look at the window before anyone moves. Six turtles, one of each color, in a column at the left?

## Stage 3: Race only if they bet
1. **If the popup returned a bet, set the race flag true.** Cancelling the popup leaves the flag false, so the loop never starts. The window still waits for a click at the end.
2. **While the race is on, loop the turtles.** Each one moves forward by a random whole number from 0 to 10. Is the top of that range included?
3. **A turtle past x 230** ends the race. Which method reads a turtle's x coordinate?

Test it: bet on `red` and watch the window. Do they all move, and does the race stop when one crosses, instead of everyone finishing?

## Stage 4: Say who won
1. **The winner is the turtle that crossed.** Its pencolor is the winning color.
2. **If that color equals the bet,** say they won and name the color. Otherwise say they lost and name the winning color.
3. **Stop checking the other turtles** on that pass. A `break` leaves the for loop. The flag is what keeps the while loop from starting another pass.
4. **After the race, or after a cancelled bet, wait for a click** to close the window.

Test it: bet on a color, then bet on a different one. Does the terminal name the turtle that actually crossed, and does it agree with your bet only when the colors match?

## Stage 5: Tidy up and break it
1. **Two turtles can cross on the same pass.** Your loop checks them in list order and stops at the first one past the line. Which color would win if red and violet both crossed together?
2. **Break it on purpose.** Bet `Red` with a capital R. Bet `purple`, which is not in the list. Cancel the popup.
3. **Explain it out loud.** Why does the race flag start false, and what turns it true?
