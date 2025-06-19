

---

## 🌐 Streamlit Dashboard

This project includes an interactive **Streamlit dashboard** to visually explore traffic patterns.

### ▶️ How to Run the Streamlit App

1. Make sure you have installed the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Then run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### 📋 Dashboard Features

Use the sidebar dropdown to explore the following visualizations:

| Visualization Option                      | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| Traffic Volume Distribution              | Histogram showing bimodal traffic patterns                                 |
| Day vs Night Traffic Volume              | Compare hourly volumes during day and night                                |
| Monthly & Yearly Traffic Volume          | Line plots showing seasonal trends                                          |
| Day of Week Traffic Volume               | Line plot showing drop on weekends                                          |
| Hourly: Weekday vs Weekend               | Rush hour patterns for business vs leisure days                             |
| Weather-based Traffic (Simple & Detailed)| bar plots showing influence of weather conditions                          |
| Scatter: Traffic vs Temperature          | Scatter plot showing weak temperature correlation                          |
| Line: Daily Traffic Volume               | Interactive timeline of daily volume (2012–2018)                           |
| Heatmap: Hour vs Weekday                 | Detailed rush hour patterns across each day of the week                    |

Each chart includes annotated **markdown insights** summarizing key trends.

---

### 📁 File Structure

- `app.py`: Full-featured Streamlit app
- `Metro_Interstate_Traffic_Volume.csv`: Dataset file
- `README.md`: Project documentation
- `requirements.txt`: Python dependencies

