# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
	if year%400 == 0 or (year%4 == 0 and year%100 != 0):
		return 1
	else:
		return 0

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
	days = d2 #days in current month
	byrneg = d1
	ycnt = y2 - y1
	mcnt = m2 - m1
	if ycnt < 0: # if negative year
		days = 0
	elif ycnt == 0 and mcnt == 0: # if same year and month
		days = d2 - d1
		if  days < 0 :
			days = 0
		return days
	elif ycnt == 0: # if same year
		if mcnt < 0:
			days = 0
		elif mcnt == 1: # if one month old
			days += (daysOfMonths[m1 - 1] - d1) # for the birth nmonth
		else:
			for i in range(m1, m2-1):
				days += daysOfMonths[i]
			days += (daysOfMonths[m1 - 1] - d1) # for days in birth month
		return days
	elif ycnt == 1: # if a year old
		for i in range(m2-1):
			days += daysOfMonths[i] #days for the current year
		for i in range(m1-1):
			byrneg += daysOfMonths[i] # neg birth year days
		if isLeapYear(y1) == 1 and m1 < 3: # days for birth year
			days += (366 - byrneg)
		else:
			days += (365 - byrneg)
		return days
	elif ycnt > 1:
		for i in range(m2 - 1):
			days += daysOfMonths[i] #days for the current year
		for i in range(m1 - 1):
			byrneg += daysOfMonths[i] # neg birth year days
		if isLeapYear(y1) == 1 or m1 < 3: # days for birth year
			days += (366 - byrneg)
		else:
			days += (365 - byrneg)
		for i in range(y1+1, y2): #total days not including curent and first year
			if isLeapYear(i) == 1:
				days += 366
			else:
				days += 365
		return days
	else:
		days = 0 

#print daysBetweenDates (2013, 1, 24, 2013, 6, 29)
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed. Your answer:", result, "Should be:", answer
        else:
            print "Test case passed!"

test()