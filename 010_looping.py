#dictionary looping
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
	print(k,v)

#enumerate
for i, v in enumerate(["tic","tac", "toe"]):
	print(i, v)


#pairing two sequences
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print(q,a)

#reverse ranging
for i in reversed(range(1, 10, 2)):
	print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
	print(f)