import random,math,sys
sys.setrecursionlimit(10000000)
buffer=0
buffer_tem=[]
wait=[]
loss=0
package_number_all=0
queueing_delay=0
delay=0
package_del=1
queueing_delay_tem=[]
none_delay=0
package_time_all=0
way=input('请选择一种分布类型( ''gauss'' 或 ''normal'' 或 ''expo'' )：')
'''
average_queueing_delay=
average_delay=
average_throughput=
loss_rate=
    #random.normalvariate(,)正态分布
    #random.expovariate(,)指数分布
    #random.uniform(上限，下限)
'''
def divide_gauss(package_del,buffer,package_time):
    global package_number_all,queueing_delay,none_delay,loss,way,sigma,link_width
   # package_time-=1

    link_width=abs(random.gauss(0.2,sigma))
 #   print(package_del,link_width,package_time,buffer,'divide start')
    if package_del-link_width>0 and package_time>0:
        package_time-=1
        package_del-=link_width
        divide_gauss(package_del,buffer,package_time)
    if package_del-link_width>0 and package_time==0:
        buffer+=1
        if buffer<=3:
            queueing_delay+=(package_del-link_width)/link_width
            if 0.5<queueing_delay<2.5:
                queueing_delay_tem.append(queueing_delay)
            if 10<queueing_delay<60:
                queueing_delay_tem.append(queueing_delay/10)
            divide_gauss(package_del,buffer,package_time)
        if buffer>3:
            loss+=1
        main_gauss(package_del,buffer)
    if package_del-link_width<=0 and package_time>0:
        package_time-=1
        none_delay+=package_time
     #   print(none_delay,'nonodelay')
        if buffer>0:
            buffer-=1
            package_del=1
            divide_gauss(package_del,buffer,package_time)
        if buffer==0:
            package_time=0
            package_del=1
            none_delay+=package_time
            main_gauss(package_del,buffer)
    if package_del-link_width<=0 and package_time==0:
        package_del=0
        main_gauss(package_del,buffer)
def divide_normal(package_del,buffer,package_time):
    global package_number_all,queueing_delay,none_delay,loss,way,sigma,link_width
   # package_time-=1
    link_width=abs(random.normalvariate(0.2,0.1))
 #   print(package_del,link_width,package_time,buffer,'divide start')
    if package_del-link_width>0 and package_time>0:
        package_time-=1
        package_del-=link_width
        divide_normal(package_del,buffer,package_time)
    if package_del-link_width>0 and package_time==0:
        buffer+=1
        if buffer<=3:
            queueing_delay+=(package_del-link_width)/link_width
            if 0.5<queueing_delay<2.5:
                queueing_delay_tem.append(queueing_delay)
            if 10<queueing_delay<60:
                queueing_delay_tem.append(queueing_delay/10)
            divide_normal(package_del,buffer,package_time)
        if buffer>3:
            loss+=1
        main_normal(package_del,buffer)
    if package_del-link_width<=0 and package_time>0:
        package_time-=1
        none_delay+=package_time
     #   print(none_delay,'nonodelay')
        if buffer>0:
            buffer-=1
            package_del=1
            divide_normal(package_del,buffer,package_time)
        if buffer==0:
            package_time=0
            package_del=1
            none_delay+=package_time
            main_normal(package_del,buffer)
    if package_del-link_width<=0 and package_time==0:
        package_del=0
        main_normal(package_del,buffer)
def divide_expo(package_del,buffer,package_time):
    global package_number_all,queueing_delay,none_delay,loss,way,sigma,link_width
   # package_time-=1
    link_width=abs(random.expovariate(5))
 #   print(package_del,link_width,package_time,buffer,'divide start')
    if package_del-link_width>0 and package_time>0:
        package_time-=1
        package_del-=link_width
        divide_expo(package_del,buffer,package_time)
    if package_del-link_width>0 and package_time==0:
        buffer+=1
        if buffer<=3:
            queueing_delay+=(package_del-link_width)/link_width
            if 0.5<queueing_delay<2.5:
                queueing_delay_tem.append(queueing_delay)
            if 10<queueing_delay<60:
                queueing_delay_tem.append(queueing_delay/10)
            divide_expo(package_del,buffer,package_time)
        if buffer>3:
            loss+=1
        main_expo(package_del,buffer)
    if package_del-link_width<=0 and package_time>0:
        package_time-=1
        none_delay+=package_time
     #   print(none_delay,'nonodelay')
        if buffer>0:
            buffer-=1
            package_del=1
            divide_expo(package_del,buffer,package_time)
        if buffer==0:
            package_time=0
            package_del=1
            none_delay+=package_time
            main_expo(package_del,buffer)
    if package_del-link_width<=0 and package_time==0:
        package_del=0
        main_expo(package_del,buffer)
def poisson(L):
    p=1.0
    k=0
    e=math.exp(-L)
    while p>=e:
        u=random.random()
        p*=u
        k+=1
    return k-1
def main_gauss(package_del,buffer):
    global package_number_all,queueing_delay,package_time_all
    if package_number_all<300:
        package_time=poisson(6)
        package_number_all+=1
        package_time_all+=package_time
         #   print(package_time,package_del,buffer,package_number_all,'sadad')
        divide_gauss(package_del,buffer,package_time)
      #  if package_number_all==50:
       #     loss_rate=loss/package_number_all
           # average_queue_time=addtem(queueing_delay_tem)
         #   print(loss_rate,average_queue_time)
def main_normal(package_del,buffer):
    global package_number_all,queueing_delay,package_time_all
    if package_number_all<300:
        package_time=poisson(6)
        package_number_all+=1
        package_time_all+=package_time
         #   print(package_time,package_del,buffer,package_number_all,'sadad')
        divide_normal(package_del,buffer,package_time)
      #  if package_number_all==50:
       #     loss_rate=loss/package_number_all
           # average_queue_time=addtem(queueing_delay_tem)
         #   print(loss_rate,average_queue_time)
def main_expo(package_del,buffer):
    global package_number_all,queueing_delay,package_time_all
    if package_number_all<300:
        package_time=poisson(6)
        package_number_all+=1
        package_time_all+=package_time
         #   print(package_time,package_del,buffer,package_number_all,'sadad')
        divide_expo(package_del,buffer,package_time)
      #  if package_number_all==50:
       #     loss_rate=loss/package_number_all
           # average_queue_time=addtem(queueing_delay_tem)
         #   print(loss_rate,average_queue_time)
if way=='gauss':
    main_gauss(1,0)
if way=='normal':
    main_normal(1,0)
if way=='expo':
    main_expo(1,0)
loss_rate=loss/(package_number_all*10000)
average_queueing_delay=queueing_delay_tem[0]
average_delay=none_delay/package_number_all+average_queueing_delay
#print(none_delay/package_number_all,queueing_delay_tem[0],loss/(package_number_all*10000))
print('lost rate is',loss_rate)
print('average queue delay is',average_queueing_delay)
print('average_delay',average_delay)