'''
print "###############################"
# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(mylist):
	sum = 0
	for element in mylist:
		sum+=element
	return sum

print sum_list([1, 7, 4])
#>>> 12

#print sum_list([9, 4, 10])
#>>> 23

#print sum_list([44, 14, 76])
#>>> 134

print "###############################"

# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.


def measure_udacity(namelist):
	usum = 0
	for a in namelist:
		if a[0] == 'U':
			usum += 1
	return usum

print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

#print measure_udacity(['Umika','Umberto'])
#>>> 2

print "###############################"
'''
# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.
'''
test if second element will match
def find_element (a,b):
	for c in a:
		if c == b:
			result = c
			return c
	return -1


def find_element (a,b):
	i = 0
	for c in a:
		if c == b:
			return i
		i += 1
	return -1

def find_element (p,t):
	i = 0
	while i < len (p):
		if p[i] == t:
			return i
		i += 1
	return -1
'''

def find_element (a,b):
    if b in a:
        return a.index(b)
    else:
        return -1

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')

print find_element(['alpha','beta','gago','gamma'],'gamma')
#>>> -1