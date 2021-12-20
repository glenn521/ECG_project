import numpy as np
from numpy import sum,isrealobj,sqrt
from numpy.random import standard_normal
from math import cos,sin,pi
import matplotlib.pyplot as plt
plt.style.use('dark_background')



def awgn(s,SNRdB,L=1):
    """
    AWGN channel
    Add AWGN noise to input signal. The function adds AWGN noise vector to signal 's' to generate a resulting signal vector 'r' of specified SNR in dB. It also
    returns the noise vector 'n' that is added to the signal 's' and the power spectral density N0 of noise added
    Parameters:
        s : input/transmitted signal vector
        SNRdB : desired signal to noise ratio (expressed in dB) for the received signal
        L : oversampling factor (applicable for waveform simulation) default L = 1.
    Returns:
        r : received signal vector (r=s+n)
"""
    gamma = 10**(SNRdB/10) #SNR to linear scale
    if s.ndim==1:# if s is single dimensional vector
        P=L*sum(abs(s)**2)/len(s) #Actual power in the vector
    else: # multi-dimensional signals like MFSK
        P=L*sum(sum(abs(s)**2))/len(s) # if s is a matrix [MxN]
    N0=P/gamma # Find the noise spectral density
    if isrealobj(s):# check if input is real/complex object type
        n = sqrt(N0/2)*standard_normal(s.shape) # computed noise
    else:
        n = sqrt(N0/2)*(standard_normal(s.shape)+1j*standard_normal(s.shape))
    r = s + n # received signal
    return r

#pwav
def p_wav(x,a_pwav,d_pwav,t_pwav,li2):
    l=li2
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
    pwav=pwav*a
    pwav=awgn(pwav,10,L=1)
    return pwav

#qwav
def q_wav(x,a_qwav,d_qwav,t_qwav,li):
    l=li
    for i in range(len(x)):
        x[i]=x[i]+t_qwav-0.05

    a=a_qwav
    b=(2*l)/d_qwav
    n=8
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
    qwav=qwav*(-1)
    qwav=awgn(qwav,10,L=1)
    return qwav

#qwav2
def q_wav2(x,a_qwav2,d_qwav2,t_qwav2,li2):
    l=li2
    for i in range(len(x)):
        x[i]=x[i]+t_qwav2-0.05

    a=a_qwav2
    b=(2*l)/d_qwav2
    n=8
    q1=(a/(2*b))*(2-b)
    q2=[]

    q2=np.zeros(len(x))

    harm5=[]
    harm5=np.zeros(len(x))

    for j in range(n+1):
        for i in range(600):
            harm5[i]=(((2*b*a)/((j+1)*(j+1)*pi*pi))*(1-cos(((j+1)*pi)/b)))*cos(((j+1)*pi*x[i])/l)
            q2[i]=q2[i]+harm5[i]
            
            

    qwav2=q2.copy()
    qwav2=qwav2*(-1)
    qwav2=awgn(qwav2,10,L=1)
    return qwav2

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
            harm[i]=(((2*b*a)/((j+1)*(j+1)*pi*pi))*(1-cos(((j+1)*pi)/b)))*cos(((j+1)*pi*x[i])/l)
            qrs2[i]=qrs2[i]+harm[i]


    
    qrswav=qrs2.copy()
    for i in range(600):
        qrswav[i]=qrswav[i] + qrs1+1
    return qrswav

#qrs2
def qrs_wav2(x,a_qrswav2,d_qrswav2,t_qrswav2,li):
    l=li
    for i in range(len(x)):
        x[i]=x[i]+t_qrswav2
    a=a_qrswav2
    b=(2*l)/d_qrswav2
    n=100
    qrs1=(a/(2*b))*(2-b)
    qrs2=[]

    harm=[]

    qrs2=np.zeros(len(x))
    harm=np.zeros(len(x))

    for j in range(n+1):
        for i in range(600):       
            harm[i]=(((2*b*a)/((j+1)*(j+1)*pi*pi))*(1-cos(((j+1)*pi)/b)))*cos(((j+1)*pi*x[i])/l)
            qrs2[i]=qrs2[i]+harm[i]


    
    qrswav=qrs2.copy()
    for i in range(600):
        qrswav[i]=qrswav[i] + qrs1+1
    return qrswav

#swav
def s_wav(x,a_swav,d_swav,t_swav,li):
    l=li  
    
    for i in range(len(x)):
        x[i]=x[i]-t_swav+0.035

    a=a_swav
    b=(2*l)/d_swav
    n=8
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
    swav=swav*(-1)
    swav=awgn(swav,10,L=1)
    return swav

def s_wav2(x,a_swav,d_swav,t_swav,li):
    l=li  
    
    for i in range(len(x)):
        x[i]=x[i]-t_swav+0.035

    a=a_swav
    b=(2*l)/d_swav
    n=8
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
    swav=swav*(-1)
    swav=awgn(swav,10,L=1)
    return swav

#twav
def t_wav(x,a_twav,d_twav,t_twav,li2):
    l=li2
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
    twav= awgn(twav,10,L=1)
    return twav


x=np.arange(0.01,6+0.01,0.01)
li=30/36
li2=30/70
    
a_pwav=0.2
d_pwav=0.10
t_pwav=0.2  

a_qwav=0.4
d_qwav=0.06
t_qwav=0.07

a_qwav2=0.4
d_qwav2=0.06
t_qwav2=0.07+0.45

a_qrswav=2.1
d_qrswav=0.05

a_qrswav2=2.1
d_qrswav2=0.05
t_qrswav2=0.45

a_swav=0.5
d_swav=0.06
t_swav=0.065

a_swav2=0.5
d_swav2=0.06
t_swav2=0.45+0.03

a_twav=0.2
d_twav=0.08
t_twav=0.1

#pwav output
x1=np.arange(0.01,6+0.01,0.01)
pwav=p_wav(x1,a_pwav,d_pwav,t_pwav,li2)

#qwav output
x2=np.arange(0.01,6+0.01,0.01)
qwav=q_wav(x2,a_qwav,d_qwav,t_qwav,li)

#qwav2 output
x6=np.arange(0.01,6+0.01,0.01)
qwav2=q_wav2(x6,a_qwav2,d_qwav2,t_qwav2,li2)

#qrswav output
x3=np.arange(0.01,6+0.01,0.01)
qrswav=qrs_wav(x3,a_qrswav,d_qrswav,li)

#qrswav2 output
x7=np.arange(0.01,6+0.01,0.01)
qrswav2=qrs_wav2(x7,a_qrswav2,d_qrswav2,t_qrswav2,li2)

#swav output
x4=np.arange(0.01,6+0.01,0.01)
swav=s_wav(x4,a_swav,d_swav,t_swav,li)

#swav output
x8=np.arange(0.01,6+0.01,0.01)
swav2=s_wav2(x8,a_swav2,d_swav2,t_swav2,li2)

#twav output
x5=np.arange(0.01,6+0.01,0.01)
twav=t_wav(x5,a_twav,d_twav,t_twav,li2)

#ecg output
ecg=np.zeros(len(x))
for i in range(600):
    ecg[i]=pwav[i]+qwav[i]+qrswav[i]+twav[i]+swav[i]+qwav2[i]+qrswav2[i]+swav2[i]



axes = plt.gca()
#axes.set_xlim([xmin,xmax])
ymin=-3
ymax=4
axes.set_ylim([ymin,ymax])


a=np.arange(0.01,6+0.01,0.01)

plt.plot(a,ecg,color="#04ed00")
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
ax.axis("off")

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()
