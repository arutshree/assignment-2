#!/usr/bin/env python
# coding: utf-8

# In[1]:


sample_list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last_ele(n):
    return n[-1]

sorted_list=sorted(sample_list,key=last_ele)
print(sorted_list)


# In[ ]:




