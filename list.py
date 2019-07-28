from itertools import groupby
l=[10,20,30,90,15]
l1=[2,32,56]
print(max(l))


l.sort()
print(l)
print('second largest number is:' ,int(l[-2]))

k=[l for l in range(5) if l%2==0]
print(k)

l2=l+l1
print(l2.sort())
print('sorted list after addition is ',l2)

m=[l*l for l in range(len(l))]
print(m)


li=['mumbai','pune','nasik','nagar','hydrabad','Aurangabad']
print(li)
print (max(li,key=len))   #largest string
print('max string length is :',len(max(li,key=len)))     #length of max string


def swap(li):
    li[0],li[-1]=li[-1],li[0]
    li[2],li[3]=li[3],li[2]
    return li

print(swap(li))

list=[1,2,1,2,3,4,3]
print('original list is :',list)

res=[i[0] for i in groupby(list)]

print('list after removing duplicates :',res)




