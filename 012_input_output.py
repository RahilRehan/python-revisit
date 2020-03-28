# formatted string literals

year = 2020
event = "Techfest"
print(f'Results of the {year} {event}')


#lining up input with :
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
	print(f'{name:10} => {phone:10d}')


# the string format()
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
#accessing dictionaries
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ' 'Dcab: {0[Dcab]:d}'.format(table))

# pretty table
for x in range(1,11):
	print("{0:2d} {0:3d} {0:4d}".format(x, x*x, x*x*x))



#files
# f = open("workfile", 'w')  #old method
# f.close()

with open("workfile", "r+") as f:  #good with handling exception too
	# read_data = f.read() #reads all data, pass arg to tell how much to read
	for line in f.readlines():
		print(line)
	f.write("I wrote this now")

	f.seek(5)
	print("something new: ", f.read(10))

print(f.closed) #file closes after with


#json
import json

# json.dump(x, f)  #puts python objects to json
# x = json.load(f) #loads json


