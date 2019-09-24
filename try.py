a= [1,2,3]
b = []
n=len(a)
for i in range(len(a)):
    if n == 1:
        b.append(a[i])
    else:
        xx = a[i]
        #print xx
        for j in range(len(a)):
            c = i+1+j
            if c < n:
                yy = xx+a[c]
                #print yy
            else:
                break
            b.append(yy)
print b
