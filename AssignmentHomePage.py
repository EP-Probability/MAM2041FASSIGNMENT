import streamlit as st

st.title('Welcome to the homepage of the MAM2041F Assignment by HRTJOS011')

st.write("In this assignment we will be taking a look at in part one, the Lagrange interpolating polynomial as well as Divided differences and Newton's form. Then in part two we take a look at the bisection method and secant method view their results and comapre them.")
st.write("I did not use AI at all for this assignment as I believe the use of AI not made by you and not hosted on your hardware is unethical.")

col1,col2,col3 = st.columns(3)

with col1:
    if st.button('press here to begin part 1 question 1. Lagrange Interpolation'):
        st.switch_page('pages/Lagrange.py')

with col2:
    if st.button("Press here to begin part 1 question 2. Divided Differences and Newton's form"):
        st.switch_page('pages/DividedDifferences.py')

with col3:
    if st.button("Press here to begin part 2. Root Finding"):
        st.switch_page('pages/RootFinding.py')

