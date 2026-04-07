import math 
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.title('Welcome to the divided differences section!')

x = np.array([2, 6, 10, 14, 18, 22, 26, 30])
n=len(x)
y = np.array([2.585, 2.869, 4.073, 5.480, 5.874, 5.401, 5.427, 6.788])
xap = np.linspace(0,30,100)
a1 = np.zeros(n)
a2 = np.zeros(len(a1))
a3 = np.zeros(len(a2))
a4 = np.zeros(len(a3))
a5 = np.zeros(len(a4))
a6 = np.zeros(len(a5))
a7 = np.zeros(len(a6))

for i in range(n-1):
    a1[i]=(y[i+1]-y[i])/(x[i+1]-x[i])
for i in range(len(a1)-2):
    a2[i]=(a1[i+1]-a1[i])/(x[i+2]-x[i])
for i in range(len(a2)-3):
    a3[i]=(a2[i+1]-a2[i])/(x[i+3]-x[i])
for i in range(len(a3)-4):
    a4[i]=(a3[i+1]-a3[i])/(x[i+4]-x[i])
for i in range(len(a4)-5):
    a5[i]=(a4[i+1]-a4[i])/(x[i+5]-x[i])
for i in range(len(a5)-6):
    a6[i]=(a5[i+1]-a5[i])/(x[i+6]-x[i])
for i in range(len(a6)-7):
    a7[i]=(a6[i+1]-a6[i])/(x[i+7]-x[i])

def D(x1):
    p = y[0]+(x1-x[0])*a1[0]+(x1-x[0])*(x1-x[1])*a2[0]+(x1-x[0])*(x1-x[1])*(x1-x[2])*a3[0]+(x1-x[0])*(x1-x[1])*(x1-x[2])*(x1-x[3])*a4[0]+(x1-x[0])*(x1-x[1])*(x1-x[2])*(x1-x[3])*(x1-x[4])*a5[0]+(x1-x[0])*(x1-x[1])*(x1-x[2])*(x1-x[3])*(x1-x[4])*(x1-x[5])*a6[0]+(x1-x[0])*(x1-x[1])*(x1-x[2])*(x1-x[3])*(x1-x[4])*(x1-x[5])*(x1-x[6])*a7[0]
    return p

def L(x1):
    y1=0
    for k in range(n):
        l=1
        for i in range(n):
            if i!=k:
                l=l*((x1-x[i])/(x[k]-x[i]))
        y1 += l*y[k]
    return y1

yap=D(xap)

if st.button("Press here to calculate Divided differnces and Newton's form for part 1 question 2"):
    st.write("In this section we use the same given data points that we used to interpolate with the Lagrange interpolating polynomial. It took me a while to figure out how to code up the divided differences, I finally formed a method, which I believe is pretty clunky, but it works. I do the same as before and present an animated version of the graph and a static version. I also display a table that contains all the divided differences not just the ones for the Newton's form polynomial. I display a message at the end that will only display if the Lagrange interpolating polynomial and the divided differences and Newton's form polynomial equal obviously using an if statement.")
    st.write('Press the white button to display an animation on how the Lagrange interpolation plots our values')
    fig = go.Figure(
        data=[
            go.Scatter(x=x,y=y,mode='lines',name='Given Data', marker=dict(color='red', size=10))
            ],
        layout=go.Layout(
            xaxis=dict(range=[0,31]),
            yaxis=dict(range=[2,7]),
        updatemenus=[{
                     'type': 'buttons',
                     'buttons':[{
                     'label':'Play',
                     'method':'animate',
                     'args':[None,{'frame':{'duration': 30,'redraw':False,'fromcurrent':True}}]
                         }], 
                     }],
        ),
        frames=[go.Frame(data=[go.Scatter(x=xap[:i],y=yap[:i])])for i in range(0,len(xap))]
        )
    st.plotly_chart(fig,use_container_width=True)
 
    st.write('This is a static version with the data points and the seventh degree polynomial that fits them')
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x,y=y,mode='markers'))
    fig.add_trace(go.Scatter(x=xap,y=D(xap),mode='lines'))
    st.plotly_chart(fig,use_container_width=True)
    st.write('Table representing the values of the divided differences')
    fig = go.Figure(data=[go.Table(header=dict(values=['x','y','D1','D2','D3','D4','D5','D6','D7']),
    cells = dict(values=[[2, 6, 10, 14, 18, 22, 26, 30],[2.585, 2.869, 4.073, 5.480, 5.874, 5.401, 5.427, 6.788],[round(a1[0],7),round(a1[1],7),round(a1[2],7),round(a1[3],7),round(a1[4],7),round(a1[5],7),round(a1[6],7),round(a1[7],7)],[round(a2[0],7),round(a2[1],7),round(a2[2],7),round(a2[3],7),round(a2[4],7),round(a2[5],7),round(a2[6],7)],[round(a3[0],7),round(a3[1],7),round(a3[2],7),round(a3[3],7),round(a3[4],7),round(a3[5],7)],[round(a4[0],7),round(a4[1],7),round(a4[2],7),round(a4[3],7),round(a4[4],7)],[round(a5[0],7),round(a5[1],7),round(a5[2],7),round(a5[3],7)],[round(a6[0],7),round(a6[1],7),round(a6[2],7)],[round(a7[0],10),a7[1]]])
    )])
    st.plotly_chart(fig,use_container_width=True)

    if np.all(L(xap))==np.all(D(xap)):
        st.write("The Lagrange method and Newton's form with divided differences does infact equal, this is proven by the if statement that allowed the display of this text.")
    
