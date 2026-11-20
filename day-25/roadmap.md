# Day 25 Roadmap: US States Game

```mermaid
flowchart TD
    A[Set up screen and load the blank map gif] --> B[Read 50_states.csv with pandas]
    B --> C[Make all_states list and empty guessed_states list]
    C --> D{Fewer than 50 guessed?}
    D -- yes --> E[Ask for a state, title shows N/50 correct]
    E --> F[Title-case the answer]
    F --> G{Answer is Exit?}
    G -- yes --> J[Loop ends]
    G -- no --> H{Answer in all_states?}
    H -- no --> D
    H -- yes --> I[Add to guessed, get its row, write name at x and y]
    I --> D
    D -- no --> J
    J --> K[Build missing_states list]
    K --> L[DataFrame then save states_to_learn.csv]
```

## Steps
1. Screen, title, and the blank map as a turtle shape (only .gif works).
2. Read the CSV, get the states as a list, and start an empty guessed list.
3. Loop: ask, title-case, check for Exit, check if it's a real state.
4. Correct guess: get the row, use .item() for x and y, write the name there.
5. After the loop: collect the missing states and save them to states_to_learn.csv.
