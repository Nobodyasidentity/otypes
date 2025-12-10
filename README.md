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
### `o` {
`o(*args, **kwargs)`: Auto-cast from a normal data type to the `otypes` equivalent.
```py
# Example
x = o("Hello")

print(type(x)) # <class 'otypes.ostr'>

print(type(o-"Hello")) # <class 'otypes.ostr'>
```  
`o.casting = dict({})`: A dict with the instructions on how `o()` should cast data types. Recommended to leave alone.  
  
`o.iscls(object ,class: class|tuple) -> bool`: Returns a boolean for if an object is the specified class or a subclass of the specified class.  
}  
`oinput(*s, sep=' ', type=str, Error="'{}' is not valid", Exit=None, Exit_code=None)`: Custom input method that lets you specify what data type to return the input as (default: `str`).  
### `ostr` {  
}
