#內建模塊
#datetime
#定義一個運行的時間
'''
from datetime import datetime
import time
class Datetimetest(object):
    def nowtime(): #獲取系統時間
        now=datetime.now()
        return (now.ctime())
    def gettime(y,m,d,h,ms):  #手動獲取時間
        dt=datetime(y,m,d,h,ms)
        return dt

if __name__=='__main__':
    gett=Datetimetest.gettime(2015, 4, 19, 12, 20)
    print(gett)
#while True:
    time.sleep(1)
    print(Datetimetest.nowtime())
    print(Datetimetest.nowtime().split(' '))
'''
#collections(集合)
from collections import namedtuple  #namedtuple()可自定義tuple對象
point=namedtuple('point',['x','y']) #創建point為tuple的子類
p=point(1,2)
circle=namedtuple('circle',['x','y','r'])
c=circle(3,4,2)
print(c) #circle(x=3, y=4, r=2)

from collections import deque #deque()高效實習list插入和刪除
q=deque(['b','c','a'])
q.append('x')
q.appendleft('y')
print(q)  #deque(['y', 'b', 'c', 'a', 'x'])

from collections import defaultdict  #dict無KEY值輸出默認值
dd=defaultdict(lambda: 'N/A')
dd['k1']=123
print(dd['k2']) #N/A

from collections import OrderedDict  #是dict輸出變為有序輸出
d=dict([('a',1),('b',2),('c',3)])
print(d)  #{'a': 1, 'b': 2, 'c': 3}
od=OrderedDict(d)
print(od)  #OrderedDict([('a', 1), ('b', 2), ('c', 3)])

#Counter 計數
from collections import Counter
c=Counter()
for ch in 'asdgjkasfgawudga':
    c[ch]=c[ch]+1
print(c) #Counter({'a': 4, 'g': 3, 's': 2,...


#struct  任意數據類型轉換為字節
import struct
print(struct.pack('>I',123123123))  #b'\x07V\xb5\xb3'
#>代表字節順序 I代表4字節無符合整數
print(struct.unpack('>I',b'\x07V\xb5\xb3')) #(123123123,)
#具體定義參考：https://docs.python.org/3/library/struct.html#format-characters


