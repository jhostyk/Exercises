#!/usr/bin/env python

'''
Return a random node from a linked list of unknown size.
~~ LeetCode https://leetcode.com/problems/linked-list-random-node/solution/
~~ 2020-12-2
~~ Joseph Hostyk
'''

import random


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
First, get the length of the list. (Didn't know how else to uniformly
random sample.)
Then select random node.
Complexity:
	Runtime: O(n)
	Space: O(1)
'''

###############################################################################

class OriginalSolution:

	def __init__(self, head: ListNode):
		"""
		@param head The linked list's head.
		Note that the head is guaranteed to be not null, so it contains at least one node.
		"""
		self.head = head
		
	def getLengthOfList(self):
		'''
		Step through the whole list to see how many total nodes there are.
		'''
		length = 1
		next = self.head.next
		while next:
			
			length +=1
			next = next.next
			
		self.length = length
		

	def getRandom(self) -> int:
		'''
		Returns a random node's value.
		'''
		self.getLengthOfList()
		randNodeNumber = random.randint(1, self.length)
		current = self.head
		print ("there are {} in list".format(self.length))
		for i in range(randNodeNumber - 1):
			current = current.next
		return current.val
	

###############################################################################

'''
Official solution.
Reservoir sampling: Keep a running list. (Here, just one node.)
With decreasing probability, replace that node.
To start, we select the first node.
When we get to the second, we swap it out with P = 1/2.
Meaning there's 50% chance we're still with the first node, and 50% we've kept
the second.
At the third, we swap it out with P = 1/3.
That means with P = 2/3, we keep our current node.
For the first node: we kept it at round 2 with P = 1/2, and independently keep it
at round 3 with P = 2/3, so after round 3, it is kept with P = 1/3.
Similarly for the second node.
Meaning all three nodes have 1/3 chance of being our final selection.
And this repeats for future rounds, as we stream and bring more nodes in.
Complexity:
	Runtime: O(N)
	Space: O(1)
'''

###############################################################################

class ReservoirSamplingSolution:

	def __init__(self, head: ListNode):
		self.head = head	

	def getRandom(self) -> int:
		"""
		Returns a random node's value.
		"""
		
		count = 1
		randomSelection = self.head # The node we'll return.
		current = self.head
		while current.next:
			current = current.next
			count += 1
			# With probability 1/count, swap out:
			if random.randint(1, count) == 1: 
				randomSelection =  current
		return randomSelection.val

		

if __name__ == '__main__':

	array = [i for i in range(3)]
	head = makeLinkedList(array)

	obj = OriginalSolution(head)
	randomNodeValue = obj.getRandom()
	print ("Original:", randomNodeValue)

	obj = ReservoirSamplingSolution(head)
	randomNodeValue = obj.getRandom()
	print ("Reservoir:", randomNodeValue)



