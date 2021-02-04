import streamlit as st
import numpy as np
import pandas as pd
import time

def getResClasses():
    return ['Resclass 1', 'Resclass 2', 'Resclass 3']

def getPropsOfResclass(resClass):
    return [resClass + 'a', resClass + 'b', resClass + 'c']
# st.title('My first app')
# st.write('Hello!')
# df = pd.DataFrame({
#     'first' : [1, 2, 3, 4],
#     'second':[10, 20, 33, 12312]
# })
#
# df
#
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c']
# )
# chart_data
# st.line_chart(chart_data)
# if st.checkbox('Show map?'):
#     map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
#     map_data
#     st.map(map_data)
# option = st.sidebar.selectbox(
#     'Which number do you like best?',
#     df['first'])
#
# 'You selected: ', option
# left_column, right_column = st.beta_columns(2)
# pressed = left_column.button('Press me?')
# if pressed:
#     right_column.write("Woohoo!")
#
# expander = st.beta_expander("FAQ")
# expander.write("Here you could put in some really, really long explanations...")
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    test = pd.read_csv(uploaded_file, sep=";")
    st.write(test)
    res = st.selectbox('Which resource class does this table represent?', getResClasses())
    for col in test.columns:
        st.subheader(col)
        case = st.selectbox('What to do with column ' + col, ['Represents property', 'Represents link to another resource', 'Ignore'], key=col)
        if case == 'Represents property':
            st.selectbox('Choose property', getPropsOfResclass(res), key=col)
        if case == 'Represents link to another resource':
            linkedClass = st.selectbox('Link to which resource', getResClasses()) #TODO: replace with property query, get object via property
            linkType = st.selectbox('How to link?', ['Is an IRI', 'Link via value of a property of the other resource'])
            if linkType == 'Link via value of a property of the other resource':
                st.selectbox('Choose the property of the linked resource class:', getPropsOfResclass(linkedClass))