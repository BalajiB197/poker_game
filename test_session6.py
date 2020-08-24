import os
import session6
from session6 import *
import pytest


cards = ['2spades', '2clubs', '2hearts', '2diamonds', '3spades', '3clubs', '3hearts', '3diamonds', 
'4spades', '4clubs', '4hearts', '4diamonds', '5spades', '5clubs', '5hearts', '5diamonds', 
'6spades', '6clubs', '6hearts', '6diamonds', '7spades', '7clubs', '7hearts', '7diamonds', 
'8spades', '8clubs', '8hearts', '8diamonds', '9spades', '9clubs', '9hearts', '9diamonds', 
'10spades', '10clubs', '10hearts', '10diamonds', 'jackspades', 'jackclubs', 'jackhearts', 
'jackdiamonds', 'queenspades', 'queenclubs', 'queenhearts', 'queendiamonds', 'kingspades', 
'kingclubs', 'kinghearts', 'kingdiamonds', 'acespades', 'aceclubs', 'acehearts', 'acediamonds']

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_winner():
    l1 = ['acehearts','kinghearts','queenhearts','jackhearts','10hearts']
    l2 = ['acehearts','acespades','acediamonds','kingspades','kinghearts']
    assert session6.poker_game(l1, l2) == 'Player 1 won the match Royal Flush'