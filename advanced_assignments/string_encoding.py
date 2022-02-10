'''
problem 
--------------------------------------
you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
--------------------------
Example
------------------------
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
''' 

def encode(text):
	d = {}
	alphabets = list('abcdefghijklmnopqrstuvwxyz')
	encodings = [i for i in range(1,len(alphabets)+1)]
	for i in range(len(alphabets)):
		d[alphabets[i]] = encodings[i]

	text = text.lower()
	encoded_list = [f'{d[i]}' for i in text if i.isalpha()]
	return( ' '.join(encoded_list))

print(encode('thomas12kut3,11ty'))

