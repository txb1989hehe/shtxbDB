#map函数
def a(x):
      return x*x
print(map(a,(i for i in range(10)))) #map函数生成的是Iterator对象 <map object at 0x01331B90>
print(list(map(a,(i for i in range(10))))) #加入list后生成Iterable对象
'''
Iterator对象为惰性序列 可调用next()函数
Iterrable对象有str，list，dict其他，for循环调用
用isinstance函数判断是Iterbable还是Iterator
'''
#reduce函数
from functools import reduce
def add(x,y):
      return x+y
print(reduce(add,(i for i in range(10)))) #reduce函数对序列的值进行向后累积
def add_x(x,y):
      return x*10+y
print(reduce(add_x,(j for j in range(10))))
check_str=reduce(add_x,(j for j in range(10)))
#import collections
print(isinstance(check_str,int))

#练习

def normalize(name):
      newname=name.title()
      return newname
namelist=['adam', 'LISA', 'barT']
print(list(map(normalize,namelist)))

#filter函数
def no_empty(s):
      return s and s.strip()
print(filter(no_empty,['a','',' ',None,12,'A']))#filter函数生成的是Iterator对象
#print(list(filter(no_empty,['a','',' ',None,12,'A'])))
#报错： 'int' object has no attribute 'strip'
#strip函数不支持int对象
print(list(filter(no_empty,list(map(str,(num for num in ['a','',' ',None,12,'A'] if num !=None))))))
#使用map函数将序列所以对象转换为str，排除None

#求素数
def odd_iter():
      n=1
      while True:
            n+=2
            yield n
def xx(a):
      return lambda x:x%a>0
def primes():
      yield 2
      num=odd_iter()
      while True:
            num1=next(num)
            yield num1
            num=filter(xx(num1),num)
list1=[]
for i in primes():
      if i<100:
            list1.append(i) 
      else:
            break
#print(list1)

#sorted函数
print(sorted(['zas','ASD','saw','Zasw','bwd'],key=str.lower,reverse=False))
#key可调用函数对value进行处理，reverse为True是倒序

def by_name(t):
      return sorted(t)
def listtodict(a):
      d={y:x for x,y in dict(a).items()}
      return tuple(d)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(by_name(L))
print(listtodict(L))

#返回函数 瞭解即可
def cal_sum(*args):
      def sum():
            s=0
            for n in args:
                  s=s+n
            return s
      return sum
a=cal_sum(1,2,3,46,5)
print(a)  #这里返回的不是SUM结果。而是求和函数 <function cal_sum.<locals>.sum at 0x02491660>
print(a()) #调用函数可得结果
