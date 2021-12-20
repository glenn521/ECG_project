import numpy as np
import math
import matplotlib.pyplot as plt

#pwav
def f_wav(x,a_fwav,d_fwav,t_fwav,li):
    l=li
    a=a_fwav

    for i in range(len(x)):
        x[i]=x[i]+t_fwav

    b=(2*l)/d_fwav
    n=100
    f1=(a/(2*b)*(2-b))

    f2=np.zeros(len(x))

    #harm1=np.empty(shape= (0,600),dtype= (float))
    harm=np.zeros(len(x))
    #print(p2)
    #print(harm1)
    #len(p2)
    #len(harm1)
    for j in range(n+1):
        for i in range(600):
            #harm[i] = (((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            harm[i] = ((2*b*a)/(math.pi*math.pi*(j+1)*(j+1))*((1/math.pi*math.pi)*math.sin((j+1)*math.pi*x[i]/l)))
            f2[i]=f2[i]+harm[i]
        #print(type(p2))
    
    fwav=f2.copy()
    fwav=f2+f1-0.035-0.3
    return fwav

#qrs
def qrs_wav(x,a_qrswav,d_qrswav,t_qrswav,li):
    l=li2

    for i in range(len(x)):
        x[i]=x[i]+t_qrswav

    a=a_qrswav

    a_pwav=0.25
    d_pwav=0.20
    t_pwav=0.2 

    b2=(2*l)/d_pwav
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
    
a_fwav=0.8
d_fwav=0.2
t_fwav=-0.28

a_qrswav=1.6
d_qrswav=0.05
t_qrswav=0.015

#pwav output
x1=np.arange(0.01,6+0.01,0.01)
#print(x1)
fwav=f_wav(x1,a_fwav,d_fwav,t_fwav,li)

#qrswav output
x2=np.arange(0.01,6+0.01,0.01)
#print(x3)
qrswav=qrs_wav(x2,a_qrswav,d_qrswav,t_qrswav,li2)

#ecg output
ecg=np.zeros(len(x))
for i in range(600):
    ecg[i]=fwav[i]+qrswav[i]


#fig, axs = plt.subplots(6)
a=np.arange(0.01,6+0.01,0.01)
#axs[0].plot(a,pwav)
#axs[1].plot(a,qwav)
#axs[2].plot(a,qrswav)
#axs[3].plot(a,swav)
#axs[4].plot(a,twav)
#axs[5].plot(a,ecg)


#plt.plot(a,ecg)

axes = plt.gca()
#axes.set_xlim([xmin,xmax])
ymin=-3
ymax=4
axes.set_ylim([ymin,ymax])

#print(len(ECG1),len(a1))
plt.plot(a,ecg,color="blue")

plt.title('Atrial Flutter')
plt.xlabel('time (in seconds)')
plt.ylabel('Volts(mV)')
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()
#plot(x,ecg)