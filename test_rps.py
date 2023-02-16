import pytest

from rps import get_computer_choice,score_game,get_player_input

def test_computer_choice_is_valid():
    """Checks if computer only chooses R, P, S """
    assert get_computer_choice() in ["R", "P", "S"]
test_data = [
    ['R', 'S', 'player_win'],
    ['P', 'P', 'draw'],
    ['R', 'R', 'draw']
]
@pytest.mark.parametrize("player,computer,expected", test_data)

def test_scoring_accuracy(player, computer, expected):
    assert score_game(player, computer) == expected

test_inputs = [
    [["r"], "R"],
    [["t", "r"], "R"]
]

@pytest.mark.parametrize("value,expected", test_inputs)

def test_player_input_is_valid(monkeypatch, value, expected):
    """Checks that the player choice is R, P, S"""
    choices = iter(value)
    monkeypatch.setattr('builtins.input', lambda x: next(choices))

    assert get_player_input() == expected

