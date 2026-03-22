import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('vehicles_us.csv')

# Title
st.header('Car Advertisement Dashboard')
st.write('Exploring the US vehicle listings dataset')

# Show raw data checkbox
if st.checkbox('Show raw data'):
    st.write(df.head(50))

# Histogram - Price Distribution
st.header('Price Distribution')
fig1 = px.histogram(df, x='price', nbins=50, title='Distribution of Car Prices')
st.plotly_chart(fig1)

# Histogram - Odometer Distribution
st.header('Odometer Distribution')
show_old = st.checkbox('Include high mileage cars (over 300,000 miles)')
if show_old:
    fig2 = px.histogram(df, x='odometer', nbins=50, title='Odometer Reading Distribution')
else:
    fig2 = px.histogram(df[df['odometer'] < 300000], x='odometer', nbins=50, title='Odometer Reading Distribution (under 300k miles)')
st.plotly_chart(fig2)

# Scatter plot - Price vs Odometer
st.header('Price vs Odometer')
fig3 = px.scatter(df, x='odometer', y='price', color='condition',
                  title='Price vs Odometer by Condition')
st.plotly_chart(fig3)