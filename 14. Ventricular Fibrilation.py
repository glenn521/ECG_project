import numpy as np
from numpy import sum,isrealobj,sqrt
from numpy.random import standard_normal
from math import cos,sin,pi
import matplotlib.pyplot as plt


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
def p_wav(x,a_pwav,d_pwav,t_pwav,li,aa,bb,cc):
    l=li
    a=a_pwav

    for i in range(aa,bb,cc):
        x[i]=x[i]+t_pwav-0.035

    b=(2*l)/d_pwav
    n=1
    p1=1/l



    p2=np.zeros(len(x))

    harm1=np.zeros(len(x))

    for j in range(n+1):
        for i in range(aa,bb,cc):
            harm1[i] = (((sin((pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(sin((pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/pi))*cos(((j+1)*pi*x[i])/l)
            
            p2[i]=p2[i]+harm1[i]

    pwav=p2.copy()
    pwav=pwav*a
    pwav=awgn(pwav,20,L=1)
    return pwav

#pwav2
def p_wav2(x2,a_pwav2,d_pwav2,t_pwav2,li,aa,bb,cc):
    l=li
    a=a_pwav2

    for i in range(aa,bb,cc):
        x2[i]=x2[i]+t_pwav2-0.035

    b=(2*l)/d_pwav2
    n=1
    p1=1/l

    p2=np.zeros(len(x2))

    harm1=np.zeros(len(x2))

    for j in range(n+1):
        for i in range(aa,bb,cc):
            harm1[i] = (((sin((pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(sin((pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/pi))*cos(((j+1)*pi*x2[i])/l)
            
            p2[i]=p2[i]+harm1[i]

    pwav2=p2.copy()
    pwav2=pwav2*a
    pwav2=awgn(pwav2,20,L=1)
    return pwav2

#qwav
def q_wav(x1,a_qwav,d_qwav,t_qwav,li2,aa,bb,cc):
    l=li2
    for i in range(aa,bb,cc):
        x1[i]=x1[i]+t_qwav-0.05

    a=a_qwav
    b=(2*l)/d_qwav
    n=1
    q1=(a/(2*b))*(2-b)
    q2=[]

    q2=np.zeros(len(x1))

    harm5=[]
    harm5=np.zeros(len(x1))

    for j in range(n+1):
        for i in range(aa,bb,cc):
            harm5[i]=(((2*b*a)/((j+1)*(j+1)*pi*pi))*(1-cos(((j+1)*pi)/b)))*cos(((j+1)*pi*x1[i])/l)
            q2[i]=q2[i]+harm5[i]
            
            

    qwav=q2.copy()
    qwav=qwav*(-1)
    qwav=awgn(qwav,50,L=1)
    return qwav

#qwav2
def q_wav2(x3,a_qwav2,d_qwav2,t_qwav2,li2,aa,bb,cc):
    l=li2
    for i in range(aa,bb,cc):
        x3[i]=x3[i]+t_qwav2-0.05

    a=a_qwav2
    b=(2*l)/d_qwav2
    n=100
    q1=(a/(2*b))*(2-b)
    q2=[]

    q2=np.zeros(len(x3))

    harm5=[]
    harm5=np.zeros(len(x3))

    for j in range(n+1):
        for i in range(aa,bb,cc):
            harm5[i]=(((2*b*a)/((j+1)*(j+1)*pi*pi))*(1-cos(((j+1)*pi)/b)))*cos(((j+1)*pi*x3[i])/l)
            q2[i]=q2[i]+harm5[i]
            
            

    qwav2=q2.copy()
    qwav2=qwav2*(-1)
    qwav2=awgn(qwav2,19,L=1)
    return qwav2

#qrs
def qrs_wav(x2,a_qrswav,d_qrswav,li3,aa,bb,cc):
    l=li3
    
    a=a_qrswav
    b=(2*l)/d_qrswav
    n=100
    qrs1=(a/(2*b))*(2-b)
    qrs2=[]

    harm=[]

    qrs2=np.zeros(len(x2))
    harm=np.zeros(len(x2))

    for j in range(n+1):
        for i in range(aa,bb,cc):       
            harm[i]=(((2*b*a)/((j+1)*(j+1)*pi*pi))*(1-cos(((j+1)*pi)/b)))*cos(((j+1)*pi*x2[i])/l)
            qrs2[i]=qrs2[i]+harm[i]


    
    qrswav=qrs2.copy()
    for i in range(aa,bb,cc):
        qrswav[i]=qrswav[i] + qrs1+1
    return qrswav

#swav
def s_wav(x4,a_swav,d_swav,t_swav,li7,aa,bb,cc):
    l=li7  
    
    for i in range(aa,bb,cc):
        x4[i]=x4[i]-t_swav+0.035

    a=a_swav
    b=(2*l)/d_swav
    n=100
    s1=(a/(2*b))*(2-b)
    s2=[]
    harm3=[]

    s2=np.zeros(len(x4))
    harm3=np.zeros(len(x4))

    for j in range(n+1):
        for i in range(aa,bb,cc):       
            
            harm3[i]=(((2*b*a)/((j+1)*(j+1)*pi*pi))*(1-cos(((j+1)*pi)/b)))*cos(((j+1)*pi*x4[i])/l)
            s2[i]=s2[i]+harm3[i]



    swav=s2.copy()
    swav=swav*(-1)
    return swav

#swav3
def s_wav3(x3,a_swav3,d_swav3,t_swav3,li8,aa,bb,cc):
    l=li8  
    
    for i in range(aa,bb,cc):
        x3[i]=x3[i]-t_swav3+0.035

    a=a_swav3
    b=(2*l)/d_swav3
    n=100
    s1=(a/(2*b))*(2-b)
    s2=[]
    harm3=[]

    s2=np.zeros(len(x3))
    harm3=np.zeros(len(x3))

    for j in range(n+1):
        for i in range(aa,bb,cc):       
            
            harm3[i]=(((2*b*a)/((j+1)*(j+1)*pi*pi))*(1-cos(((j+1)*pi)/b)))*cos(((j+1)*pi*x3[i])/l)
            s2[i]=s2[i]+harm3[i]



    swav3=s2.copy()
    swav3=swav3*(-1)
    return swav3

#swav5
def s_wav5(x,a_swav5,d_swav5,t_swav5,li5,aa,bb,cc):
    l=li5 
    
    for i in range(aa,bb,cc):
        x[i]=x[i]-t_swav5+0.035

    a=a_swav5
    b=(2*l)/d_swav5
    n=100
    s1=(a/(2*b))*(2-b)
    s2=[]
    harm3=[]

    s2=np.zeros(len(x))
    harm3=np.zeros(len(x))

    for j in range(n+1):
        for i in range(aa,bb,cc):       
            
            harm3[i]=(((2*b*a)/((j+1)*(j+1)*pi*pi))*(1-cos(((j+1)*pi)/b)))*cos(((j+1)*pi*x[i])/l)
            s2[i]=s2[i]+harm3[i]



    swav5=s2.copy()
    swav5=swav5*(-1)
    return swav5

#twav
def t_wav(x1,a_twav,d_twav,t_twav,li2,aa,bb,cc):
    l=li2
    a=a_twav

    for i in range(aa,bb,cc):
        x1[i]=x1[i]-t_twav-0.04
    b=(2*l)/d_twav
    n=1
    t1=1/l
    t2=[]
    harm2=[]

    t2=np.zeros(len(x1))
    harm2=np.zeros(len(x1))

    for j in range(n+1):
        for i in range(aa,bb,cc):
            
            harm2[i]=(((sin((pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(sin((pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/pi))*cos(((j+1)*pi*x1[i])/l)
            t2[i]=t2[i]+harm2[i]


    twav=t2.copy()
    twav=twav*a
    twav= awgn(twav,20,L=1)
    return twav

#twav2
def t_wav2(x3,a_twav2,d_twav2,t_twav2,li2,aa,bb,cc):
    l=li2
    a=a_twav2

    for i in range(aa,bb,cc):
        x3[i]=x3[i]-t_twav2-0.04
    b=(2*l)/d_twav2
    n=1
    t1=1/l
    t2=[]
    harm2=[]

    t2=np.zeros(len(x3))
    harm2=np.zeros(len(x3))

    for j in range(n+1):
        for i in range(aa,bb,cc):
            
            harm2[i]=(((sin((pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(sin((pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/pi))*cos(((j+1)*pi*x3[i])/l)
            t2[i]=t2[i]+harm2[i]


    twav2=t2.copy()
    twav2=twav2*a
    twav2= awgn(twav2,19,L=1)
    return twav2

#twav4
def t_wav4(x4,a_twav4,d_twav4,t_twav4,li7,aa,bb,cc):
    l=li7
    a=a_twav4

    for i in range(aa,bb,cc):
        x4[i]=x4[i]-t_twav4-0.04
    b=(2*l)/d_twav4
    n=100
    t1=1/l
    t2=[]
    harm2=[]

    t2=np.zeros(len(x4))
    harm2=np.zeros(len(x4))

    for j in range(n+1):
        for i in range(aa,bb,cc):
            
            harm2[i]=(((sin((pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(sin((pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/pi))*cos(((j+1)*pi*x4[i])/l)
            t2[i]=t2[i]+harm2[i]


    twav4=t2.copy()
    twav4=twav4*a
    return twav4

#twav5
def t_wav5(x,a_twav5,d_twav5,t_twav5,li5,aa,bb,cc):
    l=li5
    a=a_twav5

    for i in range(aa,bb,cc):
        x[i]=x[i]-t_twav5-0.04
    b=(2*l)/d_twav5
    n=100
    t1=1/l
    t2=[]
    harm2=[]

    t2=np.zeros(len(x))
    harm2=np.zeros(len(x))

    for j in range(n+1):
        for i in range(aa,bb,cc):
            
            harm2[i]=(((sin((pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(sin((pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/pi))*cos(((j+1)*pi*x[i])/l)
            t2[i]=t2[i]+harm2[i]


    twav5=t2.copy()
    twav5=twav5*a
    return twav5

#twav6
def t_wav6(x4,a_twav6,d_twav6,t_twav6,li6,aa,bb,cc):
    l=li6
    a=a_twav6

    for i in range(aa,bb,cc):
        x4[i]=x4[i]-t_twav6-0.04
    b=(2*l)/d_twav6
    n=1
    t1=1/l
    t2=[]
    harm2=[]

    t2=np.zeros(len(x4))
    harm2=np.zeros(len(x4))

    for j in range(n+1):
        for i in range(aa,bb,cc):
            
            harm2[i]=(((sin((pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(sin((pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/pi))*cos(((j+1)*pi*x4[i])/l)
            t2[i]=t2[i]+harm2[i]


    twav6=t2.copy()
    twav6=twav6*a
    twav6= awgn(twav6,20,L=1)
    return twav6

#twav7
def t_wav7(x3,a_twav7,d_twav7,t_twav7,li8,aa,bb,cc):
    l=li8
    a=a_twav7

    for i in range(aa,bb,cc):
        x3[i]=x3[i]-t_twav7-0.04
    b=(2*l)/d_twav7
    n=100
    t1=1/l
    t2=[]
    harm2=[]

    t2=np.zeros(len(x3))
    harm2=np.zeros(len(x3))

    for j in range(n+1):
        for i in range(aa,bb,cc):
            
            harm2[i]=(((sin((pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(sin((pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/pi))*cos(((j+1)*pi*x3[i])/l)
            t2[i]=t2[i]+harm2[i]


    twav7=t2.copy()
    twav7=twav7*a
    return twav7

####################################################################################################################################################################################################
#                                   main
####################################################################################################################################################################################################
def main():
    #################################
    # part 1 variables
    #################################
    x1=np.arange(0.01,1+0.01,0.01)
    aa1=0
    bb1=100
    cc1=1
    #x1=0.01:0.01:1       #x - x1
    li=30/200
    li5=30/70
    
    a_pwav=1
    d_pwav=0.10
    t_pwav=0.2
    
    a_qwav=0.4
    d_qwav=0.5
    t_qwav=0.07
    
    
    a_swav5=0.3
    d_swav5=0.06
    t_swav5=0.065+0.5
    
    a_twav5=0.35
    d_twav5=0.1
    t_twav5=0.2+0.601
        
    ###########################################
    # part 2 variables
    ###########################################     
    #x2=1:0.01:1.11  #x1 - x2
    
    aa2=100        #control variables
    bb2=111
    cc2=1

    x2=np.zeros(600)
    c=1.00
    for i in range(aa2,bb2,cc2):
        x2[i]=c
        c=c+0.01

    li2=30/350
    
    a_twav=0.6
    d_twav=0.14
    t_twav=0.1
        
    ###########################################
    # part 3 variables
    ###########################################   

    #x3=1.12:0.01:3.9    #x4 - x3    1.11-3.9
    
    aa3=111       #control variables
    bb3=390
    cc3=1

    x3=np.zeros(600)
    c=1.11
    for i in range(aa3,bb3,cc3):
        x3[i]=c
        c=c+0.01


    li6=30/280
    li7=30/100
    
    a_twav6=0.2
    d_twav6=0.14
    t_twav6=0.1
    
    a_swav=0.13
    d_swav=0.06
    t_swav=0.065
    
    a_twav4=0.13
    d_twav4=0.1
    t_twav4=0.2
        
    ###########################################
    # part 4 variables
    ###########################################       

    #x4=3.9:0.01:4.51    #x2 - x4
   
    aa4=390       #control variables
    bb4=451
    cc4=1

    x4=np.zeros(600)
    c=3.9
    for i in range(aa4,bb4,cc4):
        x4[i]=c
        c=c+0.01

    a_pwav2=1
    d_pwav2=0.10
    t_pwav2=0.25

    ###########################################
    # part 5 variables
    ###########################################   

    #x5=4.5:0.01:6       #x3 - x5
    
    aa5=450       #control variables
    bb5=600
    cc5=1

    x5=np.zeros(600)
    c=4.5
    for i in range(aa5,bb5,cc5):
        x5[i]=c
        c=c+0.01

    a_pwav2=1
    d_pwav2=0.10
    t_pwav2=0.25

    
    li8=30/77
    a_twav2=0.2
    d_twav2=0.14
    t_twav2=0.04+0.03
    
    a_qwav2=0.2
    d_qwav2=0.5
    t_qwav2=0.07+0.03
    
    a_swav3=0.13
    d_swav3=0.09
    t_swav3=0.065+0.15
    
    a_twav7=0.13
    d_twav7=0.1
    t_twav7=0.20+0.15
        
        
    ######################################################################
    # fucntion calls
    ######################################################################    
    #1st call
    x1=np.arange(0.01,1+0.01,0.01)
    y=p_wav(x1,a_pwav,d_pwav,t_pwav,li,aa1,bb1,cc1)
    

    #qwav output
    #qwav=q_wav(x,a_qwav,d_qwav,t_qwav,li)
        
    #qrswav output
    #qrswav=qrs_wav(x2,a_qrswav,d_qrswav,li3);
    #swav output



    #2nd call
    x3=np.zeros(600)
    c=1.11
    for i in range(aa3,bb3,cc3):
        x3[i]=c
        c=c+0.01

    swav=s_wav(x3,a_swav,d_swav,t_swav,li7,aa3,bb3,cc3)
    

    #3rd call
    x2=np.zeros(600)
    c=1.00
    for i in range(aa2,bb2,cc2):
        x2[i]=c
        c=c+0.01
    d=t_wav(x2,a_twav,d_twav,t_twav,li2,aa2,bb2,cc2)

    
    
    #4th call
    x2=np.zeros(600)
    c=1.00
    for i in range(aa2,bb2,cc2):
        x2[i]=c
        c=c+0.01
    g=q_wav(x2,a_qwav,d_qwav,t_qwav,li2,aa2,bb2,cc2)

    
    
    #5th call
    x4=np.zeros(600)
    c=3.9
    for i in range(aa4,bb4,cc4):
        x4[i]=c
        c=c+0.01
    y2=p_wav2(x4,a_pwav2,d_pwav2,t_pwav2,li,aa4,bb4,cc4)
    

    #`th call
    '''x5=np.zeros(600)
    c=4.5
    for i in range(aa5,bb5,cc5):
        x5[i]=c
        c=c+0.01'''


    #6th call
    x5=np.zeros(600)
    c=4.5
    for i in range(aa5,bb5,cc5):
        x5[i]=c
        c=c+0.01
    d2=t_wav2(x5,a_twav2,d_twav2,t_twav2,li2,aa5,bb5,cc5)
    
    
    
    #7th call
    x5=np.zeros(600)
    c=4.5
    for i in range(aa5,bb5,cc5):
        x5[i]=c
        c=c+0.01
    g2=q_wav2(x5,a_qwav2,d_qwav2,t_qwav2,li2,aa5,bb5,cc5)
    


    #8th call
    x1=np.arange(0.01,1+0.01,0.01)
    twav5=t_wav5(x1,a_twav5,d_twav5,t_twav5,li5,aa1,bb1,cc1)



    #9th call
    x1=np.arange(0.01,1+0.01,0.01)
    swav5=s_wav5(x1,a_swav5,d_swav5,t_swav5,li5,aa1,bb1,cc1)
    


    #10th call
    x3=np.zeros(600)
    c=1.11
    for i in range(aa3,bb3,cc3):
        x3[i]=c
        c=c+0.01
    d9=t_wav6(x3,a_twav6,d_twav6,t_twav6,li6,aa3,bb3,cc3)
    


    #11th call
    x3=np.zeros(600)
    c=1.11
    for i in range(aa3,bb3,cc3):
        x3[i]=c
        c=c+0.01
    twav4=t_wav4(x3,a_twav4,d_twav4,t_twav4,li7,aa3,bb3,cc3)
    


    #12th call
    x5=np.zeros(600)
    c=4.5
    for i in range(aa5,bb5,cc5):
        x5[i]=c
        c=c+0.01
    
    twav7=t_wav7(x5,a_twav7,d_twav7,t_twav7,li8,aa5,bb5,cc5)


    #13th call
    x5=np.zeros(600)
    c=4.5
    for i in range(aa5,bb5,cc5):
        x5[i]=c
        c=c+0.01
    
    swav3=s_wav3(x5,a_swav3,d_swav3,t_swav3,li8,aa5,bb5,cc5)

    #ECG OUTPUT###################################################################################################

    
    #ecg 1 
    #ecg1=y+twav5+swav5
    ecg1=np.zeros(600)
    aa1=0
    bb1=100
    cc1=1
    for i in range(aa1,bb1,cc1):
        ecg1[i]=y[i]+twav5[i]+swav5[i]

    #ecg 2
    #ecg2=d+g
    ecg2=np.zeros(600)
    for i in range(aa2,bb2,cc2):
        ecg2[i]=d[i]+g[i]
    
    #ecg 3
    #ecg3=y2
    ecg3=np.zeros(600)
    for i in range(aa3,bb3,cc3):
        ecg3[i]=y2[i]

    #ecg 4
    #ecg4=d2+g2+swav3+twav7
    ecg4=np.zeros(600)
    for i in range(aa4,bb4,cc4):
        ecg4[i]=d2[i]+g2[i]+swav3[i]+twav7[i]

    #ecg 5
    #ecg5=d9+twav4+swav
    ecg5=np.zeros(600)
    for i in range(aa5,bb5,cc5):
        ecg5[i]=d9[i]+twav4[i]+swav[i]

    
    
    #########################################################################
    #   slicing
    #########################################################################
    #ECG1=ecg1
    ##
    #3
    ##

  
    #XX1=np.arange(3.88,6+0.01,0.01)
    ECG1=np.zeros(100, dtype = float)    #100-111
    for i in range(0,100,1):
    
        ECG1[i]=ecg1[i]




    
    #XX1=np.arange(3.88,6+0.01,0.01)
    ECG2=np.zeros(13, dtype = float)    #100-111
    for i in range(100,111,1):
    
        ECG2[i-100]=ecg2[i]


    
    #XX1=np.arange(3.88,6+0.01,0.01)
    ECG3=np.zeros(280, dtype = float)   #111-390
    for i in range(111,390,1):
    
        ECG3[i-111]=ecg3[i]

    
    #XX1=np.arange(3.88,6+0.01,0.01)
    ECG4=np.zeros(62, dtype = float)    #390-451
    for i in range(390,451,1):
    
        ECG4[i-390]=ecg4[i]

    
    #XX1=np.arange(3.88,6+0.01,0.01)
    ECG5=np.zeros(150, dtype = float)    #451-600
    for i in range(451,600,1):
    
        ECG5[i-451]=ecg5[i]



    a1=np.arange(0.01,1+0.01,0.01)
    a2=np.arange(1,1.11+0.01,0.01)
    a3=np.arange(1.11,3.9+0.01,0.01)
    a4=np.arange(3.9,4.51+0.01,0.01)
    a5=np.arange(4.51,6+0.01,0.01)

    #changing y axis scaling

    '''axes = plt.gca()
    #axes.set_xlim([xmin,xmax])
    ymin=-3
    ymax=4
    axes.set_ylim([ymin,ymax])'''

    '''plt.plot(a1,ECG1,color="blue")
    plt.plot(a2,ECG2,color="blue")
    plt.plot(a3,ECG3,
    color="blue")
    plt.plot(a4,ECG4,color="blue")
    plt.plot(a5,ECG5,color="blue")'''
    a=np.arange(0.01,6+0.01,0.01)
    plt.plot(a,ecg1,color="blue")
    plt.plot(a,ecg2,color="blue")
    plt.plot(a,ecg3,color="blue")
    plt.plot(a,ecg4,color="blue")
    plt.plot(a,ecg5,color="blue")
    

    plt.title('Ventricular Fibrilation')
    plt.xlabel('time (in seconds)')
    plt.ylabel('Volts(mV)')
    plt.show()

    print()
    '''print(aa1)
    print(bb1)
    print(cc1)
    print(aa2)
    print(bb2)
    print(cc2)
    print(aa3)
    print(bb3)
    print(cc3)
    print(aa4)
    print(bb4)
    print(cc4)
    print(aa5)
    print(bb5)
    print(cc5)'''
   

main()