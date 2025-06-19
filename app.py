
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")
st.title("🚗 I-94 Traffic Volume Analysis Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv("Metro_Interstate_Traffic_Volume.csv")
    df['date_time'] = pd.to_datetime(df['date_time'])
    return df

df = load_data()

# Split data
day = df[(df['date_time'].dt.hour >= 7) & (df['date_time'].dt.hour < 19)]
night = df[(df['date_time'].dt.hour >= 19) | (df['date_time'].dt.hour < 7)]
day['month'] = day['date_time'].dt.month
day['year'] = day['date_time'].dt.year
day['dayofweek'] = day['date_time'].dt.dayofweek
day['hour'] = day['date_time'].dt.hour
business_days = day[day['dayofweek'] <= 4]
weekend = day[day['dayofweek'] >= 5]

# Sidebar options
option = st.sidebar.selectbox(
    "Select Visualization",
    [
        "Traffic Volume Distribution",
        "Day vs Night Traffic Volume",
        "Monthly Average Traffic Volume",
        "Yearly Average Traffic Volume",
        "Day of Week Traffic Volume",
        "Hourly Traffic: Weekday vs Weekend",
        "Traffic Volume by Weather",
        "Traffic Volume by Detailed Weather Description",
        "Scatter: Traffic vs Temperature",
        "Line: Daily Traffic Volume",
        "Heatmap: Hour vs Weekday"
    ]
)

# Render selected plot
if option == "Traffic Volume Distribution":
    st.subheader("Traffic Volume Distribution")
    fig, ax = plt.subplots(figsize=(5,3))
    df['traffic_volume'].plot.hist(ax=ax, bins=30)
    ax.set_xlabel("Traffic Volume")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    st.markdown("""
    ## Insights from Traffic Volume Distribution

- The traffic volume ranges from 0 to around 7000 vehicles per hour.
- There are two prominent peaks in the distribution:
- One around 0–1000, which could represent low traffic hours, possibly during the night.
- Another major peak between 4000–5000, indicating high traffic hours, likely during rush hour.
- The distribution appears to be bimodal, suggesting two distinct traffic patterns during the day (low and high volume periods).
- Very high traffic volumes (above 6000) are less frequent, and the frequency gradually decreases in that range.
    """)

elif option == "Day vs Night Traffic Volume":
    st.subheader("Day vs Night Traffic Volume")
    col1, col2 = st.columns(2)
    with col1:
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        ax1.hist(day['traffic_volume'], bins=30)
        ax1.set_title("Day Traffic")
        st.pyplot(fig1)
    with col2:
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax2.hist(night['traffic_volume'], bins=30)
        ax2.set_title("Night Traffic")
        st.pyplot(fig2)
    st.markdown("""
    ## Histogram Observations

## 1. Daytime Traffic (Left Plot):

- Shows a clear peak between 4000 and 5500 vehicles/hour, indicating high and consistent traffic during the day.
- Most values are concentrated between 3000 and 6000, typical for working hours or school runs.
- Very few low traffic volume instances during the day.

## 2. Nighttime Traffic (Right Plot):

- Displays a sharp peak below 1000 vehicles/hour, meaning most nighttime hours experience low traffic.
- The distribution is right-skewed, with occasional high-traffic outliers.
- Significantly more hours with very low volume (0–1000 range) compared to daytime.
    """)


elif option == "Monthly Average Traffic Volume":
    st.subheader("Monthly Average Traffic Volume")
    monthly = day.groupby('month')['traffic_volume'].mean()
    fig, ax = plt.subplots(figsize=(7, 4))
    monthly.plot(ax=ax)
    ax.set_ylabel("Avg Traffic Volume")
    st.pyplot(fig)
    st.markdown("""
    This line plot shows how the average daytime traffic volume on I-94 varies by month throughout the year.

## Key Observations:

- Lowest traffic volume is in December (Month 12), possibly due to holidays (Christmas/New Year),Winter weather conditions affecting road usage.
- Traffic volume increases steadily from January to May, peaking slightly around May–June (Months 5–6).
- Sharp drop in July (Month 7) — we don't know the exact reason so let's see how the traffic volume changed each year in July
- August to October (Months 8–10) see another rise in traffic, possibly as schools and work routines resume.
- A noticeable decline starts in November and drops sharply in December.
    """)

elif option == "Yearly Average Traffic Volume":
    st.subheader("Yearly Average Traffic Volume")
    yearly = day.groupby('year')['traffic_volume'].mean()
    fig, ax = plt.subplots(figsize=(5, 3))
    yearly.plot(ax=ax)
    ax.set_ylabel("Avg Traffic Volume")
    st.pyplot(fig)
    st.markdown("""
    Typically, traffic volume is high in July, much like other warm months. However, 2016 shows an unusual drop, which may be due to road construction — a 2016 article supports this explanation.(https://www.crainsdetroit.com/article/20160728/NEWS/160729841/weekend-construction-i-96-us-23-bridge-work-i-94-lane-closures-i-696)

In general, we can conclude that warmer months tend to have higher traffic compared to colder months. During a warm month, the average daytime traffic volume is usually close to 5,000 vehicles per hour.
    """)

elif option == "Day of Week Traffic Volume":
    st.subheader("Traffic Volume by Day of the Week")
    dow = day.groupby('dayofweek')['traffic_volume'].mean()
    fig, ax = plt.subplots(figsize=(5, 3))
    dow.plot(ax=ax)
    ax.set_ylabel("Avg Traffic Volume")
    st.pyplot(fig)
    st.markdown("""
    ## Average Daytime Traffic Volume by Day of the Week

This line chart shows how average daytime traffic volume varies across the days of the week, where:

0 = Monday,
6 = Sunday.

## Key Observations:

- Weekday traffic (Monday to Friday) is consistently high:
- Peaks around Wednesday and Thursday, with average traffic volume exceeding 5250 vehicles/hour.
- Slight dip on Monday, likely due to slower starts or flexible work schedules.
- Sharp decline starting Saturday (5):
Traffic drops to around 3900 vehicles/hour on Saturday.
- Lowest traffic is seen on Sunday, at roughly 3400 vehicles/hour.
- The weekend traffic is significantly lower, aligning with reduced work-related travel and more flexible schedules.
    """)


elif option == "Hourly Traffic: Weekday vs Weekend":
    st.subheader("Hourly Traffic Volume: Weekday vs Weekend")
    by_hour_business = business_days.groupby('hour')['traffic_volume'].mean()
    by_hour_weekend = weekend.groupby('hour')['traffic_volume'].mean()
    col1, col2 = st.columns(2)
    with col1:
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        by_hour_business.plot(ax=ax1)
        ax1.set_title("Weekdays")
        st.pyplot(fig1)
    with col2:
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        by_hour_weekend.plot(ax=ax2)
        ax2.set_title("Weekends")
        st.pyplot(fig2)
    st.markdown("""
    ## Traffic Volume by Hour: Weekdays vs Weekends
This analysis shows how average traffic volume changes by hour of the day, comparing business days with weekends.

 Weekdays (Monday–Friday):

- Sharp peak at 7 AM: Highest volume (~6030 cars/hour) occurs during the morning rush hour, as people commute to work.
- A second, broader peak in the late afternoon (4–5 PM) indicates the evening rush.
- Between 11 AM and 2 PM, traffic volume dips slightly but remains steady.
- This trend shows a typical two-peak (bimodal) pattern seen in daily work commutes.

 Weekends (Saturday–Sunday):

- Traffic volume is lower overall compared to weekdays.
- There is no sharp morning peak. Instead, traffic volume gradually rises starting around 8 AM and stays relatively steady between 10 AM and 4 PM (~4300–4400 cars/hour).
- This flatter curve suggests more flexible travel times, likely due to leisure activities, errands, or outings.
    """)

elif option == "Traffic Volume by Weather":
    st.subheader("Traffic Volume by Weather Condition")
    by_weather = df.groupby('weather_main')['traffic_volume'].mean()
    fig, ax = plt.subplots(figsize=(5, 3))
    by_weather.plot(kind='barh', ax=ax)
    ax.set_xlabel("Avg Traffic Volume")
    st.pyplot(fig)
    st.markdown("""
    ## Key Observations:

- Highest average traffic volumes occur during:
    Thunderstorms, Drizzle, Rain, and Clear weather.
- Surprisingly, bad weather conditions like Thunderstorm and Rain show traffic volumes comparable to or higher than clear conditions.
- Lowest average traffic volume is observed during Fog, possibly due to reduced visibility discouraging travel.
- Other weather types like Mist, Haze, Snow, and Smoke show fairly consistent traffic levels, with only slight variation.
- Squall and Snow also show slightly lower volumes compared to clear days but not significantly.

## Interpretation:

- Weather conditions do not drastically reduce traffic volume in most cases.
- High traffic during rainy or stormy conditions might indicate that people still commute regardless of weather, or possibly, that these conditions occur during peak hours.
- The drop in volume during foggy conditions suggests that severe visibility issues may influence traffic behavior more than general rain or snow.
- Since variations are minor, it confirms previous findings that weather has a weak correlation with traffic volume.


    """)

elif option == "Traffic Volume by Detailed Weather Description":
    st.subheader("Traffic Volume by Detailed Weather Description")

    # Group data
    by_weather_description = df.groupby('weather_description')['traffic_volume'].mean().sort_values()

    # Plot
    fig, ax = plt.subplots(figsize=(6, 10))
    by_weather_description.plot.barh(ax=ax)
    ax.set_xlabel("Average Traffic Volume")
    ax.set_ylabel("Weather Description")
    st.pyplot(fig)

    # Description
    st.markdown("""
    ## Key Insights:

- Highest average traffic volumes are observed during:
     - Sky is clear, drizzle, broken clouds, and light rain and snow — all exceeding 5000 vehicles/hour.
    - These conditions suggest normal or mildly disruptive weather, where people are likely to travel as usual.
- Moderate to heavy weather events (like heavy snow, very heavy rain, thunderstorm with drizzle) still maintain fairly high traffic volumes around 4000–4700, indicating that traffic often continues despite adverse conditions.
- Lowest traffic volumes are seen during:
    - Thunderstorm with drizzle and SQUALLS — both likely considered hazardous enough to discourage driving.
    - Fog, freezing rain, and haze also show relatively lower traffic, possibly due to visibility and safety concerns.
    """)


elif option == "Scatter: Traffic vs Temperature":
    st.subheader("Scatter Plot: Traffic Volume vs Temperature")
    fig = px.scatter(df, x='traffic_volume', y='temp',
                     title="Traffic Volume vs Temperature",
                     opacity=0.3)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
    ## Scatter Plot: Traffic Volume vs. Temperature

This scatter plot visualizes the relationship between traffic volume and temperature (in Kelvin) using daytime data.

Key Observations:

- The points are densely clustered between:
    - Traffic volume: 3000–6000 vehicles/hour
    - Temperature: 270–300 K (roughly 0°C to 27°C)
- There is no strong visible trend or pattern between temperature and traffic volume:
    - Data points are spread across all temperature levels, even at high traffic volumes.
    - The distribution is somewhat horizontal, suggesting low or weak correlation.
- Extreme temperatures (below 250 K or above 310 K) show fewer observations, possibly because such conditions are rare in the region or time period analyzed.
- This confirms the low correlation coefficient (~0.13) observed earlier between temperature and traffic volume.
- While traffic tends to be slightly higher in moderate to warm temperatures, temperature alone does not significantly affect traffic volume.
- Other factors like weather, hour of the day, day of the week, and work schedules likely play a much more important role.


    """)

elif option == "Line: Daily Traffic Volume":
    st.subheader("Daily Traffic Volume Over Time")
    daily_traffic = df.resample('D', on='date_time')['traffic_volume'].mean().reset_index()
    fig = px.line(daily_traffic, x='date_time', y='traffic_volume',
                  labels={'date_time': 'Date', 'traffic_volume': 'Traffic Volume'},
                  title="Daily Traffic Volume on I-94")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
    ## Insight: Daily Traffic Volume Over Time

Key Observations:

- Overall Stability:
    - Traffic volume remains fairly consistent across years, mostly fluctuating between 3000 and 5000 vehicles/day.
- Seasonal Noise and Spikes: Daily data shows frequent spikes and drops, which may correspond to:
    - Holidays and weekends
    - Weather events or road conditions
    - Sensor anomalies or maintenance
- Notable Gaps or Drops:
    - Around late 2014 to 2015, and again in mid-2016, there are visible drops or missing data.
    - These likely indicate road construction, closures, or data collection issues, as also supported by past analyses.
    """)

elif option == "Heatmap: Hour vs Weekday":
    st.subheader("Heatmap: Average Traffic Volume by Hour and Weekday")

    heatmap_data = df.copy()
    heatmap_data['weekday'] = heatmap_data['date_time'].dt.day_name()
    heatmap_data['hour'] = heatmap_data['date_time'].dt.hour

    # Group and order
    heatmap_data = heatmap_data.groupby(['weekday', 'hour'])['traffic_volume'].mean().reset_index()
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    heatmap_data['weekday'] = pd.Categorical(heatmap_data['weekday'], categories=weekday_order, ordered=True)

    # Plot
    fig_heatmap = px.density_heatmap(
        heatmap_data,
        x='hour',
        y='weekday',
        z='traffic_volume',
        color_continuous_scale='Viridis',
        title='Average Traffic Volume by Hour and Weekday',
        labels={'traffic_volume': 'Traffic Volume', 'hour': 'Hour of Day', 'weekday': 'Day of Week'}
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

    # Description
    st.markdown("""
    **Insight:**  
    This heatmap visualizes average traffic volume for each hour across weekdays.  
    - Higher traffic is visible during **morning and evening rush hours** (around 7–9 AM and 4–6 PM) from Monday to Friday.  
    - Weekends show lower and more evenly spread traffic volume.
    """)

