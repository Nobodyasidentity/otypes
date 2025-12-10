Don't excpect quality from me :3
```py
from otypes import*

o('This hurts my eyes')>()
"Please send help"-o>'%s'

```  
## docs  
`@otype`: Custom data type creator. Takes a subclass and returns an `ometa` class.  
```py
# Example:
@otype
class MyInt(int):
  def MyFunc(self):
    return self * 2

x = o-10
print(type(x)) # <class '__main__.MyInt'>
print(x.MyFunc()) # 20
```  
`._BIND_METHODS(cls, source=None, wrap=None, dunder=False)`: (Experimental) Automatically makes all builtin methods of a subclass return the subclass instead of the super class.
```py
# Example:
@otype
class MyInt(int):pass

MyInt._BIND_METHODS(dunder=True)

x = o-10

print(type(x)) # <class '__main__.MyInt'>
print(type(x*2)) # <class '__main__.MyInt'>  
```
