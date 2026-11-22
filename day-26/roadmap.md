# Day 26 Roadmap: NATO Phonetic Alphabet

```mermaid
flowchart TD
    A[Import pandas] --> B[Read nato_phonetic_alphabet.csv into a DataFrame]
    B --> C[Loop rows with iterrows]
    C --> D[Build a dict of letter to code with a dictionary comprehension]
    D --> E[Ask the user for a word]
    E --> F[Make the word uppercase]
    F --> G[Loop each letter with a list comprehension]
    G --> H[Look up each letter's code in the dict]
    H --> I[Print the list of code words]
```

## Steps
1. Read the CSV with pandas.
2. Build the letter-to-code dictionary with a dictionary comprehension over iterrows().
3. Ask for a word and uppercase it so it matches the keys.
4. Build the list of code words with a list comprehension.
5. Print the list.
