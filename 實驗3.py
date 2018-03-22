#模塊(Module)
#標準格式

#encoding: utf-8
'模塊名稱'
__author='luke tang'


#可在環境變量中添加PYTHONPATH，與PATH設置類似
#讓PYTHON直接調用路徑下的py模塊

#類(Class)
'''
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def get_score(self):
        return ('%s: %s' %(self.name,self.score))
a=Student('peter',99)
b=Student('ailin',70)
print(a.get_score())
print(b.get_score())
print(Student('luke',100)) #指向Student的實例 <__main__.Student object at 0x0000021B2F52A320>

Student.name='luke'
print(Student.name)

print(Student) #指向Student這個類 <class '__main__.Student'>
'''

class Dataform(object):
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if 0<=gender<=100:
            self.__gender=gender
        else:
            raise ValueError('wrong gender')
    def print_gender(self):
        return ('%s 的分數 %s' %(self.__name,self.__gender))
a=input('請輸入姓名：')
b=int(input('請輸入成績：')) #輸入函數input
c=Dataform(a,b) # 類對象賦值c
#Dataform.get_name=a
#Dataform.get_gender=b
print(Dataform.print_gender(c)) #調用類內函數輸出類對象
print(Dataform.set_gender(c,b)) 

#類的繼承
#定義一個父類（超類，基類）
class Animal(object):  #定義CLASS首字母大寫
    def run(self):
        return 'runing...'
#再定義一個子類
class Dog(Animal):  #括號內的參數為父類class值，這樣子類就能調用父類所有的函數
    def run(self):  #當然子類也可以再定義同名的函數并調用（覆蓋父類的run函數）
        return 'dog is runing...' 
dog=Dog()
print(dog.run()) #runing...

# class本質就是定義一個類型，如list，tuple，dict
'''
import test3
a=test3.Animal()
isinstance(a,test3.Animal)
'''
#定義一個函數調用Animal類,該函數也可直接調用子類
def run_ticw(Animal):
    Animal.run()
#'開閉'原則:
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
