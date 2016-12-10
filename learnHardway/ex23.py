i = 0
number = []

while i < 6:
	print "\n*************************************"

	print "At top i is : %r" % i
	number.append(i)

	i = i + 1

	print ">>>> Now number is: ", number
	print "At bottom i is : %r" %i
	print "\n*************************************"

print "\n The Numbers"

for num in number:
	print num