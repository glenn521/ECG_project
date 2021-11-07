import numpy as np
import math
import matplotlib.pyplot as plt

#pwav
def p_wav(x,a_pwav,d_pwav,t_pwav,li):
    l=li
    a=a_pwav

    for i in range(len(x)):
        x[i]=x[i]+t_pwav-0.035

    b=(2*l)/d_pwav
    n=100
    p1=1/l



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

#qwav
def q_wav(x,a_qwav,d_qwav,t_qwav,li):
    l=li
    for i in range(len(x)):
        x[i]=x[i]+t_qwav-0.05

    #x=x + t_qwav-0.05
    a=a_qwav
    b=(2*l)/d_qwav
    n=100
    q1=(a/(2*b))*(2-b)
    q2=[]

    q2=np.zeros(len(x))

    harm5=[]
    harm5=np.zeros(len(x))

    for j in range(n+1):
        for i in range(600):
            harm5[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            q2[i]=q2[i]+harm5[i]
            
            
        #print(type(p2))

    qwav=q2.copy()
    qwav=qwav*(-1)
    return qwav

#qrs
def qrs_wav(x,a_qrswav,d_qrswav,t_qrstwav,li):
    l=li
    for i in range(len(x)):
        x[i]=x[i]+t_qrstwav
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
    #for i in range(600):
    #    qrswav[i]=qrswav[i] + qrs1+1
    return qrswav

#swav
def s_wav(x,a_swav,d_swav,t_swav,li):
    l=li  
    
    for i in range(len(x)):
        x[i]=x[i]-t_swav-0.035
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

def s_wav2(x,a_swav2,d_swav2,t_swav2,li):
    l=li  
    
    for i in range(len(x)):
        x[i]=x[i]-t_swav2-0.035
    #x=x-t_swav+0.035

    a=a_swav2
    b=(2*l)/d_swav2
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

    swav2=s2.copy()
    swav2=swav2*(-1)
    return swav2
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
li=30/20
    
#a_pwav=0.25
#d_pwav=0.10
#t_pwav=0.2  

#a_qwav=0.4
#d_qwav=0.06
#t_qwav=0.07

a_qrswav=0.10
d_qrswav=0.3
t_qrstwav=-0.5

a_twav=0.25
d_twav=0.20
t_twav=-0.03+0.5

a_swav=0.1
d_swav=0.2
t_swav=0.11+0.28+0.5

a_twav2=-0.3
d_twav2=0.4
t_twav2=0.2+0.08+0.5

a_twav3=0.4
d_twav3=0.40
t_twav3=0.2+0.48+0.5

a_twav4=-0.1
d_twav4=0.20
t_twav4=0.2+0.43+0.5

a_swav2=0.1
d_swav2=0.2
t_swav2=0.11+0.85+0.5

#pwav output
x1=np.arange(0.01,6+0.01,0.01)
#print(x1)
twav=t_wav(x1,a_twav,d_twav,t_twav,li)

#qwav output
x2=np.arange(0.01,6+0.01,0.01)
#print(x2)
swav=s_wav(x2,a_swav,d_swav,t_swav,li)

#qrswav output
x3=np.arange(0.01,6+0.01,0.01)
#print(x3)
qrswav=qrs_wav(x3,a_qrswav,d_qrswav,t_qrstwav,li)

#swav output
x4=np.arange(0.01,6+0.01,0.01)
#print(x4)
twav2=t_wav(x4,a_twav2,d_twav2,t_twav2,li)

#twav output
x5=np.arange(0.01,6+0.01,0.01)
#print(x5)
twav3=t_wav(x5,a_twav3,d_twav3,t_twav3,li)

x6=np.arange(0.01,6+0.01,0.01)
#print(x5)
twav4=t_wav(x6,a_twav4,d_twav4,t_twav4,li)

x7=np.arange(0.01,6+0.01,0.01)
#print(x5)
swav2=s_wav2(x7,a_swav2,d_swav2,t_swav2,li)

#ecg output
ecg=np.zeros(len(x))
#for i in range(600):
#    ecg.append(pwav[i]+qwav[i]+qrswav[i]+twav[i]+swav[i])
for i in range(600):
    ecg[i]=qrswav[i]+twav[i]+swav[i]+twav2[i]+twav3[i]+twav4[i]
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

axes = plt.gca()
#xmin=0
#xmax=4
#axes.set_xlim([xmin,xmax])
ymin=-1
ymax=1
axes.set_ylim([ymin,ymax])


plt.plot(a,ecg,color="blue")

plt.title('Agonal Rhythm')
plt.xlabel('time (in seconds)')
plt.ylabel('Volts(mV)')
plt.show()
#plot(x,ecg)
