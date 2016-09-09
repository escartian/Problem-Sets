# Note: This finds all primes of the number 
# so it is not optimized for the Project Euler Problem #3

# prime factorization script 
# For fun, time it takes to calculate the prime factors
import time
start_time = time.time()

#The number we are finding the prime factors for
prime = 600851475143
#the list of first known prime numbers
primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,71,73,79,83,89,97]
#The list of prime factors (empty by default at start)
prime_factors=[]
#this is the main method
def primeFactorization(to_prime):
	i=0
	###print(primes)
	divisor=primes[i]
	while (to_prime) not in primes:
		if isDivisible(to_prime,divisor):
			to_prime=to_prime/divisor
			prime_factors.append(divisor)
			###print(to_prime)
		else:
			i=i+1
			###print("Index is", i)
			if i==len(primes):
				recordPrime()
			divisor=primes[i]
	prime_factors.append(to_prime)
	###print(primes)
	print(prime_factors)
	
def recordPrime():
	prime_calc = primes[len(primes)-1]+2
	while isPrime(prime_calc)==False:
		prime_calc = prime_calc+2
	primes.append(prime_calc)
	###print(prime_calc)


def isPrime(prime_finder):
	iter=0
	while prime_finder > primes[iter]**2:
		###print(prime_finder)
		if isDivisible(prime_finder, primes[iter]):
			return False
		iter=iter+1
		###print(iter)
	
	return True

def isDivisible(i,d):
	return i%d == 0
		
primeFactorization(prime)

#shows the time it took to calculate
print("--- %s seconds ---" % (time.time() - start_time))