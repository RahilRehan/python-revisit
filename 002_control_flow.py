print("First - If else\n")
x = int(input("Enter a number: "))
if x<0:
	x=0
	print("Negative number changed to 0")
elif x==0:
	print("Zero")
elif x == 1:
    print('Single')
else:
    print('More')

print("\nSecond - in keyword\n")
words = ['cat', 'window', 'defenestrate']
for w in words:
	print(w, len(w))

print("\nThird - Range keyword\n")
for i in range(5,10):  #range(inclusive, exclusive)
	print(i)

print("\nFourth - sum(range(x,y)), list(range(x,y))\n")
print(sum(range(1,5)))
print(list(range(4,9)))

print("\nPrime Programs\n")
for i in range(10):
	for j in range(2,i):
		if i%j==0:
			break
	else:    #wtf, else can be used without an if!! as "loop fell through"
		print(i, " is a prime number")

