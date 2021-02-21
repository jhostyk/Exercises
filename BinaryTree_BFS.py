#!/usr/bin/env python

'''
Given a binary tree, populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

~~ LeetCode https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/solution/
~~ 2020-12-6
~~ Joseph Hostyk
'''

###############################################################################

'''
Original solution:
	BFS. Go level by level. In each level, the adjacent nodes in the array
	are the ones that are the next right node in the tree.
Complexity:
	Runtime: O(N). Have to step through whole array.
	Space: O(1). Uses given array.
'''

###############################################################################

"""
# Definition for a Node.
class Node:
	def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
		self.val = val
		self.left = left
		self.right = right
		self.next = next
"""
class OriginalSolution:
	def connect(self, root: 'Node') -> 'Node':
		
		### Do BFS. Go through one level at a time.
		
		if root == None:
			return root
		currentLevel = [root]
		while(len(currentLevel) != 0):
			children = []
			for i, node in enumerate(currentLevel):
				if i == len(currentLevel) - 1: # right-most node.
					node.next = None
				else:
					node.next = currentLevel[i + 1]

				children.append(node.left)          
				children.append(node.right)  
			currentLevel = [node for node in children if node] # Get rid of the Nones.
		return root


###############################################################################

'''
Official solution.
Complexity:
	Runtime: O(N). Have to step through whole array.
	Space: O(1). Uses given array.
'''

###############################################################################

def officialSolution(flowerbed, numFlowers):
	'''
	Look in steps of three, but do it more concisely
	'''
	availableFlowerSpots = 0
	for i in range(len(flowerbed)):
		### First condition: Current flower is 0.
		### Second condition: Either we're at first spot, or previous spot is 0.
		### Third condition: Either we're at last spot, or next spot is 0.
		if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
			availableFlowerSpots += 1
			flowerbed[i] = 1		
		if availableFlowerSpots == numFlowers:
			return True
		print (flowerbed)
	return False		



if __name__ == '__main__':

	flowerbed = [1, 0, 0, 0, 1]
	numFlowers = 1
	print(officialSolution(flowerbed, numFlowers))


