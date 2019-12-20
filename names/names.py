import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1: # O(n)
#     for name_2 in names_2: # O(n)
#         if name_1 == name_2: # O(1)
#             duplicates.append(name_1) # O(1)

names_2_tree = BinarySearchTree(names_2[0]) # O(1)

# Put all the names in a search tree
for name in names_2[1:]: # O(n)
    names_2_tree.insert(name) # O(1)

# Check the tree for each name in names_1
for name in names_1: # O(n)
    if names_2_tree.contains(name): # O(logn)
        duplicates.append(name) # O(1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

"""
The Nested For Loops are what really kills the runtime of this program.
The runtime of the nested for loops is O(n^2) as shown below.

NESTED FOR LOOPS:

O(n):
    O(n):
        O(1):
            O(1):

***
O(n^2)
***

By implementing a binary search tree, we can cut the runtime from ~4.00s
to ~0.07s. The binary search tree reduces the runtime complexity from O(n^2)
to O(n + n*log(n)).

BINARY SEARCH TREE:

O(1)

O(n):
    O(1):

O(n):
    O(log(n)):
        O(1)

***

O(1)

O(n)

O(n*log(n))

***
O(n + n*log(n))
***
"""

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
