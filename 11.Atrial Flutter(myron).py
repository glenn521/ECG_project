import numpy as np
import math
import matplotlib.pyplot as plt

#pwav
def p_wav(x,a_pwav,d_pwav,t_pwav,li):
    l=li
    a=a_pwav

    for i in range(len(x)):
        x[i]=x[i]+t_pwav

    b=(2*l)/d_pwav
    n=100
    p1=(a/(2*b)*(2-b))

    p2=np.zeros(len(x))

    #harm1=np.empty(shape= (0,600),dtype= (float))
    harm1=np.zeros(len(x))
    #print(p2)
    #print(harm1)
    #len(p2)
    #len(harm1)
    for j in range(n+1):
        for i in range(600):
            harm1[i] = (((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            
            p2[i]=p2[i]+harm1[i]
        #print(type(p2))
    #print(p2)
    pwav=p2.copy()
    pwav=p2+p1-0.035-0.3
    return pwav

#qrs
def qrs_wav(x,a_qrswav,d_qrswav,li):
    l=li2
    a=a_qrswav
    b=(2*l)/d_qrswav
    n=100
    qrs1=(a/(2*b))*(2-b)
    qrs2=[]

    harm=[]

    qrs2=np.zeros(len(x))
    harm=np.zeros(len(x))

    for j in range(n+1):
        for i in range(600):       
            harm[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            qrs2[i]=qrs2[i]+harm[i]
   
    qrswav=qrs2.copy()
    qrswav=(qrs1+qrs2+1)
    return qrswav

x=np.arange(0.01,6+0.01,0.01)
#print (a)
li=30/290
li2=30/72  
    
a_pwav=0.8
d_pwav=0.2
t_pwav=-0.28

a_qrswav=1.6
d_qrswav=0.05
t_qrswav=0.015

#pwav output
x1=np.arange(0.01,6+0.01,0.01)
#print(x1)
pwav=p_wav(x1,a_pwav,d_pwav,t_pwav,li)

#qrswav output
x2=np.arange(0.01,6+0.01,0.01)
#print(x3)
qrswav=qrs_wav(x2,a_qrswav,d_qrswav,li)

#ecg output
ecg=np.zeros(len(x))
#for i in range(600):
#    ecg.append(pwav[i]+qwav[i]+qrswav[i]+twav[i]+swav[i])
for i in range(600):
    ecg[i]=pwav[i]+qrswav[i]
#figure(1);
#test=np.zeros(len(x))
#for i in range(600):
#    test[i]=pwav[i]+qwav[i]
#subplot(3,1,1)
#print(type(ecg))
#print(len(x))
#print(len(ecg))
#print(a)

#fig, axs = plt.subplots(6)
a=np.arange(0.01,6+0.01,0.01)
#axs[0].plot(a,pwav)
#axs[1].plot(a,qwav)
#axs[2].plot(a,qrswav)
#axs[3].plot(a,swav)
#axs[4].plot(a,twav)
#axs[5].plot(a,ecg)


plt.plot(a,ecg)

plt.title('Atrial Flutter')
plt.xlabel('time (in seconds)')
plt.ylabel('Volts(mV)')
plt.show()
#plot(x,ecg)