from random import choice

def get_computer_choice() -> str:
    """Returns a single-letter choice at random"""
    return choice(['R', 'P', 'S'])

def get_player_input():
    """prompts player for single input until correct"""
    text = ""
    while text not in ['R', 'P', 'S']:


        text = input("Choose [R]ock, [P]layer or [S]cissors")

        text = text.upper()


    return text

def score_game(player, computer):
    """Calculates the winner"""
    score = player + computer
    if score == "RS" or score == "SP" or score == "PR":
        return "player_win"
    if score == "SR" or score == "PS" or score == "RP":
        return "computer_win"
    if player == computer:
        return "draw"
