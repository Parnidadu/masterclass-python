
# coding: utf-8

# In[3]:


class computers:
    
    def getspecs():
        name=input("enter the specification of laptops/computers");
    def displayspecs(name):
        print(name);
    
class laptop(computers):
    def displayspecs(del)
class desktop(computers):

dell=laptop();
wipro=desktop();
dell.getspecs()
dell.displayspecs();
wipro.getspecs();
wipro.displayspecs();


# In[8]:


import re
a=input("enter your name ")
pattern = r"mishra";
if re.search(pattern,a):
    print("you have a good family");
else:
    print("you have a poor family");


# In[15]:


name = input("enter any film name");
if re.findall(name,"sholay deewar thugs of hindustan"):
    print("you love amitabh banchann");
elif re.search(name,"raone swades happy new year"):
    print("you love shahrukh khan");
else:
    print("can't predict you superstar")


# In[18]:


#find and replace code
string=input("write a simple speech: ")
pattern = r"youth"
result = re.sub(pattern,"indian youth",string)
print(result)


# In[15]:


import re
pattern=r"hey"
file=open("try.txt",'r')
content=file.read()
print(content)
if re.match(pattern,content):
    print('match found')
file.close()
