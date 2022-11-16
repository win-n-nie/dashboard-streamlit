import pandas as pd
import streamlit as st

screen_df = pd.read_csv('https://raw.githubusercontent.com/win-n-nie/dashboard-streamlit/main/ScreenTime.csv')
phone_df = pd.read_csv('')
### this is a header
st.header("Group Project Data")
st.caption("visual representation of data")

### to display 
if st.checkbox('Show Screen Time'):
    st.table(screen_df)

if st.checkbox('Show Telephone Data'):
    st.table(phone_df)

## barchart
st.subheader("Screen Time Data")
screen_bat_tot = screen_df['battery_level'].value_counts()
st.bar_chart(screen_bat_tot)
st.caption("A representation of phones battery level ") 

## line chart
st.subheader('Visual of Call type')
call_type = phone_df['type']
st.line_chart(call_type)
st.caption(" a representation of the types of calls made daily")


### code block
code = '''def assignment():
    print("This was done as a class assigment utilizing Streamlit")'''
st.code(code, language='python')