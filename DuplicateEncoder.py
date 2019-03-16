def duplicate_encode(word):
	cont=0
	rpta=''
	mword=word.lower()
	for i in mword:
		for ii in mword:
			if i == ii:
				cont+=1
		if cont>1:
			rpta+=')'
			cont=0
			
		elif cont<=1:
			rpta+='('
			cont=0
	return rpta

print(duplicate_encode('Success'))