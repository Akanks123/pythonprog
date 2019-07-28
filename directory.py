d={'name':'Akanksha','roll_no':'8'}
d1={'name':'Shweta','roll_no':'10'}
print(type(d))
print(d)

#d.update(d1)
#print('concatenated dictionary is :')
#print(d)

key=input('enter key to check :')
if key in d.keys():
    print('key is present in directionary and its value is:')
    print(d[key])
else:
    print('key is not present !')