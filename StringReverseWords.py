#!/usr/bin/env python

'''
Take in a string of words, return the words in reverse order.
~~ 2020-11-30
~~ Joseph Hostyk
'''

def reverseAstringForTime(string):
	"""
	Optimize for time.
	Args:
		string (str): the string to reverse.
	Returns:
		reversedString (str): the words in reverse order.
	Run-time:
		O(n): O(n) to split, O(n) to step through it backwards, O(n) to join with space.
	"""
	words = string.split()
	reversedString = []
	for index in range(len(words) - 1, -1, -1):
		lastWord = words[index]
		reversedString.append(lastWord)
	reversedString = " ".join(reversedString)
	return reversedString

def reverseAstringForSpace(string):
	"""
	Optimize for space.
	Given a mutable string, only ever use that array / some random variables.
	Args:
		string (str): the string to reverse.
	Returns:
		output (str): stdout
	Runtime:
		O(n) to reverse the string, O(n) to reverse the individual words.
	"""
	### Make it mutable for the sake of the problem:
	string = list(string)

	### First, reverse the full string, so even the letters read backwards:
	length = len(string)
	for i in range(int(length / 2)):
		temp = string[i]
		string[i] = string[length - i -1]
		string[length - i - 1] = temp
	### Now step through and reverse the individual words:
	wordStart = 0
	wordEnd = length
	### Step through until we get to a space / new word:
	for i in range(length + 1): # We go to + 1 so that we can check if we're at the end of the string.
		if i == length or string[i] == " ":
			wordEnd = i - 1
			### Reverse that word:
			halfWordLength = int((wordEnd - wordStart + 1)/2)
			for j in range(halfWordLength):
				temp = string[wordStart + j]
				string[wordStart + j] = string[wordEnd - j]
				string[wordEnd - j] = temp
			wordStart = i + 1

	return "".join(string)


def nickMahlanguAnswer(string):
	'''
	Optimize for time and minimal code.
	Same method as reverseAstringForSpace above, where we reverse the full string and then reverse individual words.
	'''
	return " ".join([word[::-1] for word in string[::-1].split()])




if __name__ == '__main__':


	string = "Here are five short words"

	assert (reverseAstringForTime(string) == "words short five are Here")

	assert (reverseAstringForSpace(string) == "words short five are Here")
	
	assert (nickMahlanguAnswer(string) == "words short five are Here")






	

