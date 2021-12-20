import numpy as np
import math
import matplotlib.pyplot as plt
#from pconst import const

#pwav
def p_wav(x,a_pwav,d_pwav,t_pwav,li):
    l=li
    a=a_pwav

    for i in range(len(x)):
        x[i]=x[i]+t_pwav-0.035

    b=(2*l)/d_pwav
    n=100
   #p1=1/l



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
    pwav=pwav*a
    return pwav

#qrs
def qrs_wav(x,a_qrswav,d_qrswav,li):
    l=li
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
    #qrswav=[(qrs1+x+1) for x in qrswav]
    for i in range(600):
        qrswav[i]=qrswav[i] + qrs1+1
    return qrswav

#swav
def s_wav(x,a_swav,d_swav,t_swav,li):
    l=li  
    
    for i in range(len(x)):
        x[i]=x[i]-t_swav+0.035
    #x=x-t_swav+0.035

    a=a_swav
    b=(2*l)/d_swav
    n=100
    s1=(a/(2*b))*(2-b)
    s2=[]
    harm3=[]

    s2=np.zeros(len(x))
    harm3=np.zeros(len(x))

    for j in range(n+1):
        for i in range(600):       
            
            harm3[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            s2[i]=s2[i]+harm3[i]


    #swav=-1*(s2)

    swav=s2.copy()
    swav=swav*(-1)
    return swav

#twav
def t_wav(x,a_twav,d_twav,t_twav,li):
    l=li
    a=a_twav

    for i in range(len(x)):
        x[i]=x[i]-t_twav-0.04
    #x=x-t_twav-0.04
    b=(2*l)/d_twav
    n=100
    t1=1/l
    t2=[]
    harm2=[]

    t2=np.zeros(len(x))
    harm2=np.zeros(len(x))

    for j in range(n+1):
        for i in range(600):
            
            harm2[i]=(((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            t2[i]=t2[i]+harm2[i]


    twav=t2.copy()
    twav=twav*a
    #twav1=t2
    #twav=a*twav1
    return twav

x=np.arange(0.01,6+0.01,0.01)
#print (a)
li=30/105  
    
a_pwav=-0.15
d_pwav=0.05
t_pwav=0.15

a_qrswav=1.2
d_qrswav=0.08

a_swav=0.6
d_swav=0.065
t_swav=0.065

a_twav=0.25
d_twav=0.14
t_twav=0.2

#pwav output
x1=np.arange(0.01,6+0.01,0.01)
#print(x1)
pwav=p_wav(x1,a_pwav,d_pwav,t_pwav,li)

#qrswav output
x3=np.arange(0.01,6+0.01,0.01)
#print(x3)
qrswav=qrs_wav(x3,a_qrswav,d_qrswav,li)

#swav output
x4=np.arange(0.01,6+0.01,0.01)
#print(x4)
swav=s_wav(x4,a_swav,d_swav,t_swav,li)

#twav output
x5=np.arange(0.01,6+0.01,0.01)
#print(x5)
twav=t_wav(x5,a_twav,d_twav,t_twav,li)

#ecg output
ecg=np.zeros(len(x))
#for i in range(600):
#    ecg.append(pwav[i]+qrswav[i]+twav[i]+swav[i])
for i in range(600):
    ecg[i]=pwav[i]+qrswav[i]+twav[i]+swav[i]

#fig, axs = plt.subplots(6)
a=np.arange(0.01,6+0.01,0.01)
#axs[0].plot(a,pwav)
#axs[1].plot(a,qwav)
#axs[2].plot(a,qrswav)
#axs[3].plot(a,swav)
#axs[4].plot(a,twav)
#axs[5].plot(a,ecg)


axes = plt.gca()
#axes.set_xlim([xmin,xmax])
ymin=-3
ymax=4
axes.set_ylim([ymin,ymax])


plt.plot(a,ecg,color='blue')

plt.title('Junctional Tachycardia')
plt.xlabel('time (in seconds)')
plt.ylabel('Volts(mV)')
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()
#plot(x,ecg)
