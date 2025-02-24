import streamlit as st
import pandas as pd



# Load the dataset
df = pd.read_csv("weatherHistory.csv")

# Streamlit App Title
st.title("Weather Dataset Analysis")

# Show dataset info
st.subheader("Dataset Overview")
st.write(df.head())  # Show first few rows

# Display column data types
st.subheader("Dataset Information")
st.write(pd.DataFrame({"Column": df.columns, "Data Type": df.dtypes}))

# Summary statistics
st.subheader("Dataset Summary")
st.write(df.describe())




#✅ 1️⃣ Add a Sidebar for User Filters

# Sidebar for filtering
st.sidebar.header("Filter Options")

# Select Weather Condition
weather_options = df['Summary'].unique()
selected_weather = st.sidebar.multiselect("Select Weather Conditions", weather_options, default=weather_options)

# Filter data based on selection
filtered_df = df[df['Summary'].isin(selected_weather)]
st.subheader("Filtered Data")
st.write(filtered_df.head())




#✅ 2️⃣ Visualizing Temperature Trends



import matplotlib.pyplot as plt
import seaborn as sns

st.subheader("Temperature Trends Over Time")

# Convert 'Formatted Date' to datetime
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'])
filtered_df['Formatted Date'] = pd.to_datetime(filtered_df['Formatted Date'])

# Plot the temperature trend
fig, ax = plt.subplots()
sns.lineplot(data=filtered_df, x='Formatted Date', y='Temperature (C)', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)






#✅ 3️⃣ Humidity & Wind Speed Distribution


st.subheader("Humidity & Wind Speed Distribution")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Humidity distribution
sns.histplot(df["Humidity"], kde=True, bins=30, ax=axes[0])
axes[0].set_title("Humidity Distribution")

# Wind Speed distribution
sns.histplot(df["Wind Speed (km/h)"], kde=True, bins=30, ax=axes[1])
axes[1].set_title("Wind Speed Distribution")

st.pyplot(fig)
