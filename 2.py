def max_rot(n):

	listn=list(str(n))

	for x in range(len(listn)):
		for i in range(len(listn)-1):
			if int(listn[i])<int(listn[i+1]):
				s=listn[i]
				listn[i]=listn[i+1]
				listn[i+1]=s
	num=0
	for ii in range(len(listn)):
		num = num + int(listn[ii])*10**(len(listn)-(ii+1))
	return num

if __name__=='__main__':
	print(max_rot(1133322244455588))