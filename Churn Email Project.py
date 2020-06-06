#!/usr/bin/env python
# coding: utf-8

# In[4]:


#count the no of lines
def number_of_lines():
    fhand = open('/cxldata/datasets/project/mbox-short.txt')
    inp = fhand.read()
    fhand.close()
    count = 0
    for c in inp:
        if c == '\n':
            count += 1
    return count


# In[5]:


#count the no of lines started with Subject
def count_number_of_lines():
    with open('/cxldata/datasets/project/mbox-short.txt') as f:
        count = 0
        for line in f:
            line = line.rstrip() # Remove new line characters from right
            if line.startswith('Subject:'):
                count = count + 1
    return count


# In[7]:


#Find Average Spam Confidence
def average_spam_confidence():
    with open('/cxldata/datasets/project/mbox-short.txt') as f:
        count = 0
        spam_confidence_sum = 0
        for line in f:
            line = line.rstrip() # Remove new line characters from right
            if line.startswith('X-DSPAM-Confidence:'):
                var, value = line.split(':')
                spam_confidence_sum = spam_confidence_sum + float(value)
                count = count + 1
    return spam_confidence_sum/count
    
    


# In[9]:


#Find Which Day of the Week the Email was sent
def find_email_sent_days():
    daysdict = {}
    dayslist = []

    with open("/cxldata/datasets/project/mbox-short.txt") as f:
      for line in f:
        dayslist = line.split()
        if len(dayslist) > 3 and line.startswith('From'):
            day = dayslist[2]
            if day not in daysdict:
                daysdict[day] = 1
            else:
                daysdict[day] += 1
    return daysdict


# In[10]:


#Count Number of Messages From Each Domain
def count_message_from_domain():
    lineslist=[]
    domaindict={}
    with open("/cxldata/datasets/project/mbox-short.txt") as f:
        for line in f:
            lineslist = line.split()
            if line.startswith('From:'):
                email=lineslist[1]
                domain = email.split('@')[1] 
                if domain not in domaindict:
                    domaindict[domain] = 1
                else:
                    domaindict[domain] += 1
    return domaindict


# In[ ]:




