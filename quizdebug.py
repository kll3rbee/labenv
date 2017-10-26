# Let's go over another string method: string.replace. Use this method
# to replace the instance of NOUN with "duck" and VERB with "waddle" in the string
# sentence. For more information, visit http://www.tutorialspoint.com/python/string_replace.htm.

#sentence = "A NOUN went on a walk. They can VERB really well."
#sentence = sentence.replace("NOUN","duck")#fill this in
#s#entence = sentence.replace("VERB","waddle")#fill this in
#print sentence

# Define a procedure, square, that takes one number
# as its input, and returns the square of that
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

#def sum(a,b):
#    c = a + b
#   return c
#

#def sqr(a):
#   sq = a * a
#   return sq

# To test your procedure, uncomment the print
# statement below, by removing the hash mark (#)
# at the beginning of the line.

# Do not remove the # from in front of the line
# with the arrows (>>>). Lines which begin like
# this (#>>>) are included to show the results
# you should see when run your procedure.

#print square(5)
#>>> 25

#print sqr(4)
# print udacify('dacians')


#def udacify (a):
#    return 'U'+a[0:]




# Remove the hash, #, from infront of print to test your code.

#print udacify('dacians')
#>>> Udacians

#print udacify('turn')
#>>> Uturn

#print udacify('boat')
#>>> Uboat


#def biggest (a,b,c):
#    if a>=b:
#        if a>=c:
#           return a
#        else:
#        	return c
#    else:
#        if b>=c:
 #           return b
 #       else:
 #           return c




#print biggest(3, 6, 10)
#>>> 9

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9
# This code demonstrates a while loop with a "counting variable"
#i = 0
#while i < 10:
#    print i
#    i = i+1
# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?
#def remove_spaces(text):
#    text_without_spaces = '' #empty string for now
#    while text != '':
#        next_character = text[0]
#        if next_character != ' ':    #that's a single space
#            text_without_spaces = text_without_spaces + next_character
#        text = text[1:]
#    return text_without_spaces
#print remove_spaces("hello my name is andy how are you?")

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

#def print_numbers(a):
#	b=1
#	while b <= a:
#		print b
#		b+=1



#print_numbers(5)
#>>> 1
#>>> 2
#>>> 3

# A small change will fix the crashing bug in printInches.

def printExample(a, b):
    print a + b
    
def printInches(n):
    print str(n) + " inches"

# Don't change the function calls on lines 10 - 12.
printExample(17, 23)
printExample('long', 'word')
printInches(42)
