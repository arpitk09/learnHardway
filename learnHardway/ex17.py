def break_words(stuff):
	"""This function will break words for us."""
	words = stuff.split(' ')
	return words


def sort_words(words):
	"""Sorts the words."""
	return sorted(words)


def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = word.pop(0)
	print word


def print_last_word(words):
	"""Print the last word after popping it  off."""
	word = words.pop(-1)
	print word


def sort_sentence(sentence):
	"""Takes in a full sentence and return the sorted words."""
	words = break_words(sentence)
	return sort_words(words)



def Print_first_and_last(sentence):
	"""Sorts the word then prints the first and last one."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
