class Time ():
    def print_time (time):

        print("%.2d:%.2d:%.2d" % (time.hour, time.minute , time.second) ) 

start = Time ()
start.hour = 9
start.minute = 30
start.second = 15

Time.print_time(start)
start.print_time()

class Time ():
 def __init__(self, hour = 0, minute= 0, second = 0):
     self.hour = hour 
     self.minute = minute 
     self.second = second 
 def __str__(self):
     return "%.2d:%.2d: %.2d" % (self.hour,self.minute,self.second)




class Time ():
 def __init__ (self, x = 0, y = 0):
     self.x = x
     self.y = y
 def __str__(self):
     return "%.1g,%.1g" % (self.x,self.y)    

