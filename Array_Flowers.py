#!/usr/bin/env python

'''
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1
means not empty, and an integer n, return if n new flowers can be planted in the flowerbed
without violating the no-adjacent-flowers rule.

 ~~ LeetCode https://leetcode.com/problems/can-place-flowers/solution/
~~ 2020-12-6
~~ Joseph Hostyk
'''

###############################################################################

'''
Original solution: Step through. Lots of test cases to pass different options.
Complexity:
	Runtime: O(N). Have to step through whole array.
	Space: O(1). Uses given array.
'''

###############################################################################

def originalSolution(flowerbed, numFlowers):
	'''
	Look in steps of three.
	'''
	
	availableFlowerSpots = 0
	if flowerbed == [0]:
		availableFlowerSpots += 1
	if flowerbed[0:2] == [0, 0]:
		flowerbed[0] = 1
		availableFlowerSpots += 1
	if flowerbed[-2:] == [0, 0]:
		flowerbed[-1] = 1
		availableFlowerSpots += 1
	for i in range(2, len(flowerbed) - 1):

		setOfThree = flowerbed[i - 1 : i + 2]

		if setOfThree == [0, 0, 0]:

			availableFlowerSpots += 1
			flowerbed[i] = 1 
		if i == len(flowerbed) - 2 and flowerbed[-2:] == [0, 0]:# Last three spots
			availableFlowerSpots += 1
		if availableFlowerSpots == numFlowers:
			return True
	if availableFlowerSpots >= numFlowers:
			return True
	print (availableFlowerSpots)
	return False



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


