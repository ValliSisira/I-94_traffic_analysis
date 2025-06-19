# I-94 Traffic Volume EDA 📊🚗

This project performs Exploratory Data Analysis (EDA) on the **Metro Interstate Traffic Volume** dataset collected from the I-94 highway in Minneapolis. The goal is to analyze traffic patterns by hour, day, weather, and season, and extract meaningful insights using Python and data visualization libraries.

## 📁 Dataset
The dataset used is `Metro_Interstate_Traffic_Volume.csv`, which contains hourly records of traffic volume along with weather and time data from 2012 to 2018.

## 📌 Key Analyses
- Distribution of traffic volume (overall, by day/night, weekdays/weekends)
- Temporal trends (hourly, daily, monthly, yearly)
- Weather influence (basic and detailed weather conditions)
- Interactive visualizations using Plotly and Seaborn

## 🛠️ Tools and Libraries
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook

## 📂 Structure
- `I-94_EDA.ipynb`: Main notebook containing all code and visualizations
- `requirements.txt`: List of dependencies

## ▶️ How to Run
1. Clone the repository or download the notebook and dataset.
2. Install the dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Open the notebook using Jupyter:
   ```bash
   jupyter notebook I-94_EDA.ipynb
   ```

## 📈 Example Outputs
- Heatmaps of traffic volume by weekday and hour
- Line charts showing monthly and yearly trends
- Bar plots of traffic volume under different weather conditions

## 🧠 Insights
- Traffic is highest during weekday rush hours.
- Volume drops significantly on weekends and holidays.
- Temperature and weather have only a mild effect on traffic volume.

---
## 📊 Interactive Dashboard Overview

This Streamlit-based dashboard offers multiple traffic volume visualizations using a convenient dropdown menu. Users can select different views to explore traffic patterns on I-94.

### 🧭 Dropdown Options Available:
- Traffic Volume Distribution
- Day vs Night Traffic Volume
- Monthly Average Traffic Volume
- Yearly Average Traffic Volume
- Day of Week Traffic Volume
- Hourly Traffic: Weekday vs Weekend
- Traffic Volume by Weather
- Traffic Volume by Detailed Weather Description

Each selection dynamically updates the visualization, helping users gain insights from various angles.

---

### 📸 Screenshot: Day vs Night Traffic Visualization

<img src="" alt="Day vs Night Traffic" width="800"/>



