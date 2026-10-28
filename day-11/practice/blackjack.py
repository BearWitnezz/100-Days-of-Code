import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def begin():
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
    while computers_current_score < 17:
        computers_cards.append(random.choice(cards))
        computers_current_score = sum(computers_cards)
        while computers_current_score > 21 and 11 in computers_cards:
            computers_cards[computers_cards.index(11)] = 1
            computers_current_score = sum(computers_cards)
    return computers_cards, computers_current_score
def blackjack():
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
        if current_score == 21:
            game_over = True
            computers_cards, computers_current_score = computers_turn(computers_cards, computers_current_score)
            print(f"    Your final hand: {your_cards}, final score: {current_score}")
            print(f"    Computer's final hand: {computers_cards}, final score: {computers_current_score}")
            if computers_current_score == current_score:
                print("Draw 🙃")
            else:
                print("You win 😃")
        elif another_card == 'y':
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
    begin()

begin()
