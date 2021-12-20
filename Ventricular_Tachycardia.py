import numpy as np
from math import sin,cos,pi
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
    harm1=np.zeros(len(x))

    for j in range(n+1):
        for i in range(600):
            harm1[i] = (((sin((pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(sin((pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/pi))*cos(((j+1)*pi*x[i])/l)

            p2[i]=p2[i]+harm1[i]

    pwav=p2.copy()
    pwav=(pwav*a)+0.58
    return pwav

#qwav
def q_wav(x,a_qwav,d_qwav,t_qwav,li):
    l=li
    for i in range(len(x)):
        x[i]=x[i]+t_qwav-0.05

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
            harm5[i]=(((2*b*a)/((j+1)*(j+1)*pi*pi))*(1-cos(((j+1)*pi)/b)))*cos(((j+1)*pi*x[i])/l)
            q2[i]=q2[i]+harm5[i]
                    
    qwav=q2.copy()
    qwav=qwav
    return qwav

#swav
def s_wav(x,a_swav,d_swav,t_swav,li):
    l=li  
    
    for i in range(len(x)):
        x[i]=x[i]-t_swav+0.035

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
            
            harm3[i]=(((2*b*a)/((j+1)*(j+1)*pi*pi))*(1-cos(((j+1)*pi)/b)))*cos(((j+1)*pi*x[i])/l)
            s2[i]=s2[i]+harm3[i]

    swav=s2.copy()
    swav=swav+1
    return swav

#twav
def t_wav(x,a_twav,d_twav,t_twav,li):
    l=li
    a=a_twav

    for i in range(len(x)):
        x[i]=x[i]-t_twav-0.04
    b=(2*l)/d_twav
    n=100
    t1=1/l
    t2=[]
    harm2=[]

    t2=np.zeros(len(x))
    harm2=np.zeros(len(x))

    for j in range(n+1):
        for i in range(600):
            
            harm2[i]=(((sin((pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(sin((pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/pi))*cos(((j+1)*pi*x[i])/l)
            t2[i]=t2[i]+harm2[i]

    twav=t2.copy()
    twav=twav*a
    return twav


x=np.arange(0.01,6+0.01,0.01)
li=30/145  
    
a_twav=1.8 
d_twav=0.45 
t_twav=0.2 

a_pwav=1.4 
d_pwav=0.2 
t_pwav=-0.24 

a_swav=1.3 
d_swav=0.18 
t_swav=0.4 

a_qwav=1.3 
d_qwav=0.05 
t_qwav=-0.34 


#pwav output
x1=np.arange(0.01,6+0.01,0.01)
pwav=p_wav(x1,a_pwav,d_pwav,t_pwav,li)

#qwav output
x2=np.arange(0.01,6+0.01,0.01)
qwav=q_wav(x2,a_qwav,d_qwav,t_qwav,li)

#swav output
x4=np.arange(0.01,6+0.01,0.01)
swav=s_wav(x4,a_swav,d_swav,t_swav,li)

#twav output
x5=np.arange(0.01,6+0.01,0.01)
twav=t_wav(x5,a_twav,d_twav,t_twav,li)

#ecg output
ecg=np.zeros(len(x))
for i in range(600):
    ecg[i]=pwav[i]+qwav[i]+twav[i]+swav[i]

axes = plt.gca()
#axes.set_xlim([xmin,xmax])
ymin=-3
ymax=4
axes.set_ylim([ymin,ymax])


a=np.arange(0.01,6+0.01,0.01)
plt.plot(a,ecg,color='blue')

plt.title('Ventricular Tachycardia')
plt.xlabel('time (in seconds)')
plt.ylabel('Volts(mV)')
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()