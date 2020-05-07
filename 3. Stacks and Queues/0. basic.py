"""
list.append(x)
  Add an item to the end of the list; equivalent to a[len(a):] = [x].

list.extend(L)
  Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.

list.insert(i, x)
  Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
  Remove the first item from the list whose value is x. It is an error if there is no such item.

list.pop([i])
  Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.index(x)
  Return the index in the list of the first item whose value is x. It is an error if there is no such item.

list.count(x)
  Return the number of times x appears in the list.

list.sort()
  Sort the items of the list, in place.

list.reverse()
  Reverse the elements of the list, in place.
"""

stack = list()

stack.append(1)
stack.append(2)
print(stack)

stack.append('a')
print(stack)

stack.insert(1, 'new')
print(stack)

print(stack.pop())

print(stack)

from collections import deque
queue = deque(['a', 'b', 'c'])
print(queue)

queue.append('me')
print(queue)

print(queue.popleft())
print(queue)