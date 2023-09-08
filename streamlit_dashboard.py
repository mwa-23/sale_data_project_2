import streamlit as st
import pandas as pd
import plotly.express as px


data = pd.read_csv("sales_data.csv")

# Convert "Order Date" to datetime
data['Order Date'] = pd.to_datetime(data['Order Date'], format='%Y-%m-%d')

# Extract year and month from "Order Date" and create "month/year" column
data['month/year'] = data['Order Date'].dt.strftime('%Y-%m')

# Streamlit UI
st.set_page_config(page_title="Sales Analysis Dashboard", page_icon=":bar_chart:")
st.title("Interactive Dashboard: Sales Analysis")



# Content for the tabs

st.header("Monthly Sales Trend")
 # Group data by month/year and calculate total sales

st.header("Sales Trend Over Years")
    # Group data by order year and calculate total sales
sales_over_years = data.groupby('order year')['Sales'].sum().reset_index()
fig_sales_trend = px.line(sales_over_years, x='order year', y='Sales', title="Sales Trend Over Years")
st.plotly_chart(fig_sales_trend)
sales_by_month = data.groupby('month/year')['Sales'].sum().reset_index()
fig_monthly_sales = px.line(sales_by_month, x='month/year', y='Sales', title="Monthly Sales Trend")
st.plotly_chart(fig_monthly_sales)
    
st.title("Overview")

# Sidebar for year filter
selected_year = st.sidebar.selectbox("Filter by Year", data["order year"].unique())

# Filter data based on selected year
filtered_data = data[data["order year"] == selected_year]

# Display data or visualizations
st.write(f"Showing data for the year {selected_year}")
st.write(filtered_data)


st.header("Category Analysis")
    # Group data by category and calculate total sales
title=("Category Analysis")
     
    
sales_by_subcategory = data.groupby('Sub-Category')['Sales'].sum().reset_index()
fig_category_sales = px.bar(sales_by_subcategory, x='Sub-Category', y='Sales', title="Sub Category Analysis")
    
st.plotly_chart(fig_category_sales)
    
sales_by_subcategory = data.groupby('Sub-Category')['Sales'].sum().reset_index()
fig_subcategory_sales = px.bar(sales_by_subcategory, x='Sub-Category', y='Sales', title="Sub Category Analysis")
st.plotly_chart(fig_subcategory_sales)

st.header("Region Analysis")
    # Group data by region and calculate total sales
sales_by_region = data.groupby('Region')['Sales'].sum().reset_index()
fig_region_sales = px.pie(sales_by_region, names='Region', values='Sales', title="Region Analysis")
st.plotly_chart(fig_region_sales)
    
sales_by_country = data.groupby('Country')['Sales'].sum().reset_index()
fig6 = px.choropleth(sales_by_country, locations='Country', locationmode='country names', color='Sales',         title='Sales by Country')
st.plotly_chart(fig6)



st.header("Segment Analysis")
   # Group data by segment and calculate total sales
sales_by_segment = data.groupby('Segment')['Sales'].sum().reset_index()
fig_segment_sales = px.pie(sales_by_segment, names='Segment', values='Sales', title="Segment Analysis")
st.plotly_chart(fig_segment_sales)
    

     # Sidebar with category selection
selected_segment = st.sidebar.selectbox("Select Segment", data['Segment'].unique())
    
    # Filter data by selected category
filtered_data = data[data['Segment'] == selected_segment]

# Group data by segment and calculate total sales
segment_sales = filtered_data.groupby('Category')['Sales'].sum().reset_index()

# Create a bar chart for segment analysis
fig_segment_analysis = px.bar(segment_sales, x='Category', y='Sales', title=f"Segment Analysis for       {selected_segment} Segment")
st.plotly_chart(fig_segment_analysis)
        



st.header("Top Products")
    # Group data by product name and calculate total sales
top_products = data.groupby('Product Name')['Sales'].sum().reset_index().nlargest(20, 'Sales')
fig_top_products = px.bar(top_products, x='Sales', y='Product Name', orientation='h', title="Top 20 Products")
st.plotly_chart(fig_top_products)


st.header("Discount vs. Profit")
    # Create a scatter plot of Discount vs. Profit
fig_discount_profit = px.scatter(data, x='Discount', y='Profit', title="Discount vs. Profit")
st.plotly_chart(fig_discount_profit)


st.header("Shipping Cost Distribution")
    # Create a histogram of shipping cost distribution
fig_shipping_cost = px.histogram(data, x='Shipping Cost', title="Shipping Cost Distribution")
st.plotly_chart(fig_shipping_cost)


st.header("Top Cities by Sales")
    # Group data by city and calculate total sales
top_cities = data.groupby('City')['Sales'].sum().reset_index().nlargest(10, 'Sales')
fig_top_cities = px.bar(top_cities, x='Sales', y='City', orientation='h', title="Top 10 Cities by Sales")
st.plotly_chart(fig_top_cities)


st.header("Average Order Quantity by Category")
    # Group data by category and calculate average order quantity
avg_order_quantity_by_category = data.groupby('Category')['Quantity'].mean().reset_index()
fig_avg_order_quantity = px.bar(avg_order_quantity_by_category, x='Category', y='Quantity', title="Average Order Quantity by Category")
st.plotly_chart(fig_avg_order_quantity)









