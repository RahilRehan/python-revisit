# Errors and Exceptions

# two distinguishable kinds of errors: syntax errors(code right!) and exceptions

# exceptions
# print(10 * (1/0))  #ZeroDivisionError: division by zero
# print(4 + spam*3)  #NameError: name 'spam' is not defined
# print('2' + 2)     #TypeError: Can't convert 'int' object to str implicitly

# 1st handler

while True:
	try:
		x = int(input("Enter number: "))
		print("input successful", x)
		break
	except ValueError:
		print("OOPs, not a number!")


# A try statement may have more than one except clause
# except (RuntimeError, TypeError, NameError):
#	pass


#else

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()


#example
def this_fails():
	x = 1/0

try:
	this_fails()
except ZeroDivisionError as e:
	print("Handle ", e)


#raising error, The raise statement allows the programmer to force a specified exception to occur.
# raise NameError("Hithere")

#example, raise
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    # raise #uncomment to raise manually


#cleanup using finally
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

