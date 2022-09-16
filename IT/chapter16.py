class Time (object):
    """ TAKE TIME  """

time = Time ()
time.hour = 11
time.minute = 39
time.second = 45

def print_time (time):
    print("%.2d:%.2d:%.2d" % (time.hour, time.minute , time.second) ) 

print_time(time)



def add_time(t1,t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    if sum.second >=60:
        sum.second -=60
        sum.minute +=1

    if sum.minute >=60:
        sum.minute -=60
        sum.hour +=1
    return sum 
    


start = Time ()
start.hour = 9
start.minute = 30
start.second = 15

duration = Time ()
duration.hour = 3
duration.minute= 45
duration.second = 40

final = add_time(start,duration)
print_time(final)