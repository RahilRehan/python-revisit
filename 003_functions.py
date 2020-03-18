#Functions

def fib(n):
	result = []
	a, b = 0, 1
	while a<n:
		result.append(a)
		a, b = b, a+b
	return result
res = fib(10)
print(res)


# *args vs *kwargs
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# lambdas
def make_incrementor(n):
	"""
	This is a docstring
	"""
	return lambda x: x + n
f = make_incrementor(42)
print(f(0))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])  #sorted alphabetically
print(pairs)

#function annotations -> extra info about the type of parameters and return type
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs
f('spam')

# Note
# Please refer PEP8