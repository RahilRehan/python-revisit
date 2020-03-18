# Using list as stack

stack = [3,4,5]

#push
stack.append(6)
stack.append(7)
print(stack)

#pop
ele = stack.pop()  #pop and store
print(ele)
stack.pop()

#view
print(stack[-1])

print(stack)
