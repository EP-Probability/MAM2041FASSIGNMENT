import math
import numpy as np
import streamlit as st
import plotly.graph_objects as go

st.title("Welcome to the Root Finding section")

x=np.linspace(0,30,100)
a=14
b=21
m=(a+b)/2
error=10**(-10)
n = int(np.log2((b-a)/error))
count3=0
def f(x1):
    y=(1)/(3*np.log(x1))-0.1*np.cos(0.1*x1)-0.3*np.cos(0.3*x1)
    return y

if st.button("Question 1. Press this to display the position of the local maximum of f(x) using the bisection method"):
    st.write("Here we display the bisection method to find the maximum value of f(x) near x=17. The code hosted nothing unique, we just display all the values as well as the step we are at, then a final message stating the results of the bisection method.")
    while (b-a)/2>=error:
        m=(a+b)/2
        count3+=1
        st.write("Step",count3,":",m)
        if f(m)>0:
            a=m
        elif f(m)<0:
            b=m
        else:
            a=b=m
    st.write("As we can see the final approximated value for the position of the local maximum of f(x) is, x = ",m,".This value was obatined using the bisection method with tolerance",error,"which resulted in",n,"steps")
            
phi = (1+math.sqrt(5))/2
xa=15
xb=16
xc=xb-f(xb)*((xa-xb)/(f(xa)-f(xb)))
error1=10**(-10)
count=0

if st.button("Question 2. Press this to display the position of the local maximum of f(x) using the secant method"):
    st.write("We apply essentially the same code skeleton as the bisection method section, results and steps, then our final results all stated at the end. Though as we will see, the secant method is significantly faster and computationally cheaper.")
    while np.abs(xa-xb)>=error1:
        xc=xb-f(xb)*((xa-xb)/(f(xa)-f(xb)))
        xb,xa=xc,xb
        count += 1
        st.write("Step",count,":",xc)
        
    st.write("As we can see the final approximated value for the position of the local maximum of f(x) is x =",xc,".This value was obtained with the secant method and with a tolerance of,",error1,"which resulted in",count,"steps")
    
if st.button("Question 2. Press this to view the review of the two methods to find the maximum of f(x)"):
    st.write("As we can see the secant method is significantly faster than the bisection method, since the bisection method has an order of convergence of p=",phi,"and the bisection method has an order of onvergence of p=",1,".We can also see with the tolerance of",error,"for the bisetion method we converge to the x value for the maximum value of f(x) in",n,"steps, whereas with the secant method with tolerance",error1,"we converge to the x value for the maximum value of f(x) in",6,"steps.")

x3=21
x4=19
x5=x4-f(x4)*((x3-x4)/(f(x3)-f(x4)))
x6=21
x7=22
x8=x7-f(x7)*((x6-x7)/(f(x6)-f(x7)))
count1=0
count2=0
if st.button("Question 3. Press this to display the secant method for x0=21 and x1=19,22"):
    st.write("Here we view the secant method but using two different intial conditions. We plot both versions and one converges to our previous root near x=17 and the other converges to a root near x=24. we then discuss this reult as well as display f'(x) as a graph to view it and show that infact there are two roots on the interval [10,30].")
    while np.abs(x3-x4)>=error1:
        x5=x4-f(x4)*((x3-x4)/(f(x3)-f(x4)))
        x4,x3=x5,x4
        count1+=1
        st.write("Step",count1,":",x5)
        
    st.write("As we can see the secant method for initial values x0=21 and x1=19 results in converging to the x value with tolerance,",error1,", in ",count1,"steps")

    while np.abs(x6-x7)>=error1:
        x8=x7-f(x7)*((x6-x7)/(f(x6)-f(x7)))
        x7,x6=x8,x7
        count2+=1
        st.write("Step",count2,":",x8)
    a=[x5,x8]
    b=[f(x5),f(x8)]
    st.write("As we can see the secant method with intial values x0=21 and x1=22, which interestingly converges to a different value x=",x8,"with tolerance,",error1,",in",count2,"steps.")
    st.write("Now we'd like to answer the question of the different value that we converged to, x=",x8,".As we can see from the plot of the graph of f'(x), it has two roots on the interval [10,30], we use the approximated values x=",x5,"and x=",x8,"as the roots of f'(x). Now it becomes obvious why we obtained x=",x8,"when we used the intial conditions x0=",21,"and x1=",22,"since these values caused the secant method to converge to the root x=",x8,".Due to the next value being x2=",27.479201712010155,"it caused the secant method to zero in on the root near x=",24,".Which means we can say that f(x) has a maximum value near x=",24,".")
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=a,y=b,mode='markers'))
    fig.add_trace(go.Scatter(x=x,y=f(x),mode='lines'))
    st.plotly_chart(fig,use_container_width=True)

if st.button("Question 4. Press this to discuss the comparison of the secant method and bisection method in reliability and setup."):
    st.write("As we have seen the secant method and bisection method both gave us our desired root around x=17. Though setting up the secant method was a lot simpler than setting up the bisection method, due to the secant method being a simple reursive function compared to the bisection method requiring if statements. The bisection method is highly relaible since as long as the root exists in the given interval we will converge to the root, though the main downside is that it does take significantly longer than other root finding methods. The secant method is much better due to it being significantly faster, it is also reliable although if f(x0)=f(x1) we obtain a division by zero which is obviously unwanted.")
