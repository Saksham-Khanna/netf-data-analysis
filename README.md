# Netflix Content Analysis

![Netflix Logo](https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg)

## 📌 Project Overview
This project is an end-to-end, professional Data Analysis of the Netflix catalog, designed to provide actionable business insights for executives. By analyzing thousands of movies and TV shows, we uncover trends in content strategy, regional production powerhouses, optimal movie runtimes, and genre saturation.

## 📊 Dataset
The dataset utilized is the **Netflix Movies and TV Shows** dataset (originally created by Shivam Bansal on Kaggle). It contains metadata for all movies and TV shows available on the platform, including directors, cast, release year, rating, duration, and listed genres.

## 🎯 Objectives
- Perform rigorous Exploratory Data Analysis (EDA) on the Netflix catalog.
- Extract statistical relationships between content attributes.
- Generate high-quality, executive-ready visualizations.
- Provide 15 actionable business insights to drive content acquisition and production strategies.

## 📂 Project Structure
```text
Netflix-Data-Analysis/
│
├── data/
│   └── netflix_titles.csv         # Raw dataset
│
├── notebooks/
│   └── netflix_analysis.ipynb     # Main Jupyter Notebook containing EDA & visualizations
│
├── images/                        # Saved visualization outputs
│
├── scripts/
│   ├── download_data.py           # Script to download the dataset
│   └── generate_analysis.py       # Script to generate the Jupyter Notebook
│
├── insights.md                    # 15 Actionable Executive Insights
├── requirements.txt               # Python dependencies
├── .gitignore
└── README.md                      # Project Documentation
```

## 🛠️ Methodology & Data Cleaning
1. **Data Understanding:** Assessed missing values, duplicate rows, and incorrect data types.
2. **Data Cleaning:**
   - Imputed missing categorical variables (`director`, `cast`, `country`) with "Unknown" to preserve data integrity.
   - Dropped negligible rows with missing `date_added`, `rating`, or `duration`.
   - Extracted numerical values from the text-based `duration` column.
   - Converted `date_added` into proper DateTime objects and engineered `year_added` and `month_added` features.
3. **Exploratory Data Analysis:** Addressed 15 specific business questions using Seaborn and Matplotlib.
4. **Statistical Analysis:** Calculated Pearson correlation between release year and movie duration to confirm industry trends.

## 📈 Key Visualizations & Findings
The `images/` directory and the Jupyter Notebook contain detailed visualizations. Some highlights include:
- **Movies vs. TV Shows:** A heavy skew towards movies, though TV shows show rapid recent acceleration.
- **Top Producing Countries:** The US and India dominate the platform's production pipeline.
- **Movie Duration Distribution:** A clean normal distribution centered tightly around 90-100 minutes.

## 💡 Key Business Insights
Please read the [insights.md](insights.md) file for the complete list of 15 executive-level insights. A few examples:
- **Double Down on Indian Content:** The massive scale of Indian actors and directors highlights India as the premier international growth market.
- **Pivot to Retention:** TV Shows represent the best mechanism for long-term subscriber retention, yet most fail to pass 1 season.
- **Optimize Runtimes:** Stick to the 90-100 minute sweet spot for Netflix Original Movies to minimize audience drop-off.

## 💻 Installation & Usage

1. **Clone the repository.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Download Data:**
   ```bash
   python scripts/download_data.py
   ```
4. **Generate & Run Analysis Notebook:**
   ```bash
   python scripts/generate_analysis.py
   jupyter nbconvert --to notebook --execute --inplace notebooks/netflix_analysis.ipynb
   ```

## 🚀 Future Improvements
- **Sentiment Analysis:** Scrape IMDB or Rotten Tomatoes to merge sentiment scores with this dataset.
- **Time Series Forecasting:** Predict the volume of content required to sustain growth into the next 5 years.
- **Network Analysis:** Map out actor-director collaborations using Graph Theory to identify the most central figures in Netflix productions.
