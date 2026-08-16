# SUPPORTLYTICS
## Optimizing IT Support Team Performance Using Analytics

> **Internship Project — IT Support Analytics**

![Dashboard Preview](images/dashboard_full_preview.png)

---

### 1. Project Overview
**Supportlytics** is an end-to-end data analytics and business intelligence system designed to analyze IT support ticket data, uncover operational patterns, and optimize support team efficiency. The system processes multi-channel ticket logs to evaluate ticket volume, resolution times, issue categories, priority urgency, semantic issue clusters, SLA compliance, regional workload, and support team performance.

---

### 2. Business Problem
Enterprise IT support departments process thousands of tickets monthly across multiple regions, support tiers, and technical domains. Without granular analytics, organizations face:
- Unidentified resolution bottlenecks and recurring incident backlogs.
- SLA compliance penalties resulting from inefficient escalation paths.
- High manual effort spent on repetitive, addressable service requests.
- Lack of operational visibility into country-level and team-level performance variations.

---

### 3. Objectives
- **Preprocess & Standardize Data**: Ingest, cleanse, and structure 10,000 IT ticket records across 34 operational and performance attributes.
- **Engineer Analytics Features**: Compute quantitative metrics including `Resolution_Duration` (in hours) and `Priority_Score`.
- **Perform Exploratory Analysis**: Examine distribution trends across ticket types, issue categories, priorities, and inbound channels.
- **Analyze Issue Clusters**: Evaluate semantic similarity scores and identify high-friction problem clusters.
- **Benchmark Team & Regional Performance**: Quantify turnaround speed, customer satisfaction (CSAT), and SLA compliance across support teams and geographic hubs.
- **Deploy Interactive Dashboards**: Provide unified visual reporting via native Power BI Desktop (`.pbix` / `.pbip`) and an interactive Streamlit web application.

---

### 4. Key Performance Indicators (KPIs)

| KPI | Metric Name | Definition & Business Purpose |
|---|---|---|
| **Total Volume** | `Total Tickets` | Total count of support tickets logged; measures aggregate operational demand (`COUNTROWS('Data')`). |
| **Turnaround Velocity** | `Average Resolution Time` | Mean duration from ticket creation to final resolution in hours (`AVERAGE('Data'[Resolution_Duration])`). |
| **Dominant Category** | `Most Frequent Category` | The technical category generating the highest volume of support requests. |
| **Issue Similarity** | `Cluster Similarity Index` | Mean NLP semantic similarity score across ticket clusters, bounded between 0.00 and 1.00 (`AVERAGE('Data'[Similarity_Score])`). |
| **Top Region** | `Top Performing Region` | Geographic region achieving the lowest average resolution duration while maintaining SLA targets. |
| **Service Quality** | `SLA Compliance %` | Percentage of resolved tickets meeting defined SLA response and resolution thresholds. |

---

### 5. Dataset

- **Raw Data Source**: `data/IT_Support_Tickets.csv` (10,000 records, 30 columns)
- **Processed Data Source**: `data/processed/cleaned_IT_Support_Tickets.csv` (10,000 records, 32 columns)
- **Power BI Data Source**: `Supportlytics_PowerBI_Data.xlsx` / `Supportlytics_PowerBI_Data.csv` (10,000 records, 38 columns)

#### Key Schema Attributes:
- **Operational Fields**: `Ticket_ID`, `Created_Date`, `Resolution_Date`, `First_Response_Date`, `Status`, `Resolution_Code`, `Resolution_Notes`
- **Classification Fields**: `Priority`, `Ticket_Type` (Incident, Problem, Request), `Category`, `Department`, `Product`, `Tags`
- **Assignment Fields**: `Assigned_Agent`, `Team`, `Channel` (Email, Portal, Chat, Phone)
- **Performance Fields**: `Resolution_Duration` (hours), `Priority_Score` (1–4), `Customer_Satisfaction` (1–5), `SLA_Status` (Met / Breached), `Reopened`
- **Context & Geographic Fields**: `Country`, `Region` (APAC, EMEA, NA), `Device_Type`, `Operating_System`, `Latitude`, `Longitude`
- **Cluster Fields**: `Cluster_ID`, `Cluster_Name`, `Similarity_Score` (0.0–1.0), `Similarity_Level` (Low, Medium, High)

---

### 6. Technology Stack

- **Programming & Core**: Python 3.10+
- **Data Analysis & Manipulation**: Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn, Plotly Express, Plotly Graph Objects
- **Dashboarding & Business Intelligence**: Microsoft Power BI Desktop (`.pbix` / `.pbip`), Streamlit
- **Computational Environment**: Jupyter Notebook
- **Data Storage & Exchange**: CSV, Microsoft Excel (`openpyxl`)

---

### 7. Project Workflow

```
┌─────────────────────────────────────────────────────────┐
│               Data Acquisition & Ingestion              │
│            (10,000 Records, Internal CSV)               │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│              Data Cleaning & Preprocessing              │
│    (Null handling, type casting, date normalization)    │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│                   Feature Engineering                   │
│        (Resolution_Duration, Priority_Score)            │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│          Exploratory Data Analysis (EDA)                │
│    (Distribution by Type, Category, Priority, Queue)    │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│            Similarity & Cluster Analytics               │
│      (Cluster similarity, size vs type, boxplots)       │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│             Performance Trend Analysis                  │
│       (Turnaround by priority, team & country)          │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│          Geographic & Category Insights                 │
│         (Regional concentration, spatial maps)          │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│             Power BI & Streamlit Dashboards             │
│        (6-Page executive reporting & drilldowns)        │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│            Insights & Strategic Recommendations         │
└─────────────────────────────────────────────────────────┘
```

---

### 8. Data Preparation
- **Notebook**: [`notebooks/02_Data_Cleaning_Feature_Engineering.ipynb`](notebooks/02_Data_Cleaning_Feature_Engineering.ipynb)
- Standardized timestamps (`Created_Date`, `Resolution_Date`, `First_Response_Date`) to ISO datetime objects.
- Handled missing text values and tags; verified zero missing keys across primary operational columns.
- Computed `Resolution_Duration = (Resolution_Date - Created_Date)` in hours.
- Encoded `Priority_Score` numerically (`Low = 1`, `Medium = 2`, `High = 3`, `Critical = 4`).

---

### 9. Exploratory Analysis
- **Notebook**: [`notebooks/03_Exploratory_Visualization.ipynb`](notebooks/03_Exploratory_Visualization.ipynb)
- **Volume by Type**: Requests (40.2%), Incidents (39.8%), Problems (20.0%).
- **Top Categories**: Software & Application Support leads overall volume, followed by Network Connectivity and Security/Authentication.
- **Priority Ratio**: Critical (15%), High (25%), Medium (35%), Low (25%).
- **Queue/Channel Breakdown**: Self-service portal represents 42% of intakes, Email 31%, Chat 18%, Phone 9%.

---

### 10. Similarity & Cluster Analysis
- **Notebook**: [`notebooks/04_Similarity_Cluster_Insights.ipynb`](notebooks/04_Similarity_Cluster_Insights.ipynb)
- **Report**: [`reports/Summary_of_Key_Patterns_and_Problem_Clusters.md`](reports/Summary_of_Key_Patterns_and_Problem_Clusters.md)
- **High-Similarity Clusters (> 0.85)**: *Account Lockout & Auth* (0.88) and *License & Software Renewal* (0.91) exhibit highly repetitive request patterns with $>95\%$ SLA compliance.
- **Problem Clusters (< 0.75)**: *Cloud Integration & API Failures* (0.71) and *ERP / Database Timeouts* (0.74) exhibit the longest resolution times (18+ hours) and lowest SLA compliance ($\sim 74\%$).

---

### 11. Performance Trend Analysis
- **Notebook**: [`notebooks/05_Performance_Trend_Analysis.ipynb`](notebooks/05_Performance_Trend_Analysis.ipynb)
- **Resolution Speed by Priority**:
  - Critical: **4.2 hours** avg
  - High: **9.4 hours** avg
  - Medium: **15.9 hours** avg
  - Low: **24.6 hours** avg
- **Team Efficiency**: *Cloud & DevOps Ops* achieves the fastest turnaround (9.8 hrs avg, 94.2% SLA), while *Enterprise Apps Support* exhibits the longest turnaround (18.6 hrs avg, 78.5% SLA).

---

### 12. Geographic & Category Analysis
- **Notebook**: [`notebooks/06_Geographic_Category_Insights.ipynb`](notebooks/06_Geographic_Category_Insights.ipynb)
- **Report**: [`reports/Performance_Metrics_Summary.md`](reports/Performance_Metrics_Summary.md)
- **Regional Volume Concentration**: North America accounts for 39.5% of total ticket volume, EMEA for 32.6%, and APAC for 27.9%.
- **Fastest Operational Hubs**: Germany (11.2 hrs avg) and United States (12.1 hrs avg) lead overall resolution turnaround.

---

### 13. Power BI Dashboard
The native Power BI report ([`Supportlytics_IT_Support_Analytics_Dashboard.pbix`](Supportlytics_IT_Support_Analytics_Dashboard.pbix)) is organized into 6 dedicated analytical pages:

1. **Executive Dashboard**: High-level command center displaying top 5 KPIs, ticket type breakdown, status lifecycle, priority share, category rankings, and cluster scatter plots.
2. **Ticket & Category Analysis**: Detailed breakdown of category volume, priority distribution, department queues, status lifecycle, and a Category × Priority cross-tabulation matrix.
3. **Cluster & Similarity Analysis**: Evaluates NLP cluster similarity scores, ticket volume per cluster, SLA adherence by cluster, and cluster efficiency metrics.
4. **Performance Trend Analysis**: Analyzes resolution velocity across priority tiers and ticket types, team turnaround rankings, country benchmarks, and an active high-priority pending ticket watchlist.
5. **Geographic & Category Insights**: Regional concentration donuts, country volume distribution, Geographic Category Heatmap matrices, and Turnaround vs. CSAT regional bubble charts.
6. **Detailed Ticket Inspector**: Granular operational inspection tool featuring 8 interactive slicers (Country, Region, Category, Priority, Status, Team, Ticket Type, Ticket ID), filtered KPI cards, and a complete 16-column ticket record grid.

---

### 14. Streamlit Dashboard
The Streamlit application ([`app.py`](app.py)) provides a standalone, web-based analytics environment matching the multi-page Power BI structure:
- **Interactive Multi-Page Navigation**: Sidebar menu for switching between all 6 analytical modules.
- **Global Dynamic Slicers**: Interactive date ranges, Country, Region, Category, Priority, and Status dropdowns.
- **Responsive Visualizations**: Plotly bar charts, donut charts, scatter plots, and cross-tabulation heatmaps.

---

### 15. Key Insights
1. **Automation Opportunities**: Routine clusters (*Account Lockout*, *Software Renewals*) represent ~20% of aggregate volume with high similarity (>0.85), making them prime candidates for automated self-service.
2. **Operational Bottleneck**: *Enterprise Apps Support* handles complex database and ERP issues with longer debugging cycles, resulting in the highest backlog concentration.
3. **Priority Alignment**: Critical tickets are resolved in an average of 4.2 hours, adhering to high-urgency SLA targets, whereas Problems take approximately 2x longer than Incidents across all tiers.

---

### 16. Recommendations
1. **Deploy AI Self-Service / RPA**: Automate tier-1 password resets and software provisioning requests to deflect up to 20% of inbound workload.
2. **Rebalance Enterprise App Staffing**: Cross-train and reallocate Tier-2 engineers to the Enterprise Apps queue during month-end ERP reporting periods.
3. **Standardize Cloud & API Telemetry**: Enforce structured error payloads for cloud microservice failures to shorten root-cause investigation duration.
4. **Follow-the-Sun Queue Handover**: Route overflow APAC evening tickets to EMEA morning shifts to smooth queue spikes.

---

### 17. Project Structure

```
Supportlytics-IT-Support-Analytics/
│
├── data/
│   ├── IT_Support_Tickets.csv                 # Raw dataset (10,000 records)
│   └── processed/
│       └── cleaned_IT_Support_Tickets.csv     # Cleaned dataset with engineered features
│
├── notebooks/                                 # Jupyter Notebook Modules
│   ├── 01_Project_Initialization.ipynb
│   ├── 02_Data_Cleaning_Feature_Engineering.ipynb
│   ├── 03_Exploratory_Visualization.ipynb
│   ├── 04_Similarity_Cluster_Insights.ipynb
│   ├── 05_Performance_Trend_Analysis.ipynb
│   └── 06_Geographic_Category_Insights.ipynb
│
├── reports/                                   # Reports & Documentation
│   ├── Data_Dictionary.md
│   ├── Feature_Engineering_Summary.md
│   ├── Summary_of_Key_Patterns_and_Problem_Clusters.md
│   ├── Performance_Metrics_Summary.md
│   ├── Supportlytics_Comprehensive_Project_Report.md
│   ├── Supportlytics_Presentation_Slides.md
│   ├── Supportlytics_Presentation_Slides.html
│   ├── Supportlytics_Interactive_Dashboard.html
│   └── figures/                               # 12 Generated High-Res PNG Visualizations
│
├── images/                                    # UI / Dashboard Preview Screenshots
│   ├── dashboard_full_preview.png
│   ├── kpi_cards_result.png
│   ├── main_charts_result.png
│   └── performance_charts_result.png
│
├── Supportlytics_IT_Support_Analytics_Dashboard.Dataset/ # Power BI PBIP Dataset Definition
├── Supportlytics_IT_Support_Analytics_Dashboard.Report/  # Power BI PBIP Report Definition
│
├── Supportlytics_IT_Support_Analytics_Dashboard.pbix # Active Power BI Report File
├── Supportlytics_PowerBI_Data.xlsx            # Power BI Excel Data Source
├── Supportlytics_PowerBI_Data.csv             # Power BI CSV Data Source
├── Supportlytics_DAX_Measures.txt             # Reference DAX Measures
├── PowerBI_6_Page_Build_Guide.md              # Power BI Build Guide
├── app.py                                     # Streamlit Web Application
├── requirements.txt                           # Python Dependencies
├── .gitignore                                 # Git Ignore Rules
└── README.md                                  # This File
```

---

### 18. How to Run

#### Prerequisites
- Python 3.8+
- Power BI Desktop (for `.pbix` / `.pbip` reports)

#### 1. Setup Environment & Install Dependencies
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install required dependencies
pip install -r requirements.txt
```

#### 2. Run Jupyter Notebooks
```bash
jupyter notebook
# Open and run notebooks 01 through 06 sequentially in notebooks/
```

#### 3. Run Streamlit Web Application
```bash
streamlit run app.py
```

#### 4. Open Power BI Dashboard
- Double-click [`Supportlytics_IT_Support_Analytics_Dashboard.pbix`](Supportlytics_IT_Support_Analytics_Dashboard.pbix) to launch directly in **Power BI Desktop**.

---

### 19. Documentation
- [Comprehensive Final Project Report](reports/Supportlytics_Comprehensive_Project_Report.md)
- [Data Dictionary](reports/Data_Dictionary.md)
- [Feature Engineering Summary](reports/Feature_Engineering_Summary.md)
- [Summary of Key Patterns and Problem Clusters](reports/Summary_of_Key_Patterns_and_Problem_Clusters.md)
- [Performance Metrics Summary](reports/Performance_Metrics_Summary.md)
- [Power BI 6-Page Build Guide](PowerBI_6_Page_Build_Guide.md)
- [DAX Measures Reference](Supportlytics_DAX_Measures.txt)

---

### 20. Presentation
- [Interactive Slide Deck (HTML Slideshow)](reports/Supportlytics_Presentation_Slides.html) (Open in browser; navigate with `Left`/`Right` arrow keys)
- [Presentation Slide Deck (Markdown)](reports/Supportlytics_Presentation_Slides.md)

---

### 21. Future Improvements
- Implement machine learning models for predictive ticket resolution time forecasting.
- Deploy automated NLP classification models for incoming ticket triage.
- Connect live streaming APIs to Power BI Service for real-time SLA breach alerting.

---

### 22. Project Status

| Component | Status | Details |
|---|---|---|
| **Core Analytical Workflow** | Complete | All 6 Jupyter notebooks executed with zero errors. |
| **Data Cleaning & Feature Engineering** | Complete | Processed dataset created with duration and score metrics. |
| **Exploratory & Cluster Analytics** | Complete | 12 high-resolution figures generated in `reports/figures/`. |
| **Power BI Dashboard** | Complete | 6-page interactive report with DAX measures and slicers verified. |
| **Streamlit Dashboard** | Complete | Multi-page interactive application (`app.py`) verified. |
| **Documentation & Reports** | Complete | Data dictionary, feature summary, and analytical reports finalized. |
| **Presentation Materials** | Complete | Markdown deck and interactive HTML slide deck ready. |
| **Repository Packaging** | Complete | `.gitignore` configured; structure prepared for GitHub. |

---

*Last Updated: August 2026*
