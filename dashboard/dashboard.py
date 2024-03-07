import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)
sns.set(style='dark')

hours_df = pd.read_csv('Proyek-Analisis-Data-Dicoding/dashboard/hours.csv')
days_df = pd.read_csv ('Proyek-Analisis-Data-Dicoding/dashboard/days.csv')

st.header("Bike-Sharing Dashboard")

# Sidebar
st.sidebar.title("Information:")
st.sidebar.markdown(
    "**> Nama       : Anggit Rizki Fadilah**")
st.sidebar.markdown(
    "**> Email      : anggitrizki99@gmail.com**")
st.sidebar.markdown(
    "**> Dicoding   : anggitrizkif**")
st.sidebar.markdown(
    "**> Bangkit ID : m010d4ky1448**")


st.sidebar.title("Navigasi")
page = st.sidebar.radio("Menu", ["Home", "Answering Question", "Conclusion", ])

if page == "Home":
    st.markdown("## Welcome to the Bike-Sharing Data Set")
    
    st.write("**This is a 10 Random Sample Row of Data Frame from days_df:**")
    st.write(days_df.sample(10))
    st.write("**This is Statistics of days_df:**")
    st.write(days_df.describe())
    
    st.write("**This is a 10 Random Sampel Row of Data Frame from hours_df:**")
    st.write(hours_df.sample(10))
    st.write("**This is Statistics of hours_df:**")
    st.write(hours_df.describe())
    st.write("""	
            **Information:**
            \n- **instant**: record index
	        \n- **dteday** : date
	        \n- **season** :  
            \n    1. springer
            \n    2. summer
            \n    3. fall 
            \n    4. winter
	        \n- **yr** : year (0: 2011, 1:2012)
	        \n- **mnth** : month ( 1 to 12)
	        \n- **hr** : hour (0 to 23)
	        \n- **holiday** : weather day is holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)
	        \n- **weekday** : day of the week
	        \n- **workingday** : if day is neither weekend nor holiday is 1, otherwise is 0.
	        \n+ **weathersit** : 
		    \n    - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
		    \n    - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
		    \n    - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
		    \n    - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
	        \n- **temp** : Normalized temperature in Celsius. The values are divided to 41 (max)
	        \n- **atemp**: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
	        \n- **hum**: Normalized humidity. The values are divided to 100 (max)
	        \n- **windspeed**: Normalized wind speed. The values are divided to 67 (max)
	        \n- **casual**: count of casual users
	        \n- **registered**: count of registered users
	        \n- **cnt**: count of total rental bikes including both casual and registered""")
    
    st.markdown("## Data Exploratory (EDA)")
    # Mean of Rent per Month (2012)
    st.write ("**Rent per Month (2012)**")
    rent_per_month=days_df.groupby("mnth")['cnt'].mean().reset_index()
    rent_per_month.set_index("mnth", inplace=True)
    rent_per_month
    
    plt.figure()

    sns.barplot(data=rent_per_month, x=rent_per_month.index, y="cnt")
    plt.show()
    
    # The day with the highest number of bike rentals from 2011-2012.
    st.write("**The Day With The Highest Number of Bike Rental from 2011-2012**")
    most_rent=days_df.groupby("dteday")['cnt'].mean().reset_index().sort_values(by="cnt", ascending=False)
    most_rent.set_index("dteday", inplace=True)
    most_rent 
   

elif page == "Answering Question":
    st.title("**Answering Question**")
    
    st.header("Total Rentals by Season in 2011")
    season_total_rentals = days_df[days_df['yr'] == 0].groupby('season')['cnt'].sum().sort_values(ascending=False)
    st.write(season_total_rentals)
    
    st.header("Relationship between Temperature and Registered Users")
    st.write("Scatter Plot of Temperature vs Registered Users")
    fig, ax = plt.subplots()
    sns.scatterplot(x='temp', y='registered', data=days_df, ax=ax)
    st.pyplot(fig)
    
    st.header("Weather Impact on Bike Rentals in Spring")
    filtered_days_df = days_df[(days_df['season'] == 1)]
    st.write("Bar Plot of Weather Situation vs Bike Rentals in Spring")
    fig, ax = plt.subplots()
    sns.barplot(x='weathersit', y='cnt', data=filtered_days_df, ax=ax)
    st.pyplot(fig)
    
    st.header("Hourly Bike Rentals on Christmas Holiday 2011")
    filtered_data = hours_df[(hours_df["yr"] == 0) & (hours_df["holiday"] == 1) & (hours_df["season"] == 4)]
    distribusi_per_jam = filtered_data.groupby("hr")["cnt"].sum()
    st.write("Hourly Distribution of Bike Rentals on Christmas Holiday 2011")
    st.write(distribusi_per_jam)
    
elif page == "Conclusion":
    st.title("Conclusion")
    st.write("""
    1. In 2011, the highest total bike rentals occurred during the fall season (season 3), with a total of 419,650 rentals. Meanwhile, the lowest bike rentals occurred during the spring season (season 1), with a total of 150,000 rentals.
    2. There is a positive correlation between temperature (temp) and the number of registered users, indicating that an increase in temperature leads to an increase in the number of registered users.
    3. An analysis of the impact of weather condition (weathersit) on bike rentals (cnt) in the spring season (season 1) shows that weather changes have a significant impact on bike user behavior. In clear, partly cloudy, and cloudy weather (weathersit 1), there is a significant increase in bike rentals.
    4. An analysis of the hourly distribution of bike rentals on Christmas holiday in 2011 shows that the pattern of bike rentals varies by hour, with peak rentals occurring at 5 PM and 6 PM.
    
    In conclusion, to increase bike rentals, it is recommended to focus on the fall season and consider weather conditions. An increase in temperature can also lead to an increase in the number of registered users. In the winter season, it may be beneficial to focus on Christmas holidays or Christmas Eve.
    """)

# Show dataset source
st.sidebar.markdown("## Dataset Source:")
st.sidebar.markdown("[Dataset](https://link-to-your-dataset)")
