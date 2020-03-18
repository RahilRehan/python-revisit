# A set is an unordered collection with no duplicate elements

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

#for empty set creation use set()

#fast membership test
print("apple" in basket)


a = set("abracadabra")
b = set('alacazam')

print(a - b)                              # letters in a but not in b
print(a | b)                              # letters in a or b or both, union
print(a & b)                              # letters in both a and b, intersection
print(a ^ b)                              # letters in a or b but not both, symmetric diff

#set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)