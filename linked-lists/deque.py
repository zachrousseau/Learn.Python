from collections import deque 


# Feed deque an iterable. 
print(deque(['a', 'b', 'c'])) # deque(['a', 'b', 'c'])
print(deque('abc')) # deque(['a', 'b', 'c'])
print(deque([{'data': 'a'}, {'data': 'b'}])) # deque([{'data': 'a'}, {'data': 'b'}])

# Right sides 
myfundeque = deque(['a', 'b', 'c']) 
myfundeque.pop() 
myfundeque.append('z')

print(f"myfundeque is {myfundeque}")

myfundeque.popleft() 
myfundeque.appendleft('z')

print(f"myfundeque is now {myfundeque}")