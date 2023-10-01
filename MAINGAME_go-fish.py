# Random module for shuffle of the deck and computers random game-guesses
import random
import os


# Class for the deck of cards & functions for the structure of the game.
class Deck:
    def __init__(self):
        self.cards = []
        values = ['ace', "2", "3", "4", "5", "6", "7", "8", "9", "10", "jacks", "queen", "king"]
        for _ in range(4):
            for value in values:
                card = value
                self.cards.append(card)

    # Function for randomizing the deck.
    def card_shuffle(self):
        random.shuffle(self.cards)

    # Function for pulling the last card from the deck and a printed text in case the deck gets empty.
    def draw(self):
        if not self.cards:
            print("The deck is now empty.")
            return None
        return self.cards.pop()

    # Function for dealing the first cards to empty lists for each player.
    def deal_cards(self):
        player = []
        computer = []
        for _ in range(5):
            card = self.draw()
            player.append(card)
        for _ in range(5):
            card = self.draw()
            computer.append(card)
        return player, computer

    def remaining_cards(self):
        return len(self.cards)

    # Function for reset of the deck.
    def reset(self):
        self.__init__()


def draw_border(text):
    border = '*' * 100
    return f"{border}\n{text.center(100)}\n{border}"


# Funktion för att skriva ut välkomstmeddelande och regler.
def print_welcome_message(player_name):
    welcome_message = f"♥ ♦ ♣ ♠ 𓆝 𓆟 𓆞 Welcome {player_name} to the game of Go Fish! 𓆝 𓆟 𓆞 ♠ ♣ ♦ ♥"
    rules = (
        "- You can only guess cards that you have in your hand.",
        "- If you guess a card that's not on your hand, you get to skip a round.",
        "- When you collect four of the same card, you earn a point.",
        "- The first player to reach 3 points wins.",
        "- You can always exit by typing 'x'."
    )
    return draw_border(welcome_message) + "\n" + "\n".join(rules)


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Huvudspel
def main_game():
    gamer_tag = input("Enter your game-tag: ")
    player = gamer_tag
    nemesis = "Computer"
    player_cards = []
    player_score = 0
    computer_cards = []
    computer_score = 0
    computer_guesses = (['ace', "2", "3", "4", "5", "6", "7", "8", "9", "10", "jacks", "queen", "king"] * 4)

    deck = Deck()
    deck.card_shuffle()
    symbol_list = [' ♥ ', ' ♦ ', ' ♣ ', ' ♠ ']
    symbols = ' '.join(symbol_list * 6)
    symbol_string = random.choice(symbols)

    player_cards, computer_cards = deck.deal_cards()

    # Skriv ut välkomstmeddelande och regler en gång i början av spelet.
    clear_terminal()
    print(print_welcome_message(player))
    print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
    print("Player cards: ")
    print(*player_cards, sep=', ')
    print(symbols + symbol_list[0])
    print("")

    while True:
        player_choice = input("Which card would you like to steal from your opponent? >:) ")
        clear_terminal()

        player_card_count = player_cards.count(player_choice)
        computer_card_count = computer_cards.count(computer_guesses)

        if player_choice in player_cards:
            if player_choice in computer_cards:
                while player_choice in computer_cards:
                    computer_cards.remove(player_choice)
                    player_cards.append(player_choice)
                print(print_welcome_message(player))
                print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
                print("Player cards: ")
                print(*player_cards, sep=', ')
                print(symbols + symbol_list[0])
                print("")
                print(f"It's super effective! You stole {player_choice} from Computer!")
                print("")

                player_card_count = player_cards.count(player_choice)
                if player_card_count == 4:
                    player_cards = [card for card in player_cards if card != player_choice]
                    player_score += 1
                    print("")
                    clear_terminal()
                    print(print_welcome_message(player))
                    print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
                    print("Player cards: ")
                    print(*player_cards, sep=', ')
                    print(symbols + symbol_list[0])
                    print("")
                    print("! You scored a point !")
                    print("")
            else:
                new_card = deck.draw()
                player_cards.append(new_card)
                print(print_welcome_message(player))
                print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
                print("Player cards: ")
                print(*player_cards, sep=', ')
                print(symbols + symbol_list[0])
                print("")
                print(f"Computer doesn't have the card you asked for. Go Fish!")
                print(f"You picked up: {player_cards[-1]}")
                print("")

        else:
            print(print_welcome_message(player))
            print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
            print("Player cards: ")
            print(*player_cards, sep=', ')
            print(symbols + symbol_list[0])
            print("")
            print("")
            print("You can only pick cards you have on your hand. Better luck next time.")
            print("")

        while True:
            computer_guesses = random.choice(computer_cards)
            if computer_guesses in player_cards:
                while computer_guesses in player_cards:
                    player_cards.remove(computer_guesses)
                    computer_cards.append(computer_guesses)
                clear_terminal()
                print(print_welcome_message(player))
                print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
                print("Player cards: ")
                print(*player_cards, sep=', ')
                print(symbols + symbol_list[0])
                print("")
                print("Computer guessing . . . ", computer_guesses)
                print(f"{nemesis} stole {computer_guesses} from you!")
                print("")

                computer_card_count = computer_cards.count(computer_guesses)
                if computer_card_count == 4:
                    computer_cards = [card for card in computer_cards if card != computer_guesses]
                    computer_score += 1
                    clear_terminal()
                    print(print_welcome_message(player))
                    print(draw_border(f"Player score: {player_score} Computer score: {computer_score}"))
                    print("Player cards: ")
                    print(*player_cards, sep=', ')
                    print(symbols + symbol_list[0])
                    print("")
                    print("! Computer scored a point !")
                    print("")
                break
            else:
                print(f"Computer guessing . . . {computer_guesses}!")
                print("Your nemesis guessed wrong. Go Fish! ")
                print("")
                new_card = deck.draw()
                computer_cards.append(new_card)
                break

        if player_score >= 3:
            print(draw_border("Game Over! You Won!"))
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break

        elif computer_score >= 3:
            print(draw_border("Game Over! Computer Won!"))
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break


if __name__ == "__main__":
    main_game()
