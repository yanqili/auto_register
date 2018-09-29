
# coding: utf-8

# In[1]:


from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
m = PyMouse()


# In[2]:


m.click(220,700,1)
time.sleep(2)
m.click(150,80,1)
time.sleep(3)
m.click(600,430,1)
time.sleep(3)
m.click(420,140,1)
time.sleep(3)
m.click(300,200,1)

