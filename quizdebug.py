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

def sqr(a):
    sq = a * a
    return sq

# To test your procedure, uncomment the print 
# statement below, by removing the hash mark (#) 
# at the beginning of the line.

# Do not remove the # from in front of the line 
# with the arrows (>>>). Lines which begin like 
# this (#>>>) are included to show the results
# you should see when run your procedure.

#print square(5)
#>>> 25

print sqr(4)