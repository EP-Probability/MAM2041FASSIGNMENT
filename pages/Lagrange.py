import math
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt 

st.title('Welcome to the Lagrange interpolation section!')

x = np.array([2, 6, 10, 14, 18, 22, 26, 30])
n=len(x)
y = np.array([2.585, 2.869, 4.073, 5.480, 5.874, 5.401, 5.427, 6.788])
xap = np.linspace(0,30,100)

def L(x1):
    y1=0
    for k in range(n):
        l=1
        for i in range(n):
            if i!=k:
                l=l*((x1-x[i])/(x[k]-x[i]))
        y1 += l*y[k]
    return y1

yap=L(xap)

if st.button('Press here to interpolate the values for part 1 question 1'):
    st.write("In this section we were asked to interpolate a specific set of data using a lagrange interpolating polynomial. I used two methods to display the graph of the interpolating polynomial, I present an animated version as well as a static version with the given data points present. The actual code for the Lagrange interpolation I believe is standard.")
    st.write('Press the white button to display an animation on how the Lagrange interpolation plots our values')
    fig = go.Figure(
        data=[
            go.Scatter(x=x,y=y,mode='lines',name='Given Data', marker=dict(color='red', size=10))
            ],
        layout=go.Layout(
            xaxis=dict(range=[2,31]),
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
 
    st.write('This is a static version of the data points and the seventh degree polynomial that fits them')
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Given Data'))
    fig.add_trace(go.Scatter(x=xap, y=L(xap), mode='lines', name='Lagrange Interpolated Curve'))
    st.plotly_chart(fig, use_container_width=True)

    
