# Secret Work Order Code Roadmap

Follow the stages in order. Finish and test one stage before you start the next, and only build what that stage asks for.

## The big picture

```mermaid
flowchart TD
    start([Start]) --> ask[Ask: encode or decode?<br/>message? shift?]
    ask --> call[Call the function<br/>with message, shift, direction]
    call --> dir{Encode or decode?}
    dir -- decode --> flip[Flip the shift the other way]
    dir -- encode --> loop
    flip --> loop[Go through each letter]
    loop --> isletter{Is it a letter?}
    isletter -- yes --> move[Move it by the shift<br/>wrap around after z]
    isletter -- no --> keep[Keep it as is]
    move --> show[Print the result]
    keep --> show
    show --> again{Go again?}
    again -- yes --> ask
    again -- no --> stop([Stop])
```

**One stage at a time:** write a stage, run it, and make sure it works before you touch the next one. If something breaks, it is almost always in the stage you just wrote.

## Stage 1: The alphabet
1. **Store the alphabet** in a list.
2. **Find a letter.** Which list method tells you the position of an item?

Test it: print the position of "a" and "z". Are they what you expected?

## Stage 2: Shift one letter
1. **Move forward.** If you add the shift to a position, what letter is there?
2. **Wrap around.** What happens if you shift "z" by 1? Which operator gives you the remainder so you land back at the start?

Test it: shift "a" by 3, then "z" by 1. Do you get "d" and "a"?

## Stage 3: Make it a function
1. **Inputs.** What does the function need to know? Name each parameter.
2. **Whole message.** How do you go through every letter and build up a new string?
3. **Not a letter?** What should happen to spaces, numbers and punctuation?

Test it: encode "fix sink" with shift 5. Do the spaces stay spaces?

## Stage 4: Decode
1. **The other way.** How is decoding just encoding with a different shift?
2. **One function or two?** Can one function do both if you pass in the direction?
3. **Keyword arguments.** Try calling it with names, like naming each value. Does the order still matter?

Test it: encode a message, then decode the result with the same shift. Do you get the original back?

## Stage 5: Go again
1. **Ask the questions** for direction, message and shift. Which one needs converting to a number?
2. **Repeat.** Which loop lets the player go again until they say no?

Test it: encode, then choose to go again and decode. Does it stop when you say no?

## Stage 6: Tidy up and break it
1. **Break it on purpose.** A huge shift like 100? A typo in encode? Capital letters?
2. **Explain it out loud.** Can you say what each parameter does and what you passed in for it?
