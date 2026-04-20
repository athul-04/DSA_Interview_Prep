# Arrays

import array as arr

a=arr("i",[1,2,3,4,5])
# add
a.append(6)
# adding elements to array
a.extend([7,8,9,10])
#pop is removing using the position - when no params passes it removed the last element and returns it
a.pop()
a.pop(0)
# insert(pos,value)
a.insert(0,0)
# remove value - removes the first occurrence of the value
a.remove(5)

# Time complexity of array operations
# Accessing an element by index: O(1)
# Appending an element: O(1) (amortized)
# Inserting an element at a specific position: O(n) (due to shifting elements)
# Removing an element by value: O(n) (due to searching for the value)


# Linked Lists


from collections import deque


linkedList=deque([1,2,3,4,5])
# add
linkedList.append(6)
# adding elements to linked list
linkedList.extend([7,8,9,10])
# pop is removing using the position - when no params passes it removed the last element and returns it
linkedList.pop()
linkedList.popleft()
# insert(pos,value) - not supported in deque, but we can achieve it by converting to list and back to deque
linkedList.insert(0,0)      
# remove value - removes the first occurrence of the value
linkedList.remove(5)
# Time complexity of linked list operations
# Accessing an element by index: O(n) (due to traversal)
# Appending an element: O(1)
# Inserting an element at a specific position: O(n) (due to traversal)
# Removing an element by value: O(n) (due to searching for the value)
# https://realpython.com/linked-lists-python/