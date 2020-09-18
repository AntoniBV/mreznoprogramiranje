import threading
import time

import datetime
from local_machine_info import print_machine_info

datum = datetime.datetime.now()
print(datum)
print_machine_info()

class myThread(threading.Thread):
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID =threadID
		self.name =name
		self.counter =counter
	
	def run(self):
		print "Pokrecem nit " + self.name
		
		threadLock.acquire()
		print_time(self.name,self.counter,3)
		
		threadLock.release()

def print_time(threadName,counter,delay):
	while counter:
		time.sleep(delay)
		print"%s: %s"%(threadName,time.ctime(time.time()))
		counter -=1

threadLock =threading.Lock()
threads =[]

thread1 =myThread(1,"Thread-1",1)
thread2 =myThread(2,"Thread-2",2)


thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
	t.join()
print"\nIzlazim iz glavne niti\n"