#A Python program to compute factorial of a given number

num=int(raw_input("Enter a number"))
factorial=1
while num>0:
	factorial=factorial*num
	num=num-1
print "Factorial of the given number is ",factorial
