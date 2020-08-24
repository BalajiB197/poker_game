import functools

a = []

rules = {1:['acehearts','kinghearts','queenhearts','jackhearts','10hearts'],
		2:['10clubs','9clubs','8clubs','7clubs','6clubs'],
		3:['queenclubs','queenhearts','queenspades','queendiamonds','5clubs'],
		4:['acehearts','acespades','acediamonds','kingspades','kinghearts'],
		5:['kinghearts','8hearts','6hearts','4hearts','2hearts'],
		6:['8hearts','7clubs','6diamonds','5spades','4hearts'],
		7:['queenclubs','queenhearts','queenspades','7hearts','2clubs'],
		8:['jackdiamonds','jackspades','9spades','9diamonds','5clubs'],
		9:['kinghearts','kingspades','9diamonds','8spades','4hearts'],
		10:['acehearts','queenclubs','6hearts','4spades','2diamonds']}

gameTitle = ['Royal Flush', 'Straight flush', 'four of a kind', 'full house', 'Flush', 
			 'Straight', 'Three of a kind', 'Two pair', 'One pair', 'High card']

def myfunc(v,s):
	'''
	v = list of vals in poker cards
	s = list of suits in poker cards game
	'''
	for i in range(len(v)):
		for j in range(len(s)):
			a.append(v[i]+s[j])
	return a


def poker_game(l1: 'Player1', l2: 'Player2') -> 'Returns Player won the match':
	'''
	finds the winner between 2 player poker game based on
	given set of winning rules
	l1 - player 1 list of cards, varies between 3 to 5 cards
	l2 - player 2 list of cards, varies between 3 to 5 cards
	return - the winner of the game.
	'''
	l1, l2 = sorted(l1), sorted(l2)
	cmp1, cmp2 = 0,0
	if l1 == l2:
		print('Won Equal points, DRAW MATCH!!')
	elif len(l1) == len(l2) and len(l1)>=3 and len(l1)<=5:
		for key,value in rules.items():
			if len(l1) == 5:
				if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,sorted(value),l1), True):
					cmp1 = key
				elif functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,sorted(value),l2), True):
					cmp2 = key
			elif len(l1) == 4:
				for k in range(len(value)):
					tmp = []
					tmp.extend(value) 
					del tmp[k]
					if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,sorted(tmp),l1), True):
						cmp1 = key
					elif functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,sorted(tmp),l2), True):
						cmp2 = key
			elif len(l1) == 3:
				for k in range(len(value)-1):
					tmp = []
					tmp.extend(value) 
					del tmp[k]
					del tmp[k]
					if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,sorted(tmp),l1), True):
						cmp1 = key
					elif functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,sorted(tmp),l2), True):
						cmp2 = key
                    
		if cmp1 < cmp2:
			return 'Player 1 won the match {0}'.format(gameTitle[cmp1-1])
		else:
			return 'Player 2 won the match {0}'.format(gameTitle[cmp2-1])



