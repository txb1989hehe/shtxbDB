import random
import tkinter as tk
import tkinter.messagebox as messagebox

class Choicenum():
    total=0
    def __init__(self):
        self.main()       
    def randomnum(self):
        a=list(map(str,random.sample(range(10),4)))
        d=a[0]+a[1]+a[2]+a[3]
        return self.randomvar.set(d)
    def checknum(self):
        sinput=self.inputnumvar.get()
        try:
            iinput=int(sinput)
        except (ValueError,TypeError):
            messagebox._show('warning','請輸入正確的數！')
        if len(str(iinput))!=4:
            messagebox._show('warning','請輸入4位數！')
        
        return iinput
    def comparenum(self,getrannum,getnum):
        if getrannum != getnum:
            if getnum>getrannum:
                #print('da')
                return str(getnum) + '你猜的大了~'
                self.total+=1
            elif getnum<getrannum:
                #print('xiao')
                return str(getnum) + '你猜的小了~'
                self.total+=1
        else:
            return '恭喜',r'你猜對了！  '+str(getnum)
    def choosenum(self):
        self.checknum()
        get_rannum=int(self.randomvar.get())
        get_num=int(self.inputnumvar.get())
        messagebox._show('提示',self.comparenum(get_rannum,get_num))
        #print(self.comparenum(get_rannum,get_num))
        #self.infotext.insert(END,self.comparenum(get_rannum,get_num)+'\n')
    def reset(self):
        self.randomnum()
        self.inputnumvar.set('')
        
    def main(self):
        self.window=tk.Tk()
        self.window.title('隨機數猜測')
        self.window.geometry('300x200')
        self.titlelabel=tk.Label(self.window,bg='red',text='隨機數猜測').place(x=70,y=10)
        self.randomlabel=tk.Label(self.window,text='生成數').place(x=20,y=50)
        self.randomvar=tk.StringVar()
        self.randomentry=tk.Entry(self.window,textvariable=self.randomvar,show='*').place(x=70,y=50)

        self.inputnum=tk.Label(self.window,text='猜測數').place(x=20,y=90)
        self.inputnumvar=tk.StringVar()
        self.inputentry=tk.Entry(self.window,textvariable=self.inputnumvar).place(x=70,y=90)
        self.infotext=tk.Text(self.window,height=3,width=30).place(x=10,y=130)    
        self.choosebutton=tk.Button(self.window,text='CHOOSE',command=self.choosenum).place(x=220,y=85)
        self.resetbutton=tk.Button(self.window,text='RESET',command=self.reset).place(x=220,y=45)
        self.randomnum()
        self.window.mainloop()
        
if __name__=='__main__':
    Choicenum()
#print(a)
#print(d)
