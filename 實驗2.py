#匿名函數 lambda python針對匿名函數支持有限
#lambda x: x*x  ==>  def f(x): return x*x

#如上map函數改寫
print(list(map(lambda x : x*x ,(x for x in range(10) if x!=0))))

'''
lambda只能有一個表達式
lambda也是一個函數對象，為Iterator對象
'''
f=lambda x : x*x
print(f)  #<function <lambda> at 0x00000230406F1E18>
print(f(3)) # 9

#匿名函數也可做返回值返回
def  build(x,y):
    return lambda: x*x+y*y
print(build(2,3)) #<function build.<locals>.<lambda> at 0x00000208E98B7BF8>
print(build(2,3)()) # 13

#練習
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
# ==>
l = list(filter(lambda n : n%2==1,range(1,20)))
print(l)

#裝飾器（Decorator） 在不改變函數代碼的前提下，动态增加功能的方式
#函数对象有一个__name__属性，可以拿到函数的名字

#加個日誌
import functools
def log(func):
    @functools.wraps(func) #__name__屬性依舊依賴now
    def wrapper(**args):
        print('call: %s' %func.__name__)
        return func(**args)
    return wrapper

@log  #應用裝飾器（Decorator）用@語法  ==> now=log(now)
def now():
    print('123123123')
f=now
print(now()) #call: now  123123123  func.__name__拿到的是now函數
print(f()) #f與now等同
print(f.__name__) #f.__name__拿到的是wrapper函數 不加前面的@functools... 則為now

#若log函數本身需自定義參數'call'
'''
def log(text):
    def decorator(func):
        def wrapper(**args):
            print('%s: %s()' %(text,func.__name__))
            return func(**args)
        return wrapper
    return decorator
now=log('xxxx')(now)
'''



        
