# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

#def weekend(day):
##   if day=='Saturday' or day=='Sunday':
#    	return True
#    else:
#    	return False
    # your code here
    
#print weekend('Monday')
#>>> False

#print weekend('Saturday')
#>>> True

#print weekend('July')
#>>> False

########################
# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

'''def countdown(n):
	while n>0:
		print n
		n-=1
	print 'Blastoff!'





countdown(4)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff! '''

##############################
# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b
        
def smaller(a,b):
    if a < b:
        return a
    else:
        return b
        
def biggest(a,b,c):
    return bigger(a,bigger(b,c))
'''
def smallest(a,b,c):
	return smaller(a,smaller(b,c))

def median(a,b,c):
	if a != smallest(a,b,c) & a != biggest(a,b,c):
		return a
	else:
		if b != smallest(a,b,c) & b != biggest(a,b,c):
			return b
		else:
			return c

'''

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    if biggest(a,b,c) ==a:
        return bigger(b,c)
    if biggest(a,b,c) == b:
        return bigger(a,c)
    else :
        return bigger(a,b)

print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7
