"""
str="pythonkn"
#iterates through string
#add each charater to the dictionary
#increment the count if character is already present
#iterates through a dict to find count  greater thsn one
chars={}
for i in str:
    if i not in chars:
        chars[i]=1

    else:
        chars[i]+=1
duplicate=[]
for key,count in chars.items():
    if count>1:
        duplicate.append(key)

print(chars)
print(duplicate)



#get() method --it returns the value of key if the key is not found it returns default value only if we specify in the second argument
#ex get(key,0)--not found returns 0
#create empty list and dict
#traverse a string 
dic={}
li=[]
str2="pythonkuy"
for i in str2:
    dic[i]=dic.get(i,0)+1
for i,count in dic.items():
    if count>1:
        li.append(i)
print(li)
"""
#using set
str3="pythonuiui"
char=set()
for i in str3:
    if i in char:
        print(i)
    char.add(i)
#print(char)