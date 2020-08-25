import os
import session6
from session6 import *
import pytest
from test_utils import *
import random

README_CONTENT_CHECK_FOR = ['poker_game', 'Royal Flush']

cards = ['2spades','2clubs','2hearts','2diamonds','3spades','3clubs','3hearts',
 '3diamonds', '4spades', '4clubs', '4hearts', '4diamonds', '5spades', '5clubs',
  '5hearts', '5diamonds', '6spades', '6clubs', '6hearts', '6diamonds', '7spades',
   '7clubs', '7hearts', '7diamonds', '8spades', '8clubs', '8hearts', '8diamonds',
    '9spades', '9clubs', '9hearts', '9diamonds', '10spades', '10clubs', '10hearts',
     '10diamonds', 'jackspades', 'jackclubs', 'jackhearts', 'jackdiamonds', 'queenspades',
      'queenclubs', 'queenhearts', 'queendiamonds', 'kingspades', 'kingclubs', 'kinghearts',
       'kingdiamonds', 'acespades', 'aceclubs', 'acehearts', 'acediamonds']

v = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
s = ['spades', 'clubs', 'hearts', 'diamonds']

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_fourspace_equal():
    assert fourspace(session6) == True, 'Not all spaces before lines are a multiple of 4!'

def test_function_names():
    assert function_name_had_cap_letter(session6) == False, "One of your function has a capitalized alphabet!"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_winner_1():
    l1 = ['acehearts','kinghearts','queenhearts','jackhearts','10hearts']
    l2 = ['acehearts','acespades','acediamonds','kingspades','kinghearts']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match Royal Flush'

def test_winner_2():
    l1 = ['10clubs','9clubs','8clubs','7clubs','6clubs']
    l2 = ['queenclubs','queenhearts','queenspades','queendiamonds','5clubs']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match Straight flush'

def test_winner_3():
    l1 = ['10clubs','9clubs','7clubs','6clubs']
    l2 = ['queenclubs','queenspades','queendiamonds','5clubs']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match Straight flush'

def test_winner_4():
    l1 = ['queenclubs','queenhearts','queenspades','queendiamonds','5clubs']
    l2 = ['acehearts','acespades','acediamonds','kingspades','kinghearts']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match four of a kind'

def test_winner_5():
    l1 = ['queenclubs','queenspades','queendiamonds','5clubs']
    l2 = ['acehearts','acespades','kingspades','kinghearts']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match four of a kind'

def test_winner_6():
    l1 = ['8hearts','6hearts','4hearts','2hearts']
    l2 = ['acespades','acediamonds','kingspades','kinghearts']
    assert session6.poker_game(l1, l2) == 'Player 2 won the match full house'

def test_winner_7():
    l1 = ['kinghearts','kingspades','9diamonds','8spades','4hearts']
    l2 = ['acehearts','queenclubs','6hearts','4spades','2diamonds']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match One pair'

def test_winner_8():
    l1 = ['kinghearts','kingspades','8spades','4hearts']
    l2 = ['acehearts','queenclubs','4spades','2diamonds']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match One pair'

def test_winner_9():
    l2 = ['kinghearts','kingspades','4hearts']
    l1 = ['acehearts','queenclubs','2diamonds']
    assert session6.poker_game(l1, l2) == 'Player 2 won the match One pair'

def test_winner_10():
    l1 = ['8hearts','7clubs','6diamonds','5spades','4hearts']
    l2 = ['queenclubs','queenhearts','queenspades','7hearts','2clubs']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match Straight'

def test_winner_11():
    l1 = ['8hearts','7clubs','6diamonds','5spades','4hearts']
    l2 = ['queenclubs','queenhearts','queenspades','7hearts','2clubs']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match Straight'

def test_winner_12():
    l2 = ['8hearts','7clubs','6diamonds','5spades','4hearts']
    l1 = ['queenclubs','queenhearts','queenspades','7hearts','2clubs']
    assert session6.poker_game(l1, l2) == 'Player 2 won the match Straight'

def test_winner_13():
    l1 = ['acehearts','acespades','acediamonds','kingspades','kinghearts']
    l2 = ['kinghearts','8hearts','6hearts','4hearts','2hearts']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match full house'

def test_winner_14():
    l1 = ['acehearts','acespades','kingspades','kinghearts']
    l2 = ['kinghearts','8hearts','6hearts','4hearts']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match full house'

def test_winner_15():
    l1 = ['acehearts','acespades','kinghearts']
    l2 = ['kinghearts','8hearts','6hearts']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match full house'

def test_winner_16():
    l1 = ['acehearts','kinghearts','queenhearts','jackhearts','10hearts']
    l2 = ['acehearts','queenclubs','6hearts','4spades','2diamonds']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match Royal Flush'

def test_winner_17():
    l1 = ['acehearts','kinghearts','jackhearts','10hearts']
    l2 = ['queenclubs','6hearts','4spades','2diamonds']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match Royal Flush'

def test_winner_18():
    l1 = ['acehearts','4spades','2diamonds']
    l2 = ['jackdiamonds','9diamonds','5clubs']
    assert session6.poker_game(l1, l2) == 'Player 2 won the match Two pair'

def test_winner_19():
    l1 = ['queenclubs','queenhearts','queenspades','queendiamonds','5clubs']
    l2 = ['jackdiamonds','jackspades','9spades','9diamonds','5clubs']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match four of a kind'

def test_winner_20():
    l2 = ['acehearts','kinghearts','queenhearts','jackhearts']
    l1 = ['acehearts','acespades','acediamonds','kingspades']
    assert session6.poker_game(l1, l2) == 'Player 2 won the match Royal Flush'

def test_doc_string_2():
    assert help(session6.myfunc) != ''

def test_doc_string_2a():
    assert session6.myfunc.__doc__ != ''

def test_doc_string_3():
    assert session6.poker_game.__doc__ != ''

def test_annotation_3():
    assert session6.poker_game.__annotations__ != ''

def test_manual_deck_52_cards():
    assert session6.myfunc(v,s) == cards

def test_poker_game_length_1():
    l2 = ['acehearts','kinghearts','queenhearts','jackhearts','kingspades']
    l1 = ['acehearts','acespades','acediamonds','kingspades']
    with pytest.raises(ValueError):
        session6.poker_game(l1, l2)

def test_poker_game_length_2():
    l2 = ['acehearts','kinghearts','queenhearts']
    l1 = ['acehearts','acespades']
    with pytest.raises(ValueError):
        session6.poker_game(l1, l2)

def test_poker_game_length_3():
    l2 = ['acehearts','kinghearts']
    l1 = ['acehearts','acespades']
    with pytest.raises(ValueError):
        session6.poker_game(l1, l2)

def test_poker_game_length_4():
    l2 = []
    l1 = ['acehearts','acespades']
    with pytest.raises(ValueError):
        session6.poker_game(l1, l2)

def test_poker_game_length_5():
    l2 = ['acehearts','kinghearts']
    l1 = ['acehearts','acespades','acediamonds','kingspades']
    with pytest.raises(ValueError):
        session6.poker_game(l1, l2)

def test_poker_game_length_6():
    l2 = ['acehearts','kinghearts','queenhearts','jackhearts','kingspades']
    l1 = ['acehearts']
    with pytest.raises(ValueError):
        session6.poker_game(l1, l2)

def test_52_cards():
    tmp = []
    tmp.extend(v)
    t = random.randint(0,13)
    del tmp[t] # del random value
    with pytest.raises(ValueError):
        session6.myfunc(tmp,s)

def test_52_cards_2():
    tmp = []
    tmp.extend(s) 
    t = random.randint(0,4)
    del tmp[t] # del random value
    with pytest.raises(ValueError):
        session6.myfunc(v,tmp)

def test_same_cards():
    l2 = ['acehearts','kinghearts','queenhearts','jackhearts']
    l1 = ['acehearts','kinghearts','queenhearts','jackhearts']
    assert session6.poker_game(l1, l2) == 'Won Equal points, DRAW MATCH!!'

def test_same_cards_2():
    l2 = ['queenhearts','jackhearts','queenhearts','jackhearts']
    l1 = ['queenhearts','jackhearts','queenhearts','jackhearts']
    assert session6.poker_game(l1, l2) == 'Won Equal points, DRAW MATCH!!'




