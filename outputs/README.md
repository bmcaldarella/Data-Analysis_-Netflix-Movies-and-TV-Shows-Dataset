# Netflix Data Analysis – CSE 310

## Project Overview
This project was developed for the **CSE 310 – Applied Programming** course as part of the **Data Analysis module**.  
The goal of this project is to analyze a real-world dataset using Python and data analysis libraries in order to answer meaningful questions and justify conclusions based on the data.

The dataset used contains information about movies and TV shows available on Netflix, including country of origin, release year, date added to the platform, duration, and content type.

---

## Dataset
- **Name:** Netflix Movies and TV Shows Dataset  
- **Format:** CSV  
- **Source:** Public dataset (e.g., Kaggle)  
- **Description:**  
  The dataset includes Netflix titles with attributes such as:
  - `type` (Movie or TV Show)
  - `title`
  - `country`
  - `date_added`
  - `release_year`
  - `rating`
  - `duration`
  - `listed_in` (genres)
  - `description`

---

## Technologies Used
- Python 3
- Pandas (data analysis)
- Matplotlib (data visualization)

---

## Project Structure
data-analysis-project/
│
├── data/
│ └── Netflix_movies_and_tv_shows_clustering.csv
│
├── src/
│ └── analysis.py
│
├── outputs/
│ └── titles_added_per_year.png
│
├── requirements.txt
└── README.md




---

## Questions Analyzed

### Question 1  
**What are the top 10 countries with the most titles in the Netflix catalog?**

**Techniques used:**
- Filtering missing values
- Aggregation using counts
- Sorting results

**Summary:**  
This analysis identifies which countries contribute the most content to Netflix, highlighting regional dominance in the platform’s catalog.

---

### Question 2  
**How many titles were added to Netflix each year based on the `date_added` column?**

**Techniques used:**
- Filtering missing values
- Data conversion (text to datetime)
- Grouping by year
- Aggregation using counts
- Sorting by year
- Data visualization (graph)

**Summary:**  
This analysis reveals how Netflix’s content library has grown over time and identifies peak years where the most titles were added.

---

### Question 3 (Additional Question)  
**What is the longest movie available on Netflix?**

**Techniques used:**
- Filtering by content type (movies only)
- Data cleaning and conversion (duration text to numeric minutes)
- Sorting by duration

**Summary:**  
By converting movie durations into numeric values, the analysis identifies the longest movie in the dataset.

---

## Data Visualization
The project includes a line graph that shows the **number of movies and TV shows added to Netflix per year**.

- **X-axis:** Year content was added
- **Y-axis:** Number of titles added

The graph helps visualize growth trends and highlights peak years in Netflix’s expansion.

The image is saved in:


outputs/titles_added_per_year.png


---

## How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2.Install dependencies:
pip install -r requirements.txt

3.Run the analysis:
python src/analysis.py


Author

Brandon
CSE 310 – Applied Programming
Brigham Young University–Idaho