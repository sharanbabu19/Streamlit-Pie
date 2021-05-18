import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


st.title('Pie Chart')
st.caption("Click on any legend, to remove corresponding slice from the pie.")


# Code example on plotly docs
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries'
fig = px.pie(df, values='pop', names='country', title='Population of European continent')

#print(fig)
st.plotly_chart(fig, use_container_width=True) 


# Chart with sub-chart / Burst chart
st.title("Burst Chart")
st.markdown("1) Try clicking on 'Seth' or 'Awan'")

# Place corresponding labels and their parents in 2 separate listd
# Nested pie chart will be created
fig2 =go.Figure(go.Sunburst(
    labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["",    "Eve", "Eve",  "Seth", "Seth", "Eve",   "Eve", "Awan",   "Eve" ],
    values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
))

fig2.update_layout(margin = dict(t=0, l=0, r=0, b=0))

st.plotly_chart(fig2, use_container_width=True)

# Ex: 2
st.markdown("2) I think this fulfills your needs. A Dataframe is the input for this.")
st.caption("Click on various slices")
colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

df = px.data.tips()
fig4 = px.sunburst(df, path=['day', 'time', 'sex'], values='total_bill')
st.plotly_chart(fig4, use_container_width=True)

st.markdown("""I would recommend using a selectbox to let the user select one of the pie
	and implement further functionalities based on selected slice.
	Something like this""")

st.write("")
st.write("")
st.write("")

pie = st.selectbox("Select Label of Pie you are interested in:",["Sun","Sat","Thur"])
st.markdown(f"You selected <b>{pie}</b>",unsafe_allow_html = True)
