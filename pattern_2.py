# Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.

# An N/2-dimensional forest is represented by the lower triangle of the pattern filled with ‘*’.

# For every value of ‘N’, help sam to print the corresponding N/2-dimensional forest.
# Example:

# Input:  ‘N’ = 3

# Output: 
# * 
# * *
# * * *

def nForest(n:int) ->None:
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()


nForest(3)