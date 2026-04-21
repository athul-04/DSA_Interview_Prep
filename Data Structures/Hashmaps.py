arr=[1,1,2,3,3,3,4,5,5,5,5,5,6]

hashmap=dict()

for i in arr : hashmap[i]=hashmap.get(i,0)+1
print(hashmap)

#search for a value in the hashmap
hashmap.get(3,0) # returns the value of the key 3 if it exists, otherwise returns 0

# delete a key from the hashmap
del hashmap[3] # deletes the key 3 from the hashmap 

# Time complexity of hashmap operations
# Accessing an element by key: O(1) (average case), O(n) (worst case, when there are many collisions)
# Inserting an element: O(1) (average case), O(n) (worst case, when there are many collisions)
# Removing an element by key: O(1) (average case), O(n) (worst case, when there are many collisions)    
# Note: The worst-case time complexity can occur when many keys hash to the same index, leading to a collision. In practice, good hash functions and resizing strategies help mitigate this issue, keeping the average time complexity at O(1). 


#counter

from collections import Counter

counter=Counter(arr)
print(counter.most_common(3)) # returns the 3 most common elements in the array along with their counts
print(counter.get(2))
print(counter.elements()) # returns an iterator over the elements in the counter, repeating each element as many times as its count
print(counter.keys()) # returns a view of the keys in the counter
print(counter.values()) # returns a view of the counts in the counter   
print(counter.items()) # returns a view of the (key, count) pairs in the counter
print(counter.total()) # returns the total count of all elements in the counter