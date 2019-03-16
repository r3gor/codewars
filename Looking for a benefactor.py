def new_avg(arr, newavg):
    sum=0
    x=0
    for i in arr:
        sum+=i
    x=(newavg - (sum/(len(arr)+1)))*(len(arr)+1.0)

    print('----datos----')
    print('x= {}'.format(x))
    print('sum= {}'.format(sum))
    print('newavg= {}'.format(newavg))
    print('len(arr)= {}'.format(len(arr)))
    print('sum/(len(arr)+1) = {}'.format(sum/(len(arr)+1)))
    if x<0:
    	raise ValueError("Error expected")
    else:
    	return int(x)

if __name__=='__main__':

	# print(new_avg([1,2,3,44],100))

	print(new_avg([14, 30, 5, 7, 9, 11, 16], 90))

	print(new_avg([14, 30, 5, 7, 9, 11, 15], 92))