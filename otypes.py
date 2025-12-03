class _:
	import abc,pickle,inspect,re,math,unicodedata,os
	from collections import Counter
	from typing import Iterable,Mapping,Optional,Type,TypeVar,Dict
def oinput(*s,sep=' ',type=str,Error="'{}' is not valid",Exit=None,Exit_code=None):
    while 1:
        user_input=input(sep.join(str(i)for i in s))
        if user_input==Exit:return Exit_code
        try:return type(user_input)
        except(ValueError,TypeError):print(Error.format(user_input))
class ostr(metaclass=_.abc.ABCMeta):
    T=_.TypeVar("T",bound="ostr")
    """Factory and abstract type for the concrete nested str subclass."""
    def __new__(cls:_.Type[T],*parts:object,sep:_.Optional[str]=" ")->"ostr.ostr":return getattr(cls,"ostr")((''if sep is None else sep).join(str(p)for p in(parts[0] if len(parts)==1 and isinstance(parts[0],(list,tuple))else parts)))
    class ostr(str):
        """Concrete str subclass created by the factory."""
        __name__=__qualname__="ostr";__slots__=()
        def __new__(cls,value:object):return super().__new__(cls,str(value))
        def __invert__(self):return super()
        def __neg__(self):return type(self)(self[::-1])
        def __add__(self,other:object):return type(self)(str.__add__(self,str(other)))
        def __radd__(self,other:object):return type(self)(str(other)+str(self))
        def __sub__(self,other:str):return type(self)(str(self).replace(str(other),""))
        def __mul__(self,n:int):return type(self)(str.__mul__(self,n))
        def __rmul__(self,n:int):return type(self)(str.__mul__(self,n))
        def __lshift__(self,n:int):
            s=str(self)
            if not s:return type(self)(s)
            n=int(n)%len(s)
            return type(self)(s[n:]+s[:n])
        def __rshift__(self,n:int):
            s=str(self)
            if not s:return type(self)(s)
            n=int(n)%len(s)
            return type(self)(s[-n:]+s[:-n])
        def append(self,*parts: object,sep:_.Optional[str]=" "):
            if len(parts)==1 and isinstance(parts[0],(list,tuple)):parts_iter=parts[0]
            else:parts_iter=parts
            if sep is None:sep=""
            tail=sep.join(str(p)for p in parts_iter)
            return type(self)(str(self)+tail)
        def cast(self,*types:_.Type):
            for t in types:
                try:return t(self)
                except Exception:continue
            return self
        def __floordiv__(self,replace_map:_.Mapping[str,str]):
            s=str(self)
            for old,new in replace_map.items():s=s.replace(old,new)
            return type(self)(s)
        def __getitem__(self,key):
            r=str.__getitem__(self,key)
            return type(self)(r) if isinstance(r,str)else r
        def __mod__(self,other):return type(self)(str.__mod__(self,other))
        def __rmod__(self,other):return type(self)(str.__rmod__(self,other))
        def join(self,it:_.Iterable[object]):return type(self)(str.join(self,(str(i)for i in it)))
        def format(self,*a,**k):return type(self)(str.format(self,*a,**k))
        def format_map(self,m:_.Mapping):return type(self)(str.format_map(self,m))
        def setitem(self,key,value):
            s=str(self)
            if isinstance(key,int):
                if key<0:key+=len(s)
                return type(self)(s[:key]+str(value)+s[key+1:])
            return type(self)(s)
        def __reduce__(self):return(ostr.ostr,(str(self),))
        snake=property(lambda s:type(s)((lambda t:t if t not in{"con","prn","aux","nul"}else f"{t}_")(_.re.sub(r"_+","_",_.re.sub(r"[^\w]+","_",_.unicodedata.normalize("NFKD",str(s)).encode("ascii","ignore").decode().strip().lower()),).strip("_")[:255]or"unnamed")))
        def similarity(s,string):
            """Kinda sucks but tbh, Idc"""
            a,b=_.Counter(s),_.Counter(str(string))
            keys=set(a)|set(b)
            dot=sum(a[k]*b[k]for k in keys)
            na=_.math.sqrt(sum(v*v for v in a.values()))
            nb=_.math.sqrt(sum(v*v for v in b.values()))
            return dot/(na*nb)if na and nb else 0
        _SAFE_SKIP={"__class__","__new__","__init__","__del__","__getattribute__","__getattr__","__setattr__","__delattr__","__dict__","__mro__","__subclasshook__","__init_subclass__","__weakref__","__slots__","__sizeof__","__reduce__","__reduce_ex__"}
        @classmethod
        def _BIND_STR_METHODS(cls):
            for name in dir(str):
                if name in cls._SAFE_SKIP:continue
                attr=getattr(str,name)
                if(not callable(attr))or(name in cls.__dict__):continue
                def make_wrapper(func):
                    def method(self,*a,**k):
                        r=func(self,*a,**k)
                        return cls(r)if isinstance(r,str)else r
                    return method
                setattr(cls,name,make_wrapper(attr))
    method=staticmethod(lambda name=None,func=None,*,prop=False:(lambda f:(setattr(ostr.ostr,name or f.__name__,property(f)if prop else f)or f))if func is None else(setattr(ostr.ostr,name,property(func)if prop else func)))
    ostr._BIND_STR_METHODS()

if __name__=='__main__':
	x=ostr('Hello', 'world')
	@ostr.method(prop=1)
	def reverse(self):return self[::-1]
	print(x,type(x))
	print(x.lower(),type(x.lower()))
	print(x*2,type(x*2))
	print(x.snake,type(x.snake))
	print(x.reverse,type(x.reverse))
