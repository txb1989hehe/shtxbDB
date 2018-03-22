#多進程win: multiprocessing; mac/unix: fork()
from multiprocessing import Process
from multiprocessing import Pool
import os,time,random
'''
def run_proc(name):
    print('run child process %s (%s)...' %(name,os.getpid()))
    
if __name__=='__main__':
    print('parent process %s.' %os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('child process will start.')
    p.start()  #啟動實例
    p.join()   #用于进程间的同步
    print('child process end.')
'''
#進程池（Pool）
def long_time_task(name):
    print('run task %s (%s)...' %(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('task %s run %0.2f seconds.' %(name,(end-start)))

if __name__=='__main__':
    print('parant process %s.'%os.getpid())
    p=Pool(10)
    for i in range(11):
        p.apply_async(long_time_task,args=(i,))
    print('waitting...')
    p.close() #調用close()後不能繼續添加process
    p.join()
    print('all done.')
