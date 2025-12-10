Don't excpect quality from me :3
```py
from otypes import*

o('This hurts my eyes')>()
"Please send help"-o>'%s'

```  
## docs  
`@otype`: Custom data type creator. takes a subclass and returns a `ometa` class.  
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
