import _thread
import time

def print_time(threadName="Default", time=0):
   count = 0
   while count < 5:
      count += 1
      print("%s: %s" % (threadName, time.ctime(time.time())))
      time.sleep(15)


try:
   _thread.start_new_thread(print_time,())
   _thread.start_new_thread(print_time, ("Thread-2", 4, ))
except:
   print ("Error: unable to start thread")

while 1:
   pass