# 🎧 Supportlytics — IT Support Performance Analytics

Supportlytics is an end-to-end analytics project built on a large-scale IT support ticket dataset (~200K records). It covers data cleaning, feature engineering, exploratory analysis, clustering, and trend analysis, and culminates in an interactive **Streamlit dashboard** for tracking support team performance.

This branch (`Shresth_Prakash_suportlytics`) contains the work completed as part of an **Infosys Springboard internship**.

## 📊 Key Performance Indicators

The project is organized around four core KPIs:

1. **Average Resolution Time** — how long tickets take to resolve, broken down by category, priority, and region
2. **Most Frequent Categories** — ticket volume distribution across issue categories and priorities
3. **Cluster Similarity Index** — KMeans-based clustering of tickets by resolution time, complexity, satisfaction, and priority, with a similarity score per ticket
4. **Top Performing Regions** — SLA compliance and resolution speed compared across regions

## 🗂️ Project Structure

| File | Description |
|---|---|
| `analysis.ipynb` | Main analysis notebook covering all milestones and modules (see below) |
| `main.py` | Streamlit dashboard (`streamlit run main.py`) — interactive KPI views built on the processed dataset |
| `pyproject.toml` | Project dependencies |
| `Supportlytics_Final_Report.docx` | Final written report summarizing findings |
| `LICENSE` | MIT License |

## 🧭 Milestones

- **Milestone 1 — Data Setup & Feature Engineering**
  - Module 1: Project initialization and synthetic dataset generation
  - Module 2: Data cleaning and feature engineering (missing values, text cleanup, datetime parsing, `Resolution_Duration`, `Priority_Score`, `Performance_Bucket`)
- **Milestone 2 — Exploratory Visualization & Clustering**
  - Module 3: Exploratory visualizations (ticket type, queue/priority distributions, etc.)
  - Module 4: Similarity and cluster insights (KMeans clustering + similarity scoring)
- **Milestone 3 — Performance Trend Analysis**
  - Module 5: Performance trend analysis
  - Module 6: Geographic and category-level insights
- **Milestone 4 — Interactive Dashboard**
  - Module 7: `main.py` — a Streamlit dashboard presenting all four KPIs with filters by region, priority, and category

## ⚙️ Tech Stack

- **Python 3.13+**
- **pandas**, **numpy** — data processing
- **matplotlib**, **seaborn**, **plotly** — visualization
- **scikit-learn** (`KMeans`, `StandardScaler`) — clustering
- **Streamlit** — interactive dashboard

## 🚀 Getting Started

1. Clone the repository and switch to this branch:
   ```bash
   git clone https://github.com/springboardmentor1210a/Supportlytics.git
   cd Supportlytics
   git checkout Shresth_Prakash_suportlytics
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # or, if using uv/pyproject.toml:
   uv sync
   ```
3. Run the notebook for the full analysis walkthrough:
   ```bash
   jupyter notebook analysis.ipynb
   ```
4. Launch the interactive dashboard:
   ```bash
   streamlit run main.py
   ```
   The dashboard accepts either the raw dataset (`customer_support_tickets_200k.csv`) or the pre-processed dataset (`processed_customer_support_tickets.csv`) via the sidebar uploader.

## 📄 Report

A full write-up of the methodology, findings, and recommendations is available in [`Supportlytics_Final_Report.docx`](./Supportlytics_Final_Report.docx).

## 📝 License

This project is licensed under the [MIT License](./LICENSE).
