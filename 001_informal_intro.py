import sys
print(sys.argv)  #arguments passing, argv[0] is file name and rest are additional arguments passed.

text = "# This is not a comment because it's inside quotes."
print(text)

print("\nSome math:")
print("17/3 = ", 17/3)
print("classic division returns float")
print("power: ", 5**2)

print("\nEscape chars:")
print("doesn\'t")
print('C:\some\\name')


#string literals, no need of escaping with \
print("\nString Literals:")
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


#concatenation
print("\nString concatenation:")
print("un"*3 + "rahil\n")


#python indexing
print("Python indexing:")
print("""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
	""")

#Python strings
print("\nPython strings:\nPython strings are immutable but indexable!")
s = 'supercalifragilisticexpialidocious'
print(s[4:15], s[-9:-2], s[::-1],s[-1:-7:-1] , sep="\n")
print("Length of string is, ", len(s))

#Python Lists
squares = [1,4,9,16,25]
print(squares[:]) #prints whole string
print(squares + [36, 49, 64, 81, 100])
squares.append(121)
squares[1:3] = [2,3]
print(squares)


print("Fibonacci numbers")
a,b = 0,1
while a<10:
	print(a, end=",")
	a,b = b, a+b

# Notes
# In Python, everything UTF-8 encoded, although the standard library only uses ASCII characters for identifiers