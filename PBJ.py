bread = 7
jelly = 4
pb = 4

if bread>=2 and jelly>=1 and pb>=1:
	print "You can have lunch today"
else: 
		print "No sandwich for you"
		
if bread>=2 and jelly>=1 and pb>=1:
	sandwich=bread/2
	if pb<sandwich:
		sandwich = pb
	if jelly<sandwich:
		sandwich = jelly
		
print sandwich

print "I can make {0} sandwiches".format(sandwich)

bread2 = bread - (2*sandwich)
pb2 = pb - sandwich
jelly2 = jelly - sandwich
print "I have {0} slices of bread, {1} servings of PB, and {2} servings of jam".format(bread2, pb2, jelly2)

if bread2>=0 and pb2>=0 and jelly >=0:
	of=bread
	if pb2<of:
		of = pb2
	if jelly2<of:
		of = jelly2
		
if of==0:
	print "No open-faced sandwiches for you."
else:
	print "You can have {0} open-faced sandwiches".format(of)

if jelly==0:
	print "You need more jam."
if pb==0:
	print "You need more peanut butter."
if bread==0:
	print "You need more bread."
else: 
	print "You're all set."

if bread>=0 and pb>=0 and jelly==0:
	print "You can make a peanut butter sandwich."

