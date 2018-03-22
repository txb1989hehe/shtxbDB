#encoding: utf-8
'''
#w為寫入，r為讀取，a為寫入并保存之前的資料，rb讀取二進制，圖片，視頻等文件
file=open('/PYTHON APP/testfile.txt','w+')  
file.write('luke_tang')  #文件內寫入資料
#print(file.read())  #讀取文件資料
file.close() #關閉文件
'''
# ==> 等同如下
#with open('/PYTHON APP/testfile.txt','a') as file:
#    file.write('luke'+'\n')
  
#with open(r'D:\WORK\JEDI程式\FAEREGION_JDEI\FAERegion_JEDI.exe.config','r',encoding='gbk') as file: #encoding設定gbk為讀取非UTF-8的文劍
'''
with open(r'D:\WORK\JEDI程式\FAEREGION_JDEI\FAERegion_JEDI.exe.config','rb') as file: 
    for line in file.readlines():
        print(line.strip())  #strip()去掉\n回車


#操作文件和目錄
import os

print(os.name) #獲取操作系統名稱
print(os.environ)  #獲取系統環境變量
#可用get()函數獲取具體值
print(os.environ.get('PATH'))
print(os.environ.get('x','default')) #沒有參數x，則返回default
'''
'''
#os.path
print(os.path.abspath('.'))  #查看目錄絕對路徑 E:\PYTHON APP
route=os.path.join('E:\PYTHON APP','controlfile') #新目錄完整路徑 
print(route) #E:\PYTHON APP\controlfile
#os.mkdir(route) #創建目錄
os.rmdir(route) #刪除目錄

os.rename('test.txt','test.py')#重命名
os.remove('test.py')#刪除文件
import shutil
shutil.copyfile() #複製文件

print([x for x in os.listdir('E:\PYTHON APP') if os.path.isdir(x)]) #查出目錄下的子目錄
print([x for x in os.listdir('E:\PYTHON APP') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']) #查出所有.py的文件
'''
#序列化（pickling） 只局限於python本身，不能跨版本，跨編程語音
'''
import pickle
info=dict(name='luke',age=30,score=88)
print(pickle.dumps(info)) #dumps()把任何對象轉成bytes
#with open('/PYTHON APP/testfile.txt','ab') as file:  #以bytes方式存入文件
#    pickle.dump(info,file)
with open('/PYTHON APP/testfile.txt','rb') as file:  #讀取還原
    bfile=pickle.load(file)
    print(bfile)
'''
#json函数
#dict式序列化
import json
d=dict(name='luke',age=30,score=88)
newdict=json.dumps(d) #變為可存儲對象
print(json.loads(newdict)) #{'name': 'luke', 'age': 30, 'score': 88}

#class式序列化
class Student(object):
      def __init__(self,name,age,score):
            self.name=name
            self.age=age
            self.score=score

def student2dict(std):
      return {
            'name':std.name,
            'age':std.age,
            'score':std.score
            }
def dict2student(d):
      return Student(d['name'],d['age'],d['score'])
s=Student('luke',30,88)
print(json.dumps(s,default=student2dict)) #{'name': 'luke', 'age': 30, 'score': 88}
#等同如下： 一般任何class都有對應的__dict__屬性
#print(json.dumps(s,default=lambda obj:obj.__dict__))
#json_str="{'name': 'luke', 'age': 30, 'score': 88}"
#print(json.loads(json_str,object_hook=dict2student)) #有問題？

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
t=json.loads(s)
print(t)
