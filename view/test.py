import six

import Model.connection
class MyClass:
   def __init__(self,x):
           self.x = x




A, B = (MyClass('text') for x in range(2))
print(A)
print(B)
A.get()