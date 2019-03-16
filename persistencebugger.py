def persistence(n):
    cont=0
    while n!=0 and 0<(10/n)<=1:
        cont+=1
        m=1
        for i in str(n):
            m*=int(i)
        n=m
    return cont
print(persistence(4126712))