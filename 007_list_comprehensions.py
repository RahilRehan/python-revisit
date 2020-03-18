squares = []
for x in range(5):
	squares.append(x**2)

squares = list(map(lambda x:x**2, range(5)))

squares = [x**2 for x in range(5)]

print(squares)

combs = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x!=y:
			combs.append((x,y))
print(combs)

combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]  #nested list comprehension
print(combs)


vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x*2 for x in vec])

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

# apply a function to all the elements
print([abs(x) for x in vec])

#method to all elements
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

#flatten
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for li in vec for num in li])


##Nested List Comprehensions
matrix = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]
]

transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)

