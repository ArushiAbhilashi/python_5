#!/usr/bin/env python
# coding: utf-8

# # Question 1 :
# [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
# Sort by increasing order but all zeros should be at the right hand side.
# 

# In[6]:


list1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
maximum=max(list1)
def funckey(num):
    if num==0:
        return(maximum+1)
    else:
        return(num)
list1.sort(key=funckey)
print(list1)


# # Question 2 :
# list1=[10,20,40,60,70,80] sorted list
# list2=[5,15,25,35,45,60] sorted list
# Merge these two sorted lists to produce one sorted list, but use only loop either while or for only one time.

# In[14]:


lista=[10,20,40,60,70,80]
listb=[5,15,25,35,45,60]
listc=[]
index1=0
index2=0
while index1<len(lista) and index2<len(listb):
    if lista[index1]<listb[index2]:
        listc.append(lista[index1])
        index1+=1
    elif lista[index1]>listb[index2]:
        listc.append(listb[index2])
        index2+=1
    else:
        listc.append(lista[index1])
        listc.append(listb[index2])
        index1+=1
        index2+=1
if index1 !=len(lista):
    listc+=lista[index1:]
else:
    listc+=lista[index2:]
    
print(listc)


# In[8]:





# In[ ]:





# In[ ]:




