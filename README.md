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
`._BIND_METHODS(source=None, wrap=None, dunder=False)`: (Experimental) Automatically makes all builtin methods of a subclass return the subclass instead of the super class.
> ```py
# Example:
@otype
class MyInt(int):
  pass

MyInt._BIND_METHODS(dunder=True)

x = o-10

print(type(x)) # <class '__main__.MyInt'>
print(type(x*2)) # <class '__main__.MyInt'>  
> ```
### class: `o` {
`o(*args, **kwargs)`: Auto-cast from a normal data type to the `otypes` equivalent.
```py
# Example
x = o("Hello")

print(type(x)) # <class 'otypes.ostr'>

print(type(o-"Hello")) # <class 'otypes.ostr'>
```  
`o.casting = dict({})`: A dict with the instructions on how `o()` should cast data types. Recommended to leave alone.  
  
`o.iscls(object ,class: class|tuple) -> bool`: Returns a boolean for if an object is the specified class or a subclass of the specified class. (Used by `o()` for auto-casting).  
```py
# Example
x = ostr("Hello")
print(o.iscls(x, ostr)) # True
print(o.iscls(x, int)) # False
```
> ###  class `attach` {
> `o.attach.method`: a property that returns a classmethod useful for letting users add their own functions to an `ometa` class
```py
 @otype
class myint(int):
    add_method = o.attach.method

@myint.add_method
def reverse(self):
    return -self

x=o-10
print(x.reverse())
```
> ### }
### }  
`oinput(*s, sep=' ', type=str, Error="'{}' is not valid", Exit=None, Exit_code=None)`: Custom input method that lets you specify what data type to return the input as (default: `str`).  
### `str` subclass: `ostr` {  
I'm too lazy to finnish this <3  
```py
from otypes import *

x = ostr("Hello World")

print(x) # "Hello World"
print(-x) # "dlroW olleH"
print(x+'!!!') # "Hello World!!!"
print(x-'l') # "Heo Word"
print(x*2) # "Hello WorldHello World"
print(x<<1) # "ello WorldH"
print(x>>1) # "dHello Worl"
print(type(x.cast(str))) # <class 'str'>
print(x[0]) # "H"
print(o("Hello %s")%"World") # "Hello World"
print(x//{'l':'w'}) # "Hewwo Worwd"
print(x.pipe(str.upper)) # "HELLO WORLD"
print(x.len, x.length) # 11 11
print(x.snake()) # "hello_world"
print(x.uwu()) # "Hewwo Wowwd"
print(~x) # <class 'otypes.ostr'>
print(x.escape_aware_replace('l','w')) # "Hewwo Worwd"
x>{0:"Message: %s"} # "Message: Hello World"
```
```py
@ostr.method
def indexof(self, item):
  return list(self).index(item)

x = o-"Hello"

@ostr.method
@property
def reverse(self):
  return -self

print(x.indexof('e')) # 1
print(x.reverse) # "olleH"
```
### }  
