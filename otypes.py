class _:
	import abc,pickle,inspect,re,math,unicodedata,os,sys
	from collections import Counter
	from typing import Iterable,Mapping,Optional,Type,TypeVar,Dict
	class ometa(abc.ABCMeta):
	    def __sub__(s,*_,**k):return o.__new__(s,*_,**k)
	    def __rsub__(s,*_,**k):return o.__new__(s,*_,**k)
	def ometais(i,t):return(isinstance(i,t)or issubclass(i,t))if _.inspect.isclass(i)else(isinstance(type(i),t)or issubclass(type(i),t))
	class otypesmeta(abc.ABCMeta):
	    def __sub__(cls,value):return cls(value)
	    def __rsub__(cls,value):return cls(value)
def oinput(*s,sep=' ',type=str,Error="'{}' is not valid",Exit=None,Exit_code=None):
    while 1:
        user_input=input(sep.join(str(i)for i in s))
        if user_input==Exit:return Exit_code
        try:return type(user_input)
        except(ValueError,TypeError):print(Error.format(user_input))
class ostr(metaclass=_.otypesmeta):
    T=_.TypeVar("T",bound="ostr")
    """Factory and abstract type for the concrete nested str subclass."""
    def __new__(cls:_.Type[T],*parts:object,sep:_.Optional[str]=" ")->"ostr.ostr":return getattr(cls,"ostr")((''if sep is None else sep).join(str(p)for p in(parts[0] if len(parts)==1 and isinstance(parts[0],(list,tuple))else parts)))
    class ostr(str):
        """Concrete str subclass created by the factory."""
        __name__=__qualname__="ostr";__slots__=()
        def __new__(cls,value:object=''):return super().__new__(cls,str(value))
        def __invert__(self):return self
        def __neg__(self):return type(self)(self[::-1])
        def __add__(self,other:object):return type(self)(str.__add__(self,str(other)))
        def __radd__(self,other:object):return type(self)(str.__add__(str(other),self))
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
        def pipe(self,*functions):
            if len(functions)==0:return self
            s=self
            for f in functions[0]if len(functions)==1 and isinstance(functions[0],(list,tuple))else functions:s=f(s)
            return type(self)(s)
        def setitem(self,key,value):
            s=str(self)
            if isinstance(key,int):
                if key<0:key+=len(s)
                return type(self)(s[:key]+str(value)+s[key+1:])
            return type(self)(s)
        def __reduce__(self):return(ostr.ostr,(str(self),))
        def escape_aware_replace(s,old=None,new=''):
            if old is None:return s
            def repl(match):
                slashes=match.group(1)
                if len(slashes)%2==1:return slashes[:-1]+old
                else:return slashes+new
            return type(s)(_.re.compile(rf'(\\*){_.re.escape(old)}').sub(repl,s))
        def __gt__(self,o=None):
            """print... but worse..."""
            s=type(self)(self)
            if o is None:o={0:s}
            if isinstance(o,(list,tuple)):o={0:type(s)(' '.join(str(i)for i in o)).escape_aware_replace('%s',s)if len(o)>0 else s}
            elif isinstance(o,dict):
                o[0]=(type(s)(o[0]).escape_aware_replace('%s',s)if 0 in o else type(s)(o['self']).escape_aware_replace('%s',s)if'self'in o else s)
                if'pipe'in o:o[0]=o[0].pipe(o['pipe'])
            else:o={0:str(type(s)(o).escape_aware_replace('%s',s))}
            print(type(s)(o[0]),sep=o['sep']if'sep'in o else' ',end=o['end']if'end'in o else'\n',flush=o['flush']if'flush'in o else False,file=o['file']if'file'in o else _.sys.stdout)
            return self
        snake=property(lambda s:type(s)((lambda t:t if t not in{"con","prn","aux","nul"}else f"{t}_")(_.re.sub(r"_+","_",_.re.sub(r"[^\w]+","_",_.unicodedata.normalize("NFKD",str(s)).encode("ascii","ignore").decode().strip().lower()),).strip("_")[:255]or"unnamed")))
        def similarity(s,string):
            """Kinda sucks but tbh, Idc"""
            a,b=_.Counter(s),_.Counter(str(string))
            keys=set(a)|set(b)
            dot=sum(a[k]*b[k]for k in keys)
            na=_.math.sqrt(sum(v*v for v in a.values()))
            nb=_.math.sqrt(sum(v*v for v in b.values()))
            return dot/(na*nb)if na and nb else 0
        len,length,uwu=property(lambda*_:len(_[0])),property(lambda*_:_[0].len),(lambda s:type(s)(s.translate(str.maketrans('rlRL','wwWW'))+[' owo',' uwu',' <3',' :3'][hash(s)%4]))
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
    @staticmethod
    def methods():
        """Return dict of attribute name -> attribute for the concrete inner type."""
        return {name:value for name,value in _.inspect.getmembers(ostr.ostr)}
    method=staticmethod(lambda name=None,func=None,*,prop=False:(lambda f:(setattr(ostr.ostr,name or f.__name__,property(f)if prop else f)or f))if func is None else(setattr(ostr.ostr,name,property(func)if prop else func)))
    ostr._BIND_STR_METHODS()
    maketrans=staticmethod(lambda x,y=None,z='':str.maketrans(x,y,z))
ostr.register(ostr.ostr)
class o(metaclass=_.ometa):
    """automatically turn normal data-types into their otypes counterpart"""
    def __new__(cls,*args,**kwargs):
        if _.ometais(args[0],(str,ostr.ostr)):return ostr(*args,**kwargs)
        else:return args[0]
