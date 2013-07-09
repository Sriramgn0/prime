class prime:
   def __init__(self):
	number=int(raw_input("enter number"))
	flag='prime number'
	for i in range(2,number/2+1):
	    if number%i==0:
		flag='not prime number'
	
	print flag

a=prime()



