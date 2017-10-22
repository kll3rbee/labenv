# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.


#def bigger (a,b):
#    if a > b:
 #       return a
 #   else:
#        return b



#print bigger(2,7)
#>>> 7

#print bigger(3,2)
#>>> 3

#print bigger(3,3)
#>>> 3


def is_friend (a):
    if a[0] == 'D':
        return True
    else:
        if a[0] == 'N':
            return True
        else:
            return False




print is_friend('Fiane')
#>>> True

#print is_friend('Fred')
#>>> False