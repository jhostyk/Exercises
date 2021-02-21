#!/usr/bin/env python

'''
Given a binary search tree, rearrange the tree in in-order so that the leftmost node
in the tree is now the root of the tree, and every node has no left child and only one
right child
~~ LeetCode https://leetcode.com/problems/increasing-order-search-tree/solution/
~~ 2020-12-3
~~ Joseph Hostyk
'''

###############################################################################

### Set up.

###############################################################################

class ListNode(object):
	"""Sample ListNode"""
	def __init__(self, val):
		super(ListNode, self).__init__()
		

		self.val = val
		self.next = None

	def addToList(self, previousNode):

		previousNode.next = self

def makeLinkedList(array):

	head = ListNode(array.pop(0))
	current = head
	for value in array:

		L = ListNode(value)
		L.addToList(current)
		current = L
	return head

###############################################################################

'''
Original solution.
Go through tree, add onto new tree.
But, doesn't use anything about binary search tree to go through the original
tree in any smart way.
Complexity:
	Runtime: O(n)
	Space: O(n). Have to return a struct with all the original elements.
'''

###############################################################################

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        newRoot = TreeNode(val = root.val)
        firstTime = True
        toCheck = set([root])
        while bool(toCheck): # keeps running until set is empty
            
            ### Add nodes to our list to check.
            current = toCheck.pop()
            print("running on", current.val)
            if current.left:
                toCheck.add(current.left)
            if current.right:
                toCheck.add(current.right)
            
            newNode = TreeNode(current.val)
            ### Insert current node into our new tree.   
            if firstTime:
                firstTime = False
                continue
            ### If smaller than root, add to left:
            if current.val < newRoot.val:
                newNode.right = newRoot
                newRoot = newNode
            else:
                ### Find first node that's greater than the new node:
                comparedNode = newRoot
                while comparedNode.right and current.val > comparedNode.right.val:
                    comparedNode = comparedNode.right
                ### Add in our new node:
                newNode.right = comparedNode.right
                comparedNode.right = newNode            
        return newRoot
            
       
                
            
  
	

###############################################################################

'''
Official solution.
Go through in increasing order, so that can build the new tree right away.
Complexity:
	Runtime: O(N)
	Space: O(N)
'''

###############################################################################




		

if __name__ == '__main__':

	array = [i for i in range(3)]
	head = makeLinkedList(array)




