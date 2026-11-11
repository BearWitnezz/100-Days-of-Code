# Hirst Spot Painting Roadmap

Follow the stages in order. Finish and test one stage before you start the next, and only build what that stage asks for.

This program opens a turtle window. Run it on a desktop Python that can show a GUI. The running program paints from a list of colors. It does not extract colors from the picture while it runs.

## The big picture

```mermaid
flowchart TD
    start([Start]) --> colors[Keep the list of RGB colors]
    colors --> setup[Set the color mode, pick up the pen, start at the corner]
    setup --> row[Start the next row]
    row --> dot[Paint a random colored dot and move forward]
    dot --> across{10 dots in this row?}
    across -- no --> dot
    across -- yes --> up[Step up to the next row]
    up --> rows{10 rows done?}
    rows -- no --> row
    rows -- yes --> hide[Hide the turtle]
    hide --> click[Wait for a click]
    click --> stop([Stop])
```

**One stage at a time:** write a stage, run it, and make sure it works before you touch the next one. If something breaks, it is almost always in the stage you just wrote.

## Stage 1: The colors
1. **Keep the extracted colors** in a list of RGB tuples. Each tuple is three numbers, red, green, and blue.
2. **Import `random` and turtle.** You need both `Turtle` and `Screen`.

Test it: print how many colors are in the list, and print one tuple. Does it have three numbers?

## Stage 2: One dot
1. **Turtle's color mode has to be 255** before a dot can use those RGB tuples. Where is that set?
2. **Create the turtle, give it a turtle shape, and pick the pen up** so moving does not draw a line.
3. **`dot` takes a size and a color.** Use size 20, and pick the color at random from the list.
4. **Move forward 50** after the dot so the next one is not on top of it.

Test it: paint a single dot and move. Do you see one spot, and no line connecting to it?

## Stage 3: Ten dots across, ten rows up
1. **Define `hirst` with the number of rows.** Add a docstring.
2. **Start at x -255, y -255.** Which turtle method jumps to a coordinate?
3. **An inner loop paints 10 dots** per row, each a new random color, each followed by a forward move.
4. **After the row, move y up by 50** and jump back to x -255 at that new y. The rows have to line up on the left.
5. **Hide the turtle** when the rows are done.

Test it: call `hirst(2)`. Do you get 2 rows of 10 dots, stacked 50 apart, with the second row starting at the same x as the first?

## Stage 4: The full painting, then wait
1. **Call `hirst(10)`** for the finished 10 by 10 painting.
2. **Create a screen and wait for a click** before the window closes. Which screen method does that?

Test it: run the file. Do you get 10 rows of 10 dots, in mixed colors, and does the window stay open until you click it?

## Stage 5: Tidy up and break it
1. **Break it on purpose.** Call `hirst(1)`, then `hirst(0)`. What does each one paint?
2. **Explain it out loud.** What do the inner loop and the outer loop each repeat, and why is the pen up?
