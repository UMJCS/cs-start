import random
buffer=0
buffer_tem=[]
wait=[]
loss=0
package_number_all=0
queueing_delay=0
delay=0
'''
average_queueing_delay=
average_delay=
average_throughput=
loss_rate=
    #random.normalvariate(,)正态分布
    #random.expovariate(,)指数分布
    #random.uniform(上限，下限)
'''
while package_number_all<=600:
    package_time=random.gauss(6,0.5)
    linkwidth=random.gauss(0.2,0.1)
    delunit=package_time*linkwidth
    if delunit<0:
        continue
    else:
        pass
    package_number_all+=1
    del_buffer_remain=1-delunit
    if del_buffer_remain>0:
        buffer+=1
    else:
        buffer-=1
    if buffer<=0:
        buffer=0
  #  print(buffer,package_number_all,'aaa')
    if 1<buffer<=3:
        queueing_delay+=package_time
    if buffer>3:
        loss_number=buffer-3
loss_rate=loss_number/package_number_all
print(loss_rate,'loss_rate')

#print(package,linkwidth,deltime)
