listy=[]
for i in range(1, 1000000):
    listy.append(i)
listy.append(222)
#print(len(listy))
#this is part one of the assignment

#Part 2
#Scan here
def Scan(a):
    n=len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] ==a [j]:
                print(a[i], " and ", a[j])
                return
            else:
                continue

#Scan(listy)
#For some reason timeit wont work with this, so my manual timing was around 9 seconds

#Stor here
#To make it use less memory maybe have array b be empty at first then just amend the number to it, instead of having a full empty array

@profile
def Stor(a):
    n=len(a)
    b=[0]
    for i in range(n):
        if b[a[i]]==1:
            print("There is a duplicate at ", i)
            print(a[i])
            return
        else:
            b[a[i]]=1
            b.append(0)

Stor(listy)
#Time for this was pretty much instant