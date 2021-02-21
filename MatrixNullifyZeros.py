#!/usr/bin/env python

'''
For any zero in a matrix, turn its whole row and columns into zeros.
~~ Cracking the Coding Interview Strings chapter, problem 1.8
~~ 2021-21
~~ Joseph Hostyk
'''

def zerofyMatrix(matrix):
	"""
	Optimize for space.
	Args:
		matrix (list of lists): original matrix.
	Returns:
		matrix (list of lists): the nullified matrix.
	Run-time:
		O(m^2*n^2): O(m*n) to check every item in the matrix. Then constant time
		to change all the rows, but each column has to be changed one item at a time,
		so at worst if every column has a zero in it, then it would take O(m*n) to 
		zerofy each value.
	Space:
		O(1): Uses original matrix.
	"""

	### We track these separately because we're using the first row and column as
	### trackers for the rest of the matrix. So if there's a zero at [5,5], then
	### we change both [0,5] and [5,0] to zeros. Then if in our second pass if we
	### treated the first row/column the same as the others, we would see a zero in
	### the first row and set the whole row to zeros.
	### Instead, we just track if there was initially a zero in the first row/column.
	### In our second pass we check starting from the second row/column.
	### And then after that, if there was initially a zero in the first row/column,
	### at the end we can change that row/column to zero.
	numRows = len(matrix)
	numColumns = len(matrix[0])

	### First, check the first row/column.
	firstRowHasZero = False
	firstColumnHasZero = False
	for colNumber in range(numColumns):
		if matrix[0][colNumber] == 0:
			firstRowHasZero = True
			break
	for rowNumber in range(numRows):
		if matrix[rowNumber][0] == 0:
			firstColumnHasZero = True
			break

	### Next, mark which rows and columns have 0s.

	for rowNumber, row in enumerate(matrix):
		print (rowNumber, row)
		for colNumber, item in enumerate(row):
			print ("\t", colNumber, item)
			if item == 0:
				matrix[rowNumber][0] = 0
				matrix[0][colNumber] = 0
	print ("altered matrix:", matrix)
	### Then go through again and zerofy those rows/columns.

	### Rows:
	for rowNumber in range(1, numRows):
		if matrix[rowNumber][0] == 0:
			### Can just set the row directly:
			matrix[rowNumber][1:] = [0] * (numColumns - 1)
	# print (matrix)
	for colNumber in range(1, numColumns):
		if matrix[0][colNumber] == 0:
			### Can't slice list of lists
			for rowNumber in range(1, numRows):
				matrix[rowNumber][colNumber] = 0

	#### Do the first row/column:
	### Rows:
	if firstRowHasZero:
		matrix[0] = [0] * numColumns
	if firstColumnHasZero:
		for rowNumber in range(numRows):
			matrix[rowNumber][0] = 0	

	return matrix



if __name__ == '__main__':


	matrix = [[1,2,3],[4,0,6],[7,8,9]]
	assert (zerofyMatrix(matrix) == [[1,0,3],[0,0,0],[7,0,9]])

	matrix = [[0,2,3],[4,5,6],[7,8,9]]
	print (zerofyMatrix(matrix))





	

