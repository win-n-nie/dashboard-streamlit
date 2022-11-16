import pandas as pd
import streamlit as st

screen_df = pd.read_csv('/Users/wendyarias/Documents/GitHub/dashboard-streamlit/ScreenTime.csv')
phone_df = pd.read_csv('/Users/wendyarias/Documents/GitHub/dashboard-streamlit/telephony2.csv')
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
code = '''
st.subheader("Screen Time Data")
screen_bat_tot = screen_df['battery_level'].value_counts()
st.bar_chart(screen_bat_tot)
st.caption("A representation of phones battery level ") 
'''
st.code(code, language='python')
st.caption("code used to make barchart")
#pip3 install pipenv
#pip3 install env
#sudo -H pip install -U pipenv in shh do pip install pipenv
#pipenv shell
#pip3 install streamlit
