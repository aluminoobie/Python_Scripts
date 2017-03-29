#Author:  Peter Di Giorgio
#Date: 15032017
#Version: 1.1
#Purpose: Randomly generate a row number for people registered for a
#conference.

import random

winners = set()

#Read stdin for registration pool
pool_name = input('Enter the name of this registration pool: ')
#Read stdin of number of registered people
registered = input('Enter number of people registered: ')

#Read stdin of number of seats available
seats = input('Enter number of seats available: ')

#For loop of seats.  Print the random number in the range of registered.
print ('\nLottery for ' + pool_name + '\n')
for seat in range(0,int(seats)):
	number = random.randrange(1,int(registered))
	while number in winners:
		number = random.randrange(1,int(registered))
	winners.add(number)

print (list(winners))
	
print ('\n')	
input('Press Enter to end.')