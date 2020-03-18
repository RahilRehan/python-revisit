#More on Lists

li = [5,9]
li.append(11)
li.extend([15,17])  #strips and add elements to list
li.remove(15) #removes first occurence of x
li.append(12)  #[5,9,11,17,12,13]
li.insert(0,2) #li.insert(index, element),  a.insert(len(a), x) ||ar to append
li.pop(2) #index is argument, Remove the item at the given position, if no index given then removes last element
# li.clear()  #Remove all items, doesnt deallocated
print(li.count(11))  #Return the number of times x appears in the list.
print(li)

def sortSecond(val):
    return val[1]

list1 = [(1, 2), (3, 3), (1, 1)] 
list1.sort(key=sortSecond, reverse=True)  #inplace
print(list1)

li.reverse()  #inplace
li2 = li.copy()  #shallow copy, i.e new reference

#Note
#[None, 'hello', 10] doesn’t sort as it is a composite data list
