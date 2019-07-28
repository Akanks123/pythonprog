s=set('mutex')
print(type(s))
print(s)

def vowel_count(str):
    count=0
    vowel=set('aeiouAEIOU')
for alphabet in str:
     if alphabet in vowel:
        count=count+1
print('no of vowels :',count)

str='mumbai'
vowel_count(str)