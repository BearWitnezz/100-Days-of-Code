# TODO 1: Import random. The deck is 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10. An ace starts as 11. The extra
#   10s are the face cards.

# TODO 2: Define begin() with a docstring. Loop until the answer is y or n. Ask "Do you want to play a game of
#   Blackjack? Type 'y' or 'n': ". y starts a hand. n stops. Anything else prints "Invalid input!".

# TODO 3: Define computers_turn(computers_cards, computers_current_score) with a docstring. While the computer's
#   score is under 17, draw one card from the deck and add the hand up again.

# TODO 4: In that same turn, while the computer is over 21 and still holds an 11, change the first 11 to 1 and
#   add the hand up again. Return the computer's cards and its score.

# TODO 5: Define blackjack() with a docstring. Start the hand as not over. Import the logo from art and print it.

# TODO 6: Deal two random cards to the player and two to the computer. Score each hand with sum. Remember the
#   computer's first card.

# TODO 7: Print the player's cards and current score. Print only the computer's first card.

# TODO 8: If the player has 21, the hand ends immediately. Print both final hands and scores, then
#   "Win with a Blackjack 😎".

# TODO 9: If the computer has 21 instead, print both final hands and scores, then
#   "Lose, opponent has Blackjack 😱".

# TODO 10: Loop while the hand is not over. When the player's score is not 21, ask "Type 'y' to get another card,
#   type 'n' to pass: ".

# TODO 11: On y, draw one card and rescore. While the score is over 21 and the hand still has an 11, change the
#   first 11 to 1 and rescore.
#   Nudge: do that before you decide the player busted, or an ace that could be 1 counts as a loss.

# TODO 12: Still over 21 ends the hand: print both final hands and scores, then "You lose 😤". Otherwise show the
#   player's cards and score again, and the computer's first card.

# TODO 13: On n, run the computer's turn, end the hand, and print both final hands and scores. Computer over 21
#   prints "Opponent went over. You win 😁". Equal scores print "Draw 🙃". A lower computer score prints
#   "You win 😃". Anything else prints "You lose 😤".

# TODO 14: If the player's score is 21 inside that loop, end the hand, let the computer take its turn, and print
#   both final hands. Equal scores are "Draw 🙃". Otherwise print "You win 😃".

# TODO 15: When the hand function finishes, call begin() so the player can play again. Call begin() once at the
#   bottom of the file to start the first game.

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def begin():
    """Ask whether to play a hand, then start one or stop."""
    lets_play = False
    while not lets_play:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play == 'y':
            lets_play = True
            blackjack()
        elif play == 'n':
            lets_play = True
        else:
            print("Invalid input!")
def computers_turn(computers_cards, computers_current_score):
    """Draw for the computer until its score reaches 17."""
    while computers_current_score < 17:
        computers_cards.append(random.choice(cards))
        computers_current_score = sum(computers_cards)
        while computers_current_score > 21 and 11 in computers_cards:
            computers_cards[computers_cards.index(11)] = 1
            computers_current_score = sum(computers_cards)
    return computers_cards, computers_current_score
def blackjack():
    """Play one blackjack hand, then ask to play again."""
    game_over = False
    from art import logo
    print(logo)
    your_cards = [random.choice(cards), random.choice(cards)]
    current_score = sum(your_cards)
    computers_cards = [random.choice(cards), random.choice(cards)]
    computers_first_card = computers_cards[0]
    computers_current_score = sum(computers_cards)
    print(f"    Your cards: {your_cards}, current score: {current_score}")
    print(f"    Computer's first card: {computers_first_card}")
    if current_score == 21:
        game_over = True
        print(f"    Your final hand: {your_cards}, final score: {current_score}")
        print(f"    Computer's final hand: {computers_cards}, final score: {computers_current_score}")
        print("Win with a Blackjack 😎")
    elif computers_current_score == 21:
        game_over = True
        print(f"    Your final hand: {your_cards}, final score: {current_score}")
        print(f"    Computer's final hand: {computers_cards}, final score: {computers_current_score}")
        print("Lose, opponent has Blackjack 😱")
    while not game_over:
        if current_score != 21:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == 'y':
                your_cards.append(random.choice(cards))
                current_score = sum(your_cards)
                while current_score > 21 and 11 in your_cards:
                    your_cards[your_cards.index(11)] = 1
                    current_score = sum(your_cards)
                if current_score > 21:
                    game_over = True
                    print(f"    Your final hand: {your_cards}, final score: {current_score}")
                    print(f"    Computer's final hand: {computers_cards}, final score: {computers_current_score}")
                    print("You lose 😤")
                else:
                    print(f"    Your cards: {your_cards}, current score: {current_score}")
                    print(f"    Computer's first card: {computers_first_card}")
            elif another_card == 'n':
                computers_cards, computers_current_score = computers_turn(computers_cards, computers_current_score)
                game_over = True
                print(f"    Your final hand: {your_cards}, final score: {current_score}")
                print(f"    Computer's final hand: {computers_cards}, final score: {computers_current_score}")
                if computers_current_score > 21:
                    print("Opponent went over. You win 😁")
                elif computers_current_score == current_score:
                    print("Draw 🙃")
                elif computers_current_score < current_score:
                    print("You win 😃")
                else:
                    print("You lose 😤")
        if current_score == 21:
            game_over = True
            computers_cards, computers_current_score = computers_turn(computers_cards, computers_current_score)
            print(f"    Your final hand: {your_cards}, final score: {current_score}")
            print(f"    Computer's final hand: {computers_cards}, final score: {computers_current_score}")
            if computers_current_score == current_score:
                print("Draw 🙃")
            else:
                print("You win 😃")
    begin()

begin()
