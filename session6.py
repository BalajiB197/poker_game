import functools


v = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
s = ['spades', 'clubs', 'hearts', 'diamonds']
a = []

def myfunc(v,s):
	'''
	v = list of vals in poker cards
	s = list of suits in poker cards game
	'''
	for i in range(len(v)):
		for j in range(len(s)):
			a.append(v[i]+s[j])
	return a

res =  myfunc(v,s)

rules = {1:['ace','king','queen','jack','10'],2:['10','9','8','7','6'],
		3:['queen','queen','queen','queen','5'],4:['ace','ace','ace','king','king'],
		5:['king','8','6','4','2'],6:['8','7','6','5','4'],
		7:['queen','queen','queen','7','2'],8:['jack','jack','9','9','5'],
		9:['king','king','9','8','4'],10:['ace','queen','6','4','2']}


def poker_game(l1, l2):
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
                    
        print(cmp1, cmp2)
        if cmp1 < cmp2:
            print('Player 1 won the match')
        else:
            print('Player 2 won the match')


l1 = ['ace','king','queen','jack','10']
l2 = ['10','9','8','7','6']

poker_game(l1, l2)




