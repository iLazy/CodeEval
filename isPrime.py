def isPrime(value):
	if value<=1:
		return False
	else:
		for i in xrange(2, value):
			if value%i==0:
				return False
			else:
				return True

if __name__=='__main__':
	if isPrime(929):
		print 'hello'
