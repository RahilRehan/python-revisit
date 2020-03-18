tel = {"jack":4098, "sape":4139}
tel["guido"] = 4127

print(list(tel))  # prints all keys
print("guido" in tel) #checks for key presence, you can also use "not in"

# dict() constructor
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])	
print(d.keys())
print(d.values())
print(d)

# dictionary comprehension
d = {x: x**2 for x in (2, 4, 6)}
print(d)

#simple
print(dict(sape=4139, guido=4127, jack=4098))
