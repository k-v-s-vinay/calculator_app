import streamlit as st
st.title('Calculator Application')
st.write('Hello')
num1 = st.number_input('Insert number a :',placeholder='Enter a first number')
num2 = st.number_input('Insert number b :',placeholder='Enter a second number')
operation = st.selectbox('Select the operation',('Addition','Subtraction','Division','Multiplication'))
res = st.button('Calculate')
if res:
    if operation =='Addition':
        st.write(num1+num2)
    elif operation == 'Subtraction':
        st.write(num1-num2)
    elif operation == 'Division':
        if num2 != 0:
            st.write(num1/num2)
    elif operation == 'Multiplication':
        st.write(num1*num2)
    # st.write('button is clicked')
    # st.balloons()