import numpy as np
import math
import matplotlib.pyplot as plt

#pwav
def p_wav(x,a_pwav,d_pwav,t_pwav,li,aa,bb,cc):
    l=li
    a=a_pwav

    for i in range(aa,bb,cc):
        x[i]=x[i]+t_pwav-0.035

    b=(2*l)/d_pwav
    n=100
    p1=1/l



    p2=np.zeros(len(x))

    #harm1=np.empty(shape= (0,600),dtype= (float))
    harm1=np.zeros(len(x))
    
    for j in range(n+1):
        for i in range(aa,bb,cc):
            harm1[i] = (((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            
            p2[i]=p2[i]+harm1[i]
        #print(type(p2))
    #print(p2)
    pwav=p2.copy()
    pwav=pwav*a
    return pwav

#qwav
def q_wav(x,a_qwav,d_qwav,t_qwav,li,aa,bb,cc):
    l=li
    for i in range(aa,bb,cc):
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
        for i in range(aa,bb,cc):
            harm5[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            q2[i]=q2[i]+harm5[i]
            
            
        #print(type(p2))

    qwav=q2.copy()
    qwav=qwav*(-1)
    return qwav

#qrs
def qrs_wav(x,a_qrswav,d_qrswav,t_qrswav,li,aa,bb,cc):
    l=li
    for i in range(aa,bb,cc):
        x[i]=x[i]+t_qrswav
    a=a_qrswav
    b=(2*l)/d_qrswav
    n=100
    qrs1=(a/(2*b))*(2-b)
    qrs2=[]

    harm=[]

    qrs2=np.zeros(len(x))
    harm=np.zeros(len(x))

    for j in range(n+1):
        for i in range(aa,bb,cc):       
            harm[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            qrs2[i]=qrs2[i]+harm[i]


    
    qrswav=qrs2.copy()
    #qrswav=[(qrs1+x+1) for x in qrswav]
    for i in range(aa,bb,cc):
        qrswav[i]=qrswav[i] + 0.09
    return qrswav

#swav
def s_wav(x,a_swav,d_swav,t_swav,li,aa,bb,cc):
    l=li  
    
    for i in range(aa,bb,cc):
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
        for i in range(aa,bb,cc):       
            
            harm3[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            s2[i]=s2[i]+harm3[i]


    #swav=-1*(s2)

    swav=s2.copy()
    swav=swav*(-1)
    return swav

#twav
def t_wav(x,a_twav,d_twav,t_twav,li,aa,bb,cc):
    l=li
    a=a_twav

    for i in range(aa,bb,cc):
        x[i]=x[i]-t_twav
    #x=x-t_twav-0.04
    b=(2*l)/d_twav
    n=100
    t1=1/l
    t2=[]
    harm2=[]

    t2=np.zeros(len(x))
    harm2=np.zeros(len(x))

    for j in range(n+1):
        for i in range(aa,bb,cc):
            
            harm2[i]=(((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            t2[i]=t2[i]+harm2[i]


    twav=t2.copy()
    twav=twav*a
    #twav1=t2
    #twav=a*twav1
    return twav

####################################################################################################################################################################################################
#                                   part-1
####################################################################################################################################################################################################
#0.01:1.59+0.01:0.01
#print (a)
def ecg1():
    li=30/72  
        
    a_pwav=0.25
    d_pwav=0.10
    t_pwav=0.2+0.4  

    a_qwav=0.4
    d_qwav=0.06
    t_qwav=0.07+0.4

    a_qrswav=2.1
    d_qrswav=0.05
    t_qrswav=0.4

    a_swav=0.6
    d_swav=0.06
    t_swav=0.065-0.4

    a_twav=0.35
    d_twav=0.14
    t_twav=0.2-0.4

    aa=0
    bb=155
    cc=1
    #pwav output
    x1=np.arange(0.01,1.55+0.01,0.01)
    #print(x1)
    pwav=p_wav(x1,a_pwav,d_pwav,t_pwav,li,aa,bb,cc)

    #qwav output
    x2=np.arange(0.01,1.55+0.01,0.01)
    #print(x2)
    qwav=q_wav(x2,a_qwav,d_qwav,t_qwav,li,aa,bb,cc)

    #qrswav output
    x3=np.arange(0.01,1.55+0.01,0.01)
    #print(x3)
    qrswav=qrs_wav(x3,a_qrswav,d_qrswav,t_qrswav,li,aa,bb,cc)

    #swav output
    x4=np.arange(0.01,1.55+0.01,0.01)
    #print(x4)
    swav=s_wav(x4,a_swav,d_swav,t_swav,li,aa,bb,cc)

    #twav output
    x5=np.arange(0.01,1.55+0.01,0.01)
    #print(x5)
    twav=t_wav(x5,a_twav,d_twav,t_twav,li,aa,bb,cc)

    #ecg output
    ecg1=np.zeros(len(x1)) #len(x1) or len(x2 or x3 or x4 or x5)

    for i in range(aa,bb,cc):
        ecg1[i]=pwav[i]+qwav[i]+qrswav[i]+twav[i]+swav[i]-0.006
    return ecg1
####################################################################################################################################################################################################
#                                   part-2
####################################################################################################################################################################################################

#1.59:2.2+0.01:0.01
#print (a)
def ecg2():
    li=30/72
    
    a_pwav=0.3
    d_pwav=0.12
    t_pwav=-0.2+0.38+0.48

    a_qwav=2
    d_qwav=0.12
    t_qwav=0.07+0.38+0.35
    
    
    a_twav=1.1
    d_twav=0.16
    t_twav=0.2-0.38-0.48


    aa=155
    bb=220
    cc=1


    #pwav output
    x1=np.zeros(600)
    c=1.55
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    pwav2=p_wav(x1,a_pwav,d_pwav,t_pwav,li,aa,bb,cc)

    #qwav output
    x1=np.zeros(600)
    c=1.55
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    qwav2=q_wav(x1,a_qwav,d_qwav,t_qwav,li,aa,bb,cc)
    
    '''#qrswav output
    x1=np.zeros(600)
    c=1.55
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    qrswav2=qrs_wav(x1,a_qrswav,d_qrswav,t_qrswav,li,aa,bb,cc)

    #swav output
    x1=np.zeros(600)
    c=1.55
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    swav2=s_wav(x1,a_swav,d_swav,t_swav,li,aa,bb,cc)
    '''
    #twav output
    x1=np.zeros(600)
    c=1.55
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    twav2=t_wav(x1,a_twav,d_twav,t_twav,li,aa,bb,cc)

    #ecg output
    ecg2=np.zeros(600)

    for i in range(aa,bb,cc):
        ecg2[i]=qwav2[i]+pwav2[i]+twav2[i]-0.0308+0.05

    return ecg2
####################################################################################################################################################################################################
#                                   part-3
####################################################################################################################################################################################################
def ecg3():
    li=30/72
    a_pwav=0.25
    d_pwav=0.10
    t_pwav=0.2-0.35+0.2
    
    a_qwav=0.4
    d_qwav=0.06
    t_qwav=0.07-0.35+0.2
    
    a_qrswav=2.1
    d_qrswav=0.05
    t_qrswav=-0.35+0.2
    
    
    a_swav=0.6
    d_swav=0.06
    t_swav=0.065+0.35-0.20
    
    a_twav=0.35
    d_twav=0.14
    t_twav=0.2+0.35-0.2
   
    aa=220
    bb=470
    cc=1

    #pwav output
    x1=np.zeros(600)
    c=2.2
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    #print(x1)
    pwav=p_wav(x1,a_pwav,d_pwav,t_pwav,li,aa,bb,cc)

    #qwav output
    x1=np.zeros(600)
    c=2.2
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    #print(x2)
    qwav=q_wav(x1,a_qwav,d_qwav,t_qwav,li,aa,bb,cc)

    #qrswav output
    x1=np.zeros(600)
    c=2.2
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    #print(x3)
    qrswav=qrs_wav(x1,a_qrswav,d_qrswav,t_qrswav,li,aa,bb,cc)

    #swav output
    x1=np.zeros(600)
    c=2.2
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    #print(x4)
    swav=s_wav(x1,a_swav,d_swav,t_swav,li,aa,bb,cc)

    #twav output
    x1=np.zeros(600)
    c=2.2
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    #print(x5)
    twav=t_wav(x1,a_twav,d_twav,t_twav,li,aa,bb,cc)

    #ecg output
    ecg3=np.zeros(len(x1)) #len(x1) or len(x2 or x3 or x4 or x5)

    for i in range(aa,bb,cc):
        ecg3[i]=pwav[i]+qwav[i]+qrswav[i]+twav[i]+swav[i]-0.006

    return ecg3


####################################################################################################################################################################################################
#                                   part-4
####################################################################################################################################################################################################

def ecg4():
    li=30/72
    
    a_pwav=0.3
    d_pwav=0.12
    t_pwav=-0.2+0.38+0.48+0.3

    
    a_qwav=2
    d_qwav=0.12
    t_qwav=0.07+0.38+0.35+0.3
    
    
    a_twav=1.1
    d_twav=0.16
    t_twav=0.2-0.38-0.48-0.3

    aa=470
    bb=530
    cc=1


    #pwav output
    x1=np.zeros(600)
    c=4.7
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    pwav=p_wav(x1,a_pwav,d_pwav,t_pwav,li,aa,bb,cc)

    #qwav output
    x1=np.zeros(600)
    c=4.7
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    qwav=q_wav(x1,a_qwav,d_qwav,t_qwav,li,aa,bb,cc)
    
    #twav output
    x1=np.zeros(600)
    c=4.7
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    twav=t_wav(x1,a_twav,d_twav,t_twav,li,aa,bb,cc)

    #ecg output
    ecg=np.zeros(600)

    for i in range(aa,bb,cc):
        ecg[i]=qwav[i]+pwav[i]+twav[i]-0.0308+0.00573+0.0439

    return ecg

####################################################################################################################################################################################################
#                                   part-5
####################################################################################################################################################################################################

def ecg5():
    li=30/72
    a_pwav=0.25
    d_pwav=0.10
    t_pwav=0.2+0.05+0.95
    
    a_qwav=0.4
    d_qwav=0.06
    t_qwav=0.07+0.05+0.95
    
    a_qrswav=2.1
    d_qrswav=0.05
    t_qrswav=0.05+0.95
    
    
    a_swav=0.6
    d_swav=0.06
    t_swav=0.065-0.05-0.95
    
    a_twav=0.35
    d_twav=0.14
    t_twav=0.2-0.05-0.95

    aa=530
    bb=600
    cc=1

    #pwav output
    x1=np.zeros(600)
    c=5.3
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    #print(x1)
    pwav=p_wav(x1,a_pwav,d_pwav,t_pwav,li,aa,bb,cc)

    #qwav output
    x1=np.zeros(600)
    c=5.3
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    #print(x2)
    qwav=q_wav(x1,a_qwav,d_qwav,t_qwav,li,aa,bb,cc)

    #qrswav output
    x1=np.zeros(600)
    c=5.3
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    #print(x3)
    qrswav=qrs_wav(x1,a_qrswav,d_qrswav,t_qrswav,li,aa,bb,cc)

    #swav output
    x1=np.zeros(600)
    c=5.3
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    #print(x4)
    swav=s_wav(x1,a_swav,d_swav,t_swav,li,aa,bb,cc)

    #twav output
    x1=np.zeros(600)
    c=5.3
    for i in range(aa,bb,cc):
        x1[i]=c
        c=c+0.01
    #print(x5)
    twav=t_wav(x1,a_twav,d_twav,t_twav,li,aa,bb,cc)

    #ecg output
    ecg5=np.zeros(len(x1)) #len(x1) or len(x2 or x3 or x4 or x5)

    for i in range(aa,bb,cc):
        ecg5[i]=pwav[i]+qwav[i]+qrswav[i]+twav[i]+swav[i]-0.0064

    return ecg5


####################################################################################################################################################################################################
#                                   slicing
####################################################################################################################################################################################################

ECG1=ecg1()

ecg=ecg2()
#XX1=np.arange(3.88,6+0.01,0.01)
ECG2=np.zeros(66, dtype = float)
for i in range(155,220,1):
   
    ECG2[i-155]=ecg[i]


ecg=ecg3()
#XX1=np.arange(3.88,6+0.01,0.01)
ECG3=np.zeros(251, dtype = float)
for i in range(220,470,1):
   
    ECG3[i-220]=ecg[i]

ecg=ecg4()
#XX1=np.arange(3.88,6+0.01,0.01)
ECG4=np.zeros(61, dtype = float)
for i in range(470,530,1):
   
    ECG4[i-470]=ecg[i]

ecg=ecg5()
#XX1=np.arange(3.88,6+0.01,0.01)
ECG5=np.zeros(71, dtype = float)
for i in range(530,600,1):
   
    ECG5[i-530]=ecg[i]



a1=np.arange(0.01,1.55+0.01,0.01)
a2=np.arange(1.55,2.2+0.01,0.01)
a3=np.arange(2.2,4.7+0.01,0.01)
a4=np.arange(4.7,5.3+0.01,0.01)
a5=np.arange(5.3,6+0.01,0.01)

#changing y axis scaling

axes = plt.gca()
#axes.set_xlim([xmin,xmax])
ymin=-3
ymax=4
axes.set_ylim([ymin,ymax])

#print(len(ECG1),len(a1))
plt.plot(a1,ECG1,color="blue")
plt.plot(a2,ECG2,color="blue")
plt.plot(a3,ECG3,color="blue")
plt.plot(a4,ECG4,color="blue")
plt.plot(a5,ECG5,color="blue")

plt.title('Premature Junctional Complexes')
plt.xlabel('time (in seconds)')
plt.ylabel('Volts(mV)')
plt.show()
#plot(x,ecg)
