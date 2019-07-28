str='computer,it,entc,mech'
print(str)
print(str.replace('c','$'))

def remove(str1,n):
    first_part=str1[:n]
    last_part=str1[n+1:]
    return first_part + last_part

print(remove('python',2))
print(remove('python',5))

def anagram(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print('strings are anagram')
    else:
        print('strings are not anagram')

s1='listen'
print(sorted(s1))
s2='silent'
anagram(s1,s2)
