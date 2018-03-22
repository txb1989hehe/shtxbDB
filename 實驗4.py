#實例屬性與類屬性
class Student(object):
    count=0
    namelist=[]
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name

    

while True:  #統計人數
    Student.name=input('請輸入name: ')
    
    if Student.name in Student.namelist:
        print('已存在！請重新輸入')
        continue
        #raise ImportWarning('已存在！請重新輸入')
    else:
        Student.namelist.append(Student.name)
        Student.count+=1
        print(Student.name,Student.count,Student.namelist)
        #print(type(Student.name))
        #print(type(namelist[0]))

#錯誤分析
from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:
        
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except ValueError as e:
        print('valueerror:',e)
        
main()

#調試
#第一種方法： print()直接打印出錯誤信息
#第二種方法： assert斷言,不需要run assert語句時，開頭加上-0參數
'''
$python -0 err.py
assert n!=0 ,'n is zero!'
'''
#第三種方法（推薦）： logging，不報錯但輸出文件,有INFO,DEBUG,ERROR,WARNING四種方式
'''
import logging
logging.basicConfig(level=logging.INFO)
'''
#第四種方法： pdb調式器，進入pdb調試環境，命令p查看變量，命令c繼續運行
'''
import pdb
pdb.set_trace() #運行到此自動暫停，設置斷點
'''




    
    
