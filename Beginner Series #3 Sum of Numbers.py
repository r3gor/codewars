def get_sum(A,B):
    if A>B:
        b=A
        a=B
    if B>A:
        b=B
        a=A
    nums=[]
    suma=0
    for i in range(b-a+1):
        nums.append(a+i)
    for ii in range(len(nums)):
        suma+=nums[ii]
    return suma
if __name__ == '__main__':
	print(get_sum(0,-1))