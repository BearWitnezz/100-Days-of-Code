# Secret Work Order Code Rebuild Roadmap

Follow the stages in order. Finish and test one stage before you start the next, and only build what that stage asks for.

## The big picture

```mermaid
flowchart TD
    start([Start]) --> welcome[Print a welcome message]
    welcome --> askdir[Ask: encode or decode?]
    askdir --> ok{Encode or decode?}
    ok -- neither --> bad[Say the input is invalid]
    ok -- encode or decode --> ask[Ask for the message and the shift]
    ask --> call[Call caesar]
    call --> way{Which direction?}
    way -- encode --> forward[Shift each letter forward and wrap]
    way -- decode --> back[Shift each letter backward and wrap]
    forward --> keep[Leave non-letters unchanged and print]
    back --> keep
    keep --> again{Continue?}
    again -- n --> stop([Stop])
    again -- anything else --> askdir
    bad --> askdir
```

**One stage at a time:** write a stage, run it, and make sure it works before you touch the next one. If something breaks, it is almost always in the stage you just wrote.

## Stage 1: The alphabet
1. **Store the lowercase alphabet** in a list.
2. **Find a letter's position** with the list method that searches for an item.

Test it: print where `a` and `z` sit.

## Stage 2: Encode
1. **Define `caesar`** with the message, the shift, and the direction. Add a docstring.
2. **When the direction is encode,** walk the message. A letter moves forward by the shift and wraps with the remainder operator. Anything else is copied unchanged.
3. **Print the finished string.**

Test it: encode `a z!` by 1. Do you get `b a!`?

## Stage 3: Decode
1. **A second if, not an elif.** When the direction is decode, walk the message again and subtract the shift, still wrapping.
2. **Non-letters stay** on this path too.
3. **A direction that is neither** does not enter either if, so this function prints nothing for it. The next stage is what rejects that direction, before the function is called.

Test it: encode a work order, then decode that result with the same shift. Do you get the original message back?

## Stage 4: Reject a bad direction first
1. **Welcome them once,** before the loop.
2. **Ask encode or decode** and make it lowercase.
3. **If it is neither,** print that the input is invalid, and do not ask for the message or the shift.
4. **Only a real direction** asks for the message and the shift, then calls `caesar`.

Test it: type `encrypt`. Does it stop you before the message question? Type `encode` and confirm it still asks.

## Stage 5: Another message
1. **Loop while a flag is true.**
2. **Ask y or n only after a real encode or decode.** An invalid direction does not ask. The loop just asks for a direction again.
3. **`n` sets the flag false.** Any other answer leaves it true.

Test it: code one message, say y, code another, say n. Does it stop? Then type a bad direction. Does it skip the continue question and ask for a direction again?

## Stage 6: Tidy up and break it
1. **Break it on purpose.** `ENCODE`, a shift of 100, a message that is only `123`.
2. **Explain it out loud.** Why is the bad-direction check outside the function, and why are encode and decode two separate ifs?
