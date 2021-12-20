import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('dark_background')

############################################################################################################################################
#part 1 - 0.01 to 1.55
############################################################################################################################################
#pwav
def p_wav1(x,a_pwav,d_pwav,t_pwav,li):
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
        for i in range(0,152,1):
            harm1[i] = (((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            
            p2[i]=p2[i]+harm1[i]
        #print(type(p2))
    #print(p2)
    pwav=p2.copy()
    pwav=pwav*a
    return pwav

#qwav
def q_wav1(x,a_qwav,d_qwav,t_qwav,li):
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
        for i in range(0,152,1):
            harm5[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            q2[i]=q2[i]+harm5[i]
            
            
        #print(type(p2))

    qwav=q2.copy()
    qwav=qwav*(-1)
    return qwav

#qrs
def qrs_wav1(x,a_qrswav,d_qrswav,t_qrswav,li):
    l=li
    for i in range(len(x)):
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
        for i in range(0,152,1):       
            harm[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            qrs2[i]=qrs2[i]+harm[i]


    
    qrswav=qrs2.copy()
    #qrswav=[(qrs1+x+1) for x in qrswav]
    for i in range(0,152,1):
        qrswav[i]=qrswav[i] + 0.09
    return qrswav

#swav
def s_wav1(x,a_swav,d_swav,t_swav,li):
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
        for i in range(0,152,1):       
            
            harm3[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            s2[i]=s2[i]+harm3[i]


    #swav=-1*(s2)

    swav=s2.copy()
    swav=swav*(-1)
    return swav

#twav
def t_wav1(x,a_twav,d_twav,t_twav,li):
    l=li
    a=a_twav

    for i in range(len(x)):
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
        for i in range(0,152,1):
            
            harm2[i]=(((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            t2[i]=t2[i]+harm2[i]


    twav=t2.copy()
    twav=twav*a
    #twav1=t2
    #twav=a*twav1
    return twav


############################################################################################################################################
#part 2 - 1.52 to 2.2 
############################################################################################################################################

def p_wav2(x,a_pwav,d_pwav,t_pwav,li):
    l=li
    a=a_pwav

    for i in range(152,220,1):
        x[i]=x[i]+t_pwav-0.035

    b=(2*l)/d_pwav
    n=100
    p1=1/l

    p2=np.zeros(600)
    
    harm1=np.zeros(600)

    for j in range(n+1):
        for i in range(152,220,1):
            harm1[i] = (((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            
            p2[i]=p2[i]+harm1[i]
        #print(type(p2))
    #print(p2)
    pwav=p2.copy()
    pwav=pwav*a
    return pwav

def p_wav22(x,a_pwav2,d_pwav2,t_pwav2,li):
    l=li
    a=a_pwav2

    for i in range(152,220,1):
        x[i]=x[i]+t_pwav2-0.035

    b=(2*l)/d_pwav2
    n=100
    p1=1/l

    p2=np.zeros(len(x))
    
    harm1=np.zeros(len(x))

    for j in range(n+1):
        for i in range(152,220,1):
            harm1[i] = (((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            
            p2[i]=p2[i]+harm1[i]
        #print(type(p2))
    #print(p2)
    pwav=p2.copy()
    pwav=pwav*a
    return pwav
#qwav
def q_wav2(x,a_qwav,d_qwav,t_qwav,li):
    l=li
    for i in range(152,220,1):
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
        for i in range(152,220,1):
            harm5[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            q2[i]=q2[i]+harm5[i]
            
            
        #print(type(p2))

    qwav=q2.copy()
    qwav=qwav*(-1)
    return qwav

#qrs
def qrs_wav2(x,a_qrswav,d_qrswav,t_qrswav,li):
    l=li
    for i in range(152,220,1):
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
        for i in range(152,220,1):       
            harm[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            qrs2[i]=qrs2[i]+harm[i]


    
    qrswav=qrs2.copy()
    #qrswav=[(qrs1+x+1) for x in qrswav]
    for i in range(152,220,1):
        qrswav[i]=qrswav[i] + 0.09
    return qrswav

#swav
def s_wav2(x,a_swav,d_swav,t_swav,li):
    l=li  
    
    for i in range(152,220,1):
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
        for i in range(152,220,1):       
            
            harm3[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            s2[i]=s2[i]+harm3[i]


    #swav=-1*(s2)

    swav=s2.copy()
    swav=swav*(-1)
    return swav

#twav
def t_wav2(x,a_twav,d_twav,t_twav,li):
    l=li
    a=a_twav

    for i in range(152,220,1):
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
        for i in range(152,220,1):
            
            harm2[i]=(((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            t2[i]=t2[i]+harm2[i]


    twav=t2.copy()
    twav=twav*a
    #twav1=t2
    #twav=a*twav1
    return twav

#############################################################################################################################################
#part 3 - 2.2 to 4.58
#############################################################################################################################################
def p_wav3(x,a_pwav,d_pwav,t_pwav,li):
    l=li
    a=a_pwav

    for i in range(220,458,1):
        x[i]=x[i]+t_pwav-0.035

    b=(2*l)/d_pwav
    n=100
    p1=1/l

    p2=np.zeros(600)
    
    harm1=np.zeros(600)

    for j in range(n+1):
        for i in range(220,458,1):
            harm1[i] = (((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            
            p2[i]=p2[i]+harm1[i]
        #print(type(p2))
    #print(p2)
    pwav=p2.copy()
    pwav=pwav*a
    return pwav


#qwav
def q_wav3(x,a_qwav,d_qwav,t_qwav,li):
    l=li
    for i in range(220,458,1):
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
        for i in range(220,458,1):
            harm5[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            q2[i]=q2[i]+harm5[i]
            
            
        #print(type(p2))

    qwav=q2.copy()
    qwav=qwav*(-1)
    return qwav

#qrs
def qrs_wav3(x,a_qrswav,d_qrswav,t_qrswav,li):
    l=li
    for i in range(220,458,1):
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
        for i in range(220,458,1):       
            harm[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            qrs2[i]=qrs2[i]+harm[i]


    
    qrswav=qrs2.copy()
    #qrswav=[(qrs1+x+1) for x in qrswav]
    for i in range(220,458,1):
        qrswav[i]=qrswav[i] + 0.09
    return qrswav

#swav
def s_wav3(x,a_swav,d_swav,t_swav,li):
    l=li  
    
    for i in range(220,458,1):
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
        for i in range(220,458,1):       
            
            harm3[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            s2[i]=s2[i]+harm3[i]


    #swav=-1*(s2)

    swav=s2.copy()
    swav=swav*(-1)
    return swav

#twav
def t_wav3(x,a_twav,d_twav,t_twav,li):
    l=li
    a=a_twav

    for i in range(220,458,1):
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
        for i in range(220,458,1):
            
            harm2[i]=(((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            t2[i]=t2[i]+harm2[i]


    twav=t2.copy()
    twav=twav*a
    #twav1=t2
    #twav=a*twav1
    return twav
#############################################################################################################################################
#part 4- 4.578 to 5.3
#############################################################################################################################################
def p_wav4(x,a_pwav,d_pwav,t_pwav,li):
    l=li
    a=a_pwav

    for i in range(458,530,1):
        x[i]=x[i]+t_pwav-0.035

    b=(2*l)/d_pwav
    n=100
    p1=1/l

    p2=np.zeros(600)
    
    harm1=np.zeros(600)

    for j in range(n+1):
        for i in range(458,530,1):
            harm1[i] = (((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            
            p2[i]=p2[i]+harm1[i]
        #print(type(p2))
    #print(p2)
    pwav=p2.copy()
    pwav=pwav*a
    return pwav

def p_wav44(x,a_pwav2,d_pwav2,t_pwav2,li):
    l=li
    a=a_pwav2

    for i in range(458,530,1):
        x[i]=x[i]+t_pwav2-0.035

    b=(2*l)/d_pwav2
    n=100
    p1=1/l

    p2=np.zeros(len(x))
    
    harm1=np.zeros(len(x))

    for j in range(n+1):
        for i in range(458,530,1):
            harm1[i] = (((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            
            p2[i]=p2[i]+harm1[i]
        #print(type(p2))
    #print(p2)
    pwav=p2.copy()
    pwav=pwav*a
    return pwav
#qwav
def q_wav4(x,a_qwav,d_qwav,t_qwav,li):
    l=li
    for i in range(458,530,1):
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
        for i in range(458,530,1):
            harm5[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            q2[i]=q2[i]+harm5[i]
            
            
        #print(type(p2))

    qwav=q2.copy()
    qwav=qwav*(-1)
    return qwav

#qrs
def qrs_wav4(x,a_qrswav,d_qrswav,t_qrswav,li):
    l=li
    for i in range(458,530,1):
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
        for i in range(458,530,1):       
            harm[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            qrs2[i]=qrs2[i]+harm[i]


    
    qrswav=qrs2.copy()
    #qrswav=[(qrs1+x+1) for x in qrswav]
    for i in range(458,530,1):
        qrswav[i]=qrswav[i] + 0.09
    return qrswav

#swav
def s_wav4(x,a_swav,d_swav,t_swav,li):
    l=li  
    
    for i in range(458,530,1):
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
        for i in range(458,530,1):       
            
            harm3[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            s2[i]=s2[i]+harm3[i]


    #swav=-1*(s2)

    swav=s2.copy()
    swav=swav*(-1)
    return swav

#twav
def t_wav4(x,a_twav,d_twav,t_twav,li):
    l=li
    a=a_twav

    for i in range(458,530,1):
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
        for i in range(458,530,1):
            
            harm2[i]=(((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            t2[i]=t2[i]+harm2[i]


    twav=t2.copy()
    twav=twav*a
    #twav1=t2
    #twav=a*twav1
    return twav

#############################################################################################################################################
#part 5 - 5.3 to 6
#############################################################################################################################################
def p_wav5(x,a_pwav,d_pwav,t_pwav,li):
    l=li
    a=a_pwav

    for i in range(530,600,1):
        x[i]=x[i]+t_pwav-0.035

    b=(2*l)/d_pwav
    n=100
    p1=1/l

    p2=np.zeros(600)
    
    harm1=np.zeros(600)

    for j in range(n+1):
        for i in range(530,600,1):
            harm1[i] = (((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            
            p2[i]=p2[i]+harm1[i]
        #print(type(p2))
    #print(p2)
    pwav=p2.copy()
    pwav=pwav*a
    return pwav


#qwav
def q_wav5(x,a_qwav,d_qwav,t_qwav,li):
    l=li
    for i in range(530,600,1):
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
        for i in range(530,600,1):
            harm5[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            q2[i]=q2[i]+harm5[i]
            
            
        #print(type(p2))

    qwav=q2.copy()
    qwav=qwav*(-1)
    return qwav

#qrs
def qrs_wav5(x,a_qrswav,d_qrswav,t_qrswav,li):
    l=li
    for i in range(530,600,1):
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
        for i in range(530,600,1):       
            harm[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            qrs2[i]=qrs2[i]+harm[i]


    
    qrswav=qrs2.copy()
    #qrswav=[(qrs1+x+1) for x in qrswav]
    for i in range(530,600,1):
        qrswav[i]=qrswav[i] + 0.09
    return qrswav

#swav
def s_wav5(x,a_swav,d_swav,t_swav,li):
    l=li  
    
    for i in range(530,600,1):
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
        for i in range(530,600,1):       
            
            harm3[i]=(((2*b*a)/((j+1)*(j+1)*math.pi*math.pi))*(1-math.cos(((j+1)*math.pi)/b)))*math.cos(((j+1)*math.pi*x[i])/l)
            s2[i]=s2[i]+harm3[i]


    #swav=-1*(s2)

    swav=s2.copy()
    swav=swav*(-1)
    return swav

#twav
def t_wav5(x,a_twav,d_twav,t_twav,li):
    l=li
    a=a_twav

    for i in range(530,600,1):
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
        for i in range(530,600,1):
            
            harm2[i]=(((math.sin((math.pi/(2*b))*(b-(2*(j+1)))))/(b-(2*(j+1)))+(math.sin((math.pi/(2*b))*(b+(2*(j+1)))))/(b+(2*(j+1))))*(2/math.pi))*math.cos(((j+1)*math.pi*x[i])/l)
            t2[i]=t2[i]+harm2[i]


    twav=t2.copy()
    twav=twav*a
    #twav1=t2
    #twav=a*twav1
    return twav

#############################################################################################################################################
#main part 1
#############################################################################################################################################
x=np.arange(0.01,1.52+0.01,0.01)
#print (a)
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

#pwav output
x1=np.arange(0.01,1.52+0.01,0.01)
#print(x1)
pwav1=p_wav1(x1,a_pwav,d_pwav,t_pwav,li)

#qwav output
x2=np.arange(0.01,1.52+0.01,0.01)
#print(x2)
qwav1=q_wav1(x2,a_qwav,d_qwav,t_qwav,li)

#qrswav output
x3=np.arange(0.01,1.52+0.01,0.01)
#print(x3)
qrswav1=qrs_wav1(x3,a_qrswav,d_qrswav,t_qrswav,li)

#swav output
x4=np.arange(0.01,1.52+0.01,0.01)
#print(x4)
swav1=s_wav1(x4,a_swav,d_swav,t_swav,li)

#twav output
x5=np.arange(0.01,1.52+0.01,0.01)
#print(x5)
twav1=t_wav1(x5,a_twav,d_twav,t_twav,li)

#ecg1 output
ecg1=np.zeros(len(x))

for i in range(0,152,1):
    ecg1[i]=pwav1[i]+qwav1[i]+qrswav1[i]+twav1[i]+swav1[i]-0.00624427

a=np.arange(0.01,1.52+0.01,0.01)


#print(len(x))
#plt.plot(a,ecg1)

#############################################################################################################################################
#main part 2
#############################################################################################################################################
li=30/72
a_pwav=0.25
d_pwav=0.10
t_pwav=0.2+0.38+0.4  

a_pwav2=0.3
d_pwav2=0.05
t_pwav2=0.2+0.38+0.4

a_qwav=0.4
d_qwav=0.06
t_qwav=0.07+0.38+0.4

a_qrswav=2.1
d_qrswav=0.05
t_qrswav=0.38+0.4


a_swav=0.6
d_swav=0.06
t_swav=0.065-0.38-0.4

a_twav=0.35
d_twav=0.14
t_twav=0.2-0.38-0.4

#pwav2
xx1=np.zeros(600)
c=1.52
for i in range(152,220,1):
  xx1[i]=c
  c=c+0.01
pwav2=p_wav2(xx1,a_pwav,d_pwav,t_pwav,li)

#pwav22
xx22=np.zeros(600)
dd=1.52
for i in range(152,220,1):
  xx22[i]=dd
  dd=dd+0.01
pwav22=p_wav22(xx22,a_pwav2,d_pwav2,t_pwav2,li)

#qwav2
xx2=np.zeros(600)
d=1.52
for i in range(152,220,1):
  xx2[i]=d
  d=d+0.01
qwav2=q_wav2(xx2,a_qwav,d_qwav,t_qwav,li)

#qrswav2
xx3=np.zeros(600)
e=1.52
for i in range(152,220,1):
  xx3[i]=e
  e=e+0.01
qrswav2=qrs_wav2(xx3,a_qrswav,d_qrswav,t_qrswav,li)

#swav2
xx4=np.zeros(600)
f=1.52
for i in range(152,220,1):
  xx4[i]=f
  f=f+0.01
swav2=s_wav2(xx4,a_swav,d_swav,t_swav,li)

#twav2
xx5=np.zeros(600)
g=1.52
for i in range(152,220,1):
  xx5[i]=g
  g=g+0.01
twav2=t_wav2(xx5,a_twav,d_twav,t_twav,li)

#ecg2 output
ecg2=np.zeros(600)

for i in range(152,220,1):
    ecg2[i]=pwav2[i]+pwav22[i]+qwav2[i]+qrswav2[i]+twav2[i]+swav2[i]+0.0051

######################################################################################
#main part 3
######################################################################################

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

#qwav3
xxx1=np.zeros(600)
c=2.2
for i in range(220,458,1):
  xxx1[i]=c
  c=c+0.01
pwav3=p_wav3(xxx1,a_pwav,d_pwav,t_pwav,li)


#qwav2
xxx2=np.zeros(600)
d=2.2
for i in range(220,458,1):
  xxx2[i]=d
  d=d+0.01
qwav3=q_wav3(xxx2,a_qwav,d_qwav,t_qwav,li)

#qrswav2
xxx3=np.zeros(600)
e=2.2
for i in range(220,458,1):
  xxx3[i]=e
  e=e+0.01
qrswav3=qrs_wav3(xxx3,a_qrswav,d_qrswav,t_qrswav,li)

#swav2
xxx4=np.zeros(600)
f=2.2
for i in range(220,458,1):
  xxx4[i]=f
  f=f+0.01
swav3=s_wav3(xxx4,a_swav,d_swav,t_swav,li)

#twav2
xxx5=np.zeros(600)
g=2.2
for i in range(220,458,1):
  xxx5[i]=g
  g=g+0.01
twav3=t_wav3(xxx5,a_twav,d_twav,t_twav,li)

ecg3=np.zeros(600)

for i in range(220,458,1):
    ecg3[i]=pwav3[i]+qwav3[i]+qrswav3[i]+twav3[i]+swav3[i]-0.00645

######################################################################################
#main part 4
######################################################################################
li=30/72
a_pwav=0.25
d_pwav=0.10
t_pwav=0.2-0.2+0.25+1

a_pwav2=0.3
d_pwav2=0.05
t_pwav2=0.2-0.2+0.25+1

a_qwav=0.4
d_qwav=0.06
t_qwav=0.07-0.2+0.25+1

a_qrswav=2.1
d_qrswav=0.05
t_qrswav=-0.20+0.25+1


a_swav=0.6
d_swav=0.06
t_swav=0.065+0.20-0.25-1

a_twav=0.35
d_twav=0.14
t_twav=0.2+0.2-0.25-1

#pwav4
xxxx1=np.zeros(600)
c=4.578
for i in range(458,530,1):
  xxxx1[i]=c
  c=c+0.01
pwav4=p_wav4(xxxx1,a_pwav,d_pwav,t_pwav,li)

#pwav44
xxxx22=np.zeros(600)
dd=4.578
for i in range(458,530,1):
  xxxx22[i]=dd
  dd=dd+0.01
pwav44=p_wav44(xxxx22,a_pwav2,d_pwav2,t_pwav2,li)

#qwav4
xxxx2=np.zeros(600)
d=4.578
for i in range(458,530,1):
  xxxx2[i]=d
  d=d+0.01
qwav4=q_wav4(xxxx2,a_qwav,d_qwav,t_qwav,li)

#qrswav4
xxxx3=np.zeros(600)
e=4.578
for i in range(458,530,1):
  xxxx3[i]=e
  e=e+0.01
qrswav4=qrs_wav4(xxxx3,a_qrswav,d_qrswav,t_qrswav,li)

#swav4
xxxx4=np.zeros(600)
f=4.578
for i in range(458,530,1):
  xxxx4[i]=f
  f=f+0.01
swav4=s_wav4(xxxx4,a_swav,d_swav,t_swav,li)

#twav4
xxxx5=np.zeros(600)
g=4.578
for i in range(458,530,1):
  xxxx5[i]=g
  g=g+0.01
twav4=t_wav4(xxxx5,a_twav,d_twav,t_twav,li)

#ecg4 output
ecg4=np.zeros(600)

for i in range(458,530,1):
    ecg4[i]=pwav4[i]+pwav44[i]+qwav4[i]+qrswav4[i]+twav4[i]+swav4[i]+0.0046

######################################################################################
#main part 5
######################################################################################
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

#pwav5
xxxxx1=np.zeros(600)
c=5.3
for i in range(530,600,1):
  xxxxx1[i]=c
  c=c+0.01
pwav5=p_wav5(xxxxx1,a_pwav,d_pwav,t_pwav,li)


#qwav5
xxxxx2=np.zeros(600)
d=5.3
for i in range(530,600,1):
  xxxxx2[i]=d
  d=d+0.01
qwav5=q_wav5(xxxxx2,a_qwav,d_qwav,t_qwav,li)

#qrswav5
xxxxx3=np.zeros(600)
e=5.3
for i in range(530,600,1):
  xxxxx3[i]=e
  e=e+0.01
qrswav5=qrs_wav5(xxxxx3,a_qrswav,d_qrswav,t_qrswav,li)

#swav5
xxxxx4=np.zeros(600)
f=5.3
for i in range(530,600,1):
  xxxxx4[i]=f
  f=f+0.01
swav5=s_wav5(xxxxx4,a_swav,d_swav,t_swav,li)

#twav5
xxxxx5=np.zeros(600)
g=5.3
for i in range(530,600,1):
  xxxxx5[i]=g
  g=g+0.01
twav5=t_wav5(xxxxx5,a_twav,d_twav,t_twav,li)

ecg5=np.zeros(600)

for i in range(530,600,1):
    ecg5[i]=pwav5[i]+qwav5[i]+qrswav5[i]+twav5[i]+swav5[i]-0.00627

######################################################################################
#final cuts
######################################################################################
#ECG1 final cut
XX1=np.arange(0.01,1.52+0.01,0.01)   #changed fro 6.00 to 1.98
ECG1=np.zeros(152, dtype = float)
for i in range(0,152,1):
    ECG1[i]=ecg1[i]


#ECG2 final cut
XX2=np.arange(1.52,2.2+0.01,0.01)
ECG2=np.zeros(69, dtype = float)
for i in range(152,220,1):
    if i>=152:
        ECG2[i-220]=ecg2[i]

#ECG3 final cut
XX3=np.arange(2.2,4.58+0.01,0.01)
ECG3=np.zeros(239, dtype = float)
for i in range(220,458,1):
    if i>=220:
        ECG3[i-220]=ecg3[i]

#ECG4 final cut
XX4=np.arange(4.578,5.3+0.01,0.01)
ECG4=np.zeros(74, dtype = float)
for i in range(458,530,1):
    if i>=458:
        ECG4[i-458]=ecg4[i]

#ECG5 final cut
XX5=np.arange(5.3,6.0+0.01,0.01)
ECG5=np.zeros(71, dtype = float)
for i in range(530,600,1):
    if i>=530:
        ECG5[i-530]=ecg5[i]

axes = plt.gca()
#axes.set_xlim([xmin,xmax])
ymin=-3
ymax=4
axes.set_ylim([ymin,ymax])

plt.plot(XX1,ECG1,color="#04ed00")        
plt.plot(XX2,ECG2,color="#04ed00")
plt.plot(XX3,ECG3,color="#04ed00")
plt.plot(XX4,ECG4,color="#04ed00")
plt.plot(XX5,ECG5,color="#04ed00")

ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
ax.axis("off")

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()
#plot(x,ecg)
