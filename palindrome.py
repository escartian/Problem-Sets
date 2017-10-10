#By Igor Bich

#Project Euler Problem #4

#Finds the largest palindrome made from the product of two 3-digit numbers.
def isPalindrome(paly):
	test = list(str(paly))
	reverse = test[::-1]
	if reverse==test:
		return True
	else:
		return False


def check():
	a=999
	b=999
	palyList = []
	while a!=100:

		while b!=100:
			c=a*b
			b=b-1
			if isPalindrome(c):
				print("%d multiplied by %d gives us the palindrome: %d" %(a,b,c))
				palyList.append(c)
		a=a-1
		b=a	
	palyList.sort()
	print("*** The largest palindrome found was %d ***" % (palyList[-1]))

check()
