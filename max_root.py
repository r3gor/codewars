def max_rot(n):

	listn=list(str(n))
	numeros=[]
	for x in range(len(listn)):

		s=listn[x]
		listn[x]=listn[x+1]
		listn[x+1]=s

	numeros.append(lambda: list2int(listn))
	return(numeros)

def list2int(a):	
	for ii in range(len(a)):
		num = num + int(a[ii])*10**(len(a)-(ii+1))



if __name__=='__main__':
	print(max_rot(12869))