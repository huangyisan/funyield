class D(object): pass
class E(object): pass
class F(object): pass
class B(D, E): pass
class C(D, F): pass
class A(B, C): pass
print(A.__mro__)


'''
查询关系
D --> D,object
E --> E,object
F --> F,object

B --> B, D, E, ...., object
C --> C, D, F, ...., object
A --> A. B, C, ...., object
  将B和C带入后得到
  --> A, (B, D, E, ..., object), (C,D,F, ..., object)
  B和C存在共同的父类，D，所以B和C是同一级别，查询顺序是A, B, C, 然后D,
  --> A, B, C, D (E, ..., object), (F, ..., object) 
  查询完了全部则查询object
  --> A, B, C, D, E, F, object
'''


class g(object): pass
class f(object): pass
class h(object): pass
class i(object): pass
class e(object): pass
class d(h,i): pass
class b(d,e): pass
class c(f,g): pass
class a(b,c): pass
print(a.__mro__)

'''
查询关系：
g --> g, object
f --> f, object
h --> h, object
i --> i, object
e --> e, object

b --> b, d, e, ..., object
c --> c, f, g, ..., object
d --> d, h, i, ..., object

a --> a, b, c, ..., object
  将B和C带入后得到
  --> a, (b, d, e, ..., object), (c, f, g, ..., object)
  将b带入后得到
  --> a, (b, (d, h, i, ..., object), e, ..., object), (c, f, g, ..., object)
  b和c没有共同的父类，所以直接查询了d，d后，查询他的继承，h，因为h最顶了，所以开始依次返回，查询其平级的i，然后折回到b中右边的e,然后再次返回到a中右边的c，然后查询c中的f,发现到顶了，则查询其平级的g，然后依次退出，发现直接查询完了全部，则查询object
'''

