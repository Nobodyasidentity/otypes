class _:
    import abc,pickle,inspect,re,math,unicodedata,os,sys
    from collections import Counter
    from functools import wraps
    SAFE={"__class__","__new__","__init__","__del__","__getattribute__","__getattr__","__setattr__","__delattr__","__dict__","__mro__","__subclasshook__","__init_subclass__","__weakref__","__slots__","__sizeof__","__reduce__","__reduce_ex__"}
    @classmethod
    def BIND(_,cls,*,source=None,wrap=None,dunder=False):
        if source is None:source=next((b for b in cls.__bases__ if b is not object),cls.__bases__[0])
        if wrap is None:wrap=(source,)
        mark=f"__bound_{source.__name__}__"
        if getattr(cls,mark,False):return cls
        for n in dir(source):
            if(not dunder and n.startswith("__"))or n in _.SAFE or n in cls.__dict__:continue
            try:
                raw=_.inspect.getattr_static(source,n)
                if isinstance(raw,(property,staticmethod,classmethod)):continue
                fn=getattr(source,n)
            except:continue
            if not callable(fn):continue
            def wrapfn(f,WT=wrap):
                @_.wraps(f)
                def m(self,*a,**k):
                    r=f(self,*a,**k)
                    return cls(r)if isinstance(r,WT)else r
                return m
            setattr(cls,n,wrapfn(fn))
        setattr(cls,mark,True)
        return cls
class ometa(type):
    def __new__(cls,*args,**kwargs):return super().__new__(cls,*args,**kwargs)
    __sub__=__rsub__=lambda c,v:c(v)
def otype(cls):
    ns=dict(cls.__dict__)
    ns.pop("__dict__",None)
    ns.pop("__weakref__",None)
    new=ometa(cls.__name__,cls.__bases__,ns)
    base=cls.__bases__[0]
    if "__new__" not in ns:
        def default_new(cls,*args,**kwargs):return super(cls,cls).__new__(cls,*args,**kwargs)
        new.__new__=default_new
    new._BIND_METHODS=classmethod(_.BIND)
    o.casting[base]=new
    return new
class o(metaclass=ometa):
    casting=dict({})
    def iscls(o,c):return(isinstance(o,c)or issubclass(type(o),c))
    def __new__(cls,*args,**kwargs):
        if len(args)<1:return None
        for i in cls.casting:
            if cls.iscls(args[0],(i,cls.casting[i])):return cls.casting[i](*args,**kwargs)
        return args[0]if len(args)==1 else args
def oinput(*s,sep=' ',type=str,Error="'{}' is not valid",Exit=None,Exit_code=None):
    while 1:
        user_input=input(sep.join(str(i)for i in s))
        if user_input==Exit:return Exit_code
        try:return type(user_input)
        except(ValueError,TypeError):print(Error.format(user_input))
@otype
class ostr(str,metaclass=ometa):
    def __new__(cls,*s,sep=' '):return str.__new__(cls,sep.join(str(a)for a in s))
    @classmethod
    def method(cls,f):
        if isinstance(f,property)or issubclass(type(f),property):name=f.fget.__name__
        elif isinstance(f,(classmethod,staticmethod))or issubclass(type(f),(classmethod,staticmethod)):name=f.__func__.__name__
        else:name=f.__name__
        setattr(cls,name,f);return f
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
    def cast(self,*types):
        for t in types:
            try:return t(self)
            except Exception:continue
        return self
    def __getitem__(self,key):r=str.__getitem__(self,key);return type(self)(r) if isinstance(r,str)else r
    def __mod__(self,other):return type(self)(str.__mod__(self,other))
    def __rmod__(self,other):return type(self)(str.__rmod__(self,other))
    def join(self,it):return type(self)(str.join(self,(str(i)for i in it)))
    def format(self,*a,**k):return type(self)(str.format(self,*a,**k))
    def format_map(self,m):return type(self)(str.format_map(self,m))
    def __floordiv__(self,replace_map):
        s=str(self)
        for old,new in replace_map.items():s=s.escape_aware_replace(old,new)
        return type(self)(s)
    def pipe(self,*functions):
        if len(functions)==0:return self
        s=type(self)(self)
        for f in functions[0]if len(functions)==1 and isinstance(functions[0],(list,tuple))else functions:s=f(s)
        return type(self)(s)
    def __reduce__(self):return(type(self),(str(self),))
    len=length=property(lambda*_:len(_[0]))
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
        print(type(s)(o[0]),sep=o['sep']if'sep'in o else' ',end=o['end']if'end'in o else'\n',flush=o['flush']if'flush'in o else False,file=o['file']if'file'in o else _.sys.stdout);return self
    snake,uwu=(lambda s:type(s)((lambda t:t if t not in{"con","prn","aux","nul"}else f"{t}_")(_.re.sub(r"_+","_",_.re.sub(r"[^\w]+","_",_.unicodedata.normalize("NFKD",str(s)).encode("ascii","ignore").decode().strip().lower()),).strip("_")[:255]or"unnamed"))),(lambda s:type(s)(s.translate(str.maketrans('rlRL','wwWW'))+[' owo',' uwu',' <3',' :3'][hash(s)%4]))
    def __invert__(s):return type(s)
ostr._BIND_METHODS(dunder=1)
