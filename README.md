# SUPPORTLYTICS
## IT Support Analytics & Performance Intelligence

> **Internship Project — IT Support Analytics**

[![Power BI](https://img.shields.io/badge/Power_BI-Desktop_Report-F2C811?logo=powerbi&logoColor=black)](Supportlytics_Dashboard.pbix)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](requirements.txt)
[![Dataset](https://img.shields.io/badge/Dataset-10%2C000_Tickets-0F2C59)](Supportlytics_PowerBI_Data.xlsx)
[![Documentation](https://img.shields.io/badge/Documentation-30_Pages_PDF-1E40AF)](docs/Supportlytics_Final_Project_Documentation.pdf)

---

![Executive Overview](images/Executive%20Overview.png)

---

### 1. Executive Summary & Project Overview

**Supportlytics** is an end-to-end data analytics and business intelligence system engineered to evaluate IT service desk performance, multi-channel ticket lifecycles, semantic issue clusters, SLA compliance, and regional operational efficiency. 

Built using Python for data engineering and exploratory modeling, and deployed through an interactive 6-page **Microsoft Power BI Dashboard** (`Supportlytics_Dashboard.pbix`), the platform translates 10,000 enterprise support ticket records into actionable operational intelligence.

---

### 2. Business Problem & Analytical Objectives

Enterprise IT support organizations process thousands of service requests, incident reports, and system problems monthly across global regions. Without unified business intelligence, support leadership faces:

* **Resolution Bottlenecks**: Extended ticket turnaround times across technical categories and support tiers.
* **SLA Non-Compliance**: Contractual SLA breach penalties arising from inefficient escalation workflows.
* **High-Priority Backlog**: Unresolved critical and high-priority cases accumulating without real-time triage visibility.
* **Repetitive Workload Overhead**: Recurring routine issues consuming engineering capacity without targeted deflection.
* **Geographic Imbalances**: Workload variations across regional support queues.

#### Core Project Objectives:
1. **Standardize & Cleanse**: Ingest and audit 10,000 ticket records across 38 schema attributes with 100% unique primary keys.
2. **Engineer Analytics Features**: Derive exact numerical durations (`Resolution_Hours`), priority rankings (`Priority_Score`), and date keys.
3. **Profile Workload Distributions**: Evaluate demand across ticket types (Request, Problem, Incident), 5 categories, and 4 intake channels.
4. **Analyze Issue Clusters**: Evaluate semantic similarity scores across verified clusters (Login, Network, Software).
5. **Benchmark Support Tiers & Regions**: Quantify turnaround speed, SLA compliance (50.39%), and CSAT across L1, L2, and Security teams in North America, EMEA, and APAC.
6. **Deploy Interactive Power BI Dashboard**: Build a production-grade 6-page interactive report (`Supportlytics_Dashboard.pbix`) with dynamic DAX KPI measures and multi-criteria slicers.

---

### 3. Verified Key Performance Indicators (KPIs)

All metrics are validated against the authoritative dataset (`Supportlytics_PowerBI_Data.xlsx`, Sheet: `Data`):

| KPI Metric | Verified Value | DAX Calculation / Definition | Operational Role |
|---|:---:|---|---|
| **Total Ticket Volume** | **10,000** | `COUNTROWS('Data')` | Aggregate operational demand across all channels |
| **Average Resolution Time** | **61.1032 Hours** | `AVERAGE('Data'[Resolution_Hours])` | Mean duration from ticket creation to final resolution |
| **Cluster Similarity Index** | **0.7446 (74.46%)** | `AVERAGE('Data'[Similarity_Score])` | Mean semantic similarity score across issue clusters |
| **SLA Compliance Rate** | **50.39%** | `DIVIDE(SLA Met [5,039], Total Tickets [10,000])` | Contractual SLA adherence rate (`SLA_Status = "Met"`) |
| **SLA Met Tickets** | **5,039 Tickets** | `CALCULATE([Total Tickets], 'Data'[SLA_Status] = "Met")` | Volume of tickets successfully resolved within SLA window |
| **SLA Breached Tickets** | **4,961 Tickets** | `CALCULATE([Total Tickets], 'Data'[SLA_Status] = "Breached")` | Volume of tickets exceeding contractual SLA window |
| **Average Customer Satisfaction** | **2.9818 / 5.00** | `AVERAGE('Data'[Customer_Satisfaction])` | Post-resolution user CSAT rating (1.0 to 5.0 scale) |
| **Performance Score** | **59.64 / 100** | `AVERAGE('Data'[Customer_Satisfaction]) * 20` | Standardized composite service performance score |
| **Total Unresolved Tickets** | **4,984 Tickets** | `CALCULATE([Total Tickets], Status <> "Resolved" && Status <> "Closed")` | Active queue volume (Open: 2,470 + In Progress: 2,514) |
| **High/Critical Unresolved Backlog** | **2,504 Tickets** | `CALCULATE(Unresolved, Priority IN {"Critical", "High"})` | High-risk active cases requiring prioritized triage |

---

### 4. Verified Workload Distributions

#### Ticket Types (ITIL Classification)
* **Request**: `3,358 tickets (33.58%)` — Standard service requests and user provisioning.
* **Problem**: `3,342 tickets (33.42%)` — Root-cause technical investigations.
* **Incident**: `3,300 tickets (33.00%)` — Unplanned service interruptions and outages.

#### Technical Categories
* **Security**: `2,068 tickets (20.68%)` — Access control, MFA, authentication, firewall rules.
* **Hardware**: `2,014 tickets (20.14%)` — Laptop repairs, peripherals, connectivity hardware.
* **Software**: `1,996 tickets (19.96%)` — Application bugs, licensing, client software errors.
* **Email**: `1,985 tickets (19.85%)` — Mailbox quotas, Outlook sync, routing configuration.
* **Network**: `1,937 tickets (19.37%)` — VPN access, Wi-Fi authentication, DNS resolution.

#### Verified Issue Clusters
| Cluster Name | Ticket Volume | Share (%) | Average Similarity | Average Resolution Time | SLA Compliance Rate |
|---|:---:|:---:|:---:|:---:|:---:|
| **Network** | 3,370 | 33.70% | 0.7426 | 61.6065 Hours | 50.86% (1,714 Met) |
| **Software** | 3,346 | 33.46% | 0.7477 | 60.2836 Hours | 50.24% (1,681 Met) |
| **Login** | 3,284 | 32.84% | 0.7435 | 61.4219 Hours | 50.06% (1,644 Met) |

#### Verified Support Teams
* **L1 Support**: `3,365 tickets (33.65%)` — Mean resolution: `61.1807 hrs` | SLA Met: `51.62% (1,737)` | CSAT: `2.9845 / 5`
* **L2 Support**: `3,358 tickets (33.58%)` — Mean resolution: `60.7980 hrs` | SLA Met: `49.40% (1,659)` | CSAT: `2.9821 / 5`
* **Security**: `3,277 tickets (32.77%)` — Mean resolution: `61.3365 hrs` | SLA Met: `50.14% (1,643)` | CSAT: `2.9789 / 5`

#### Geographic Regions & Hub Countries
* **North America**: `4,047 tickets (40.47%)` | USA: `2,022` (60.15 hrs avg), Canada: `2,025` (61.23 hrs avg)
* **EMEA**: `3,910 tickets (39.10%)` | UK: `1,975` (60.64 hrs avg), Germany: `1,935` (61.70 hrs avg)
* **APAC**: `2,043 tickets (20.43%)` | India: `2,043` (61.81 hrs avg)

---

### 5. Microsoft Power BI Dashboard

The primary deliverable of this project is the native Power BI report ([`Supportlytics_Dashboard.pbix`](Supportlytics_Dashboard.pbix)), structured into six dedicated analytical pages:

#### Page 1 — Executive Overview
High-level operational command center featuring primary KPI cards, Ticket Type donut chart, Status lifecycle breakdown, Priority distribution bar chart, Category volume rankings, and global interactive slicers.
![Executive Overview](images/Executive%20Overview.png)

---

#### Page 2 — Ticket & Category Analysis
Workload composition view displaying category volume rankings, multi-channel intake mix (Email, Web Portal, Live Chat, Phone), departmental demand allocation, and a Category × Priority cross-tabulation matrix.
![Ticket & Category Analysis](images/Ticket%20&%20Category%20Analysis.png)

---

#### Page 3 — Cluster & Similarity Analysis
Semantic cluster exploration module analyzing ticket volumes across Login, Network, and Software clusters, Similarity Level distribution (Low, Medium, High), Cluster × Ticket Type stacked bars, and Turnaround vs. CSAT scatter analysis.
![Cluster & Similarity Analysis](images/Cluster%20&%20Similarity%20Analysis.png)

---

#### Page 4 — Performance Analysis
Turnaround velocity diagnostics comparing resolution duration by Priority level, Support Tier benchmarks (L1, L2, Security), Country turnaround rankings, and the High/Critical Unresolved Backlog monitor tracking 2,504 urgent pending cases.
![Performance Analysis](images/Performance%20Analysis.png)

---

#### Page 5 — Geographic Analysis
Global operational footprint mapping regional volume distribution across North America, EMEA, and APAC, country ticket volume bars, Regional Category concentration heatmaps, and spatial coordinate mapping using Latitude and Longitude.
![Geographic Analysis](images/Geographic%20Analysis.png)

---

#### Page 6 — Ticket Details
Granular investigation and audit tool equipped with an 8-slicer filter pane (Country, Region, Category, Priority, Status, Team, Ticket Type, Ticket ID), summary KPI metric cards, and a responsive tabular grid of individual ticket records.
![Ticket Details](images/Ticket%20Details.png)

---

### 6. Power BI Technology & Modeling Architecture

The Power BI solution is built on enterprise business intelligence best practices:

* **Data Model Architecture**: Star-Schema design with a central fact table (`Data`) connected via an active `1:*` single-direction relationship to a dedicated `Calendar` date dimension (`Calendar[Date] -> Data[Created_Date]`).
* **Date Intelligence**: Dedicated `Calendar` table generated via DAX `CALENDAR()`, featuring `Year`, `Month Number`, `Month Name`, `Quarter`, and `Year-Month` with explicit month sorting.
* **DAX KPI Engine**: Centralized DAX measures providing dynamic context-filtered evaluations for volume, duration, similarity, SLA adherence, and backlog tracking.
* **Interactive Visual Capabilities**: Synchronized cross-filtering, multi-select slicers, customized KPI cards, donut charts, horizontal/vertical bar charts, scatter matrices, and tabular audit grids.

#### Primary DAX Measures Reference:
1. `Total Tickets = COUNTROWS('Data')`
2. `Average Resolution Time (Hours) = AVERAGE('Data'[Resolution_Hours])`
3. `Cluster Similarity Index = AVERAGE('Data'[Similarity_Score])`
4. `Performance Score = AVERAGE('Data'[Customer_Satisfaction]) * 20`
5. `SLA Compliance % = DIVIDE(CALCULATE(COUNTROWS('Data'), 'Data'[SLA_Status] = "Met"), [Total Tickets], 0)`
6. `SLA Compliance Rate = DIVIDE(CALCULATE(COUNTROWS('Data'), 'Data'[SLA_Status] = "Met"), [Total Tickets], 0)`
7. `Most Frequent Category = VAR T = TOPN(1, SUMMARIZE('Data', 'Data'[Category], "C", [Total Tickets]), [C], DESC) RETURN CONCATENATEX(T, 'Data'[Category], ", ")`
8. `Top Performing Region = VAR R = TOPN(1, FILTER(ADDCOLUMNS(VALUES('Data'[Region]), "A", [Average Resolution Time (Hours)]), NOT ISBLANK([A])), [A], ASC) RETURN CONCATENATEX(R, 'Data'[Region], ", ")`
9. `Total Unresolved Tickets = CALCULATE([Total Tickets], 'Data'[Status] <> "Resolved", 'Data'[Status] <> "Closed")`
10. `High Priority Unresolved Tickets = CALCULATE([Total Tickets], 'Data'[Priority] IN {"Critical", "High"}, 'Data'[Status] <> "Resolved", 'Data'[Status] <> "Closed")`
11. `Average Customer Satisfaction = AVERAGE('Data'[Customer_Satisfaction])`

#### Supporting DAX Measures:
* `Resolved Tickets = CALCULATE([Total Tickets], 'Data'[Status] = "Resolved")`
* `Open Tickets = CALCULATE([Total Tickets], 'Data'[Status] = "Open")`
* `Closed Tickets = CALCULATE([Total Tickets], 'Data'[Status] = "Closed")`
* `SLA Met Tickets = CALCULATE([Total Tickets], 'Data'[SLA_Status] = "Met")`
* `SLA Breached Tickets = CALCULATE([Total Tickets], 'Data'[SLA_Status] = "Breached")`
* `Reopened Tickets = CALCULATE([Total Tickets], 'Data'[Reopened] = 1 || 'Data'[Reopened] = "Yes")`

---

### 7. Authoritative Dataset & Schema Architecture

* **Power BI Authoritative Source**: [`Supportlytics_PowerBI_Data.xlsx`](Supportlytics_PowerBI_Data.xlsx) / [`Supportlytics_PowerBI_Data.csv`](Supportlytics_PowerBI_Data.csv) (10,000 rows × 38 columns).
* **Raw Historical Dataset**: [`IT_Support_Tickets.csv`](IT_Support_Tickets.csv) / [`data/IT_Support_Tickets.csv`](data/IT_Support_Tickets.csv) (10,000 records).
* **Processed Dataset**: [`data/processed/cleaned_IT_Support_Tickets.csv`](data/processed/cleaned_IT_Support_Tickets.csv).

#### 38-Column Schema Structure:
* **Ticket Lifecycle**: `Ticket_ID` (100% Unique PK), `Created_Date`, `Resolution_Date`, `First_Response_Date`, `Status`, `Resolution_Code`, `Resolution_Notes`
* **Classification**: `Priority`, `Priority_Score`, `Ticket_Type`, `Category`, `Product`, `Tags`, `Description`
* **Assignment & Intake**: `Assigned_Agent`, `Team`, `Department`, `Channel`, `Escalation_Level`
* **Service Outcomes**: `SLA_Status`, `Reopened`, `Customer_Satisfaction`, `Resolution_Duration`, `Resolution_Hours`
* **Similarity & Clusters**: `Cluster_ID`, `Cluster_Name`, `Similarity_Score`, `Similarity_Level`
* **Geographic Fields**: `Country`, `Region`, `Latitude`, `Longitude`
* **Context & Platform**: `Device_Type`, `Operating_System`
* **Date Helper Fields**: `Created_Year`, `Created_Month`, `Created_Month_Number`

---

### 8. Analytical Python Notebooks

The repository includes six structured Jupyter notebooks establishing data engineering, exploratory profiling, and statistical baselines:

1. [`01_Project_Initialization.ipynb`](01_Project_Initialization.ipynb): Environment setup, dependency validation, raw data ingestion, and schema inspection.
2. [`02_Data_Cleaning_Feature_Engineering.ipynb`](02_Data_Cleaning_Feature_Engineering.ipynb): Missing value imputation, datetime standardization, `Resolution_Hours` computation, and `Priority_Score` encoding.
3. [`03_Exploratory_Visualization.ipynb`](03_Exploratory_Visualization.ipynb): Statistical distribution analysis across ticket types, categories, intake channels, and status lifecycles.
4. [`04_Similarity_Cluster_Insights.ipynb`](04_Similarity_Cluster_Insights.ipynb): Cluster similarity evaluation across Login, Network, and Software issue groups.
5. [`05_Performance_Trend_Analysis.ipynb`](05_Performance_Trend_Analysis.ipynb): Resolution duration benchmarking across support tiers (L1, L2, Security), priority tiers, and SLA outcomes.
6. [`06_Geographic_Category_Insights.ipynb`](06_Geographic_Category_Insights.ipynb): Geospatial distribution and regional category concentration analysis across North America, EMEA, and APAC.

---

### 9. Project Documentation

The complete, professional **30-page project documentation** is available in the repository:

📄 **[Download Supportlytics Final Project Documentation (PDF)](docs/Supportlytics_Final_Project_Documentation.pdf)**

#### Documentation Overview:
* **Part 1 — Context & Foundations**: Project Overview, Business Problem, Objectives, Analytical Workflow.
* **Part 2 — Data Engineering & Modeling**: Dataset Overview, Data Dictionary (38 attributes), Data Preparation, Star-Schema Model, Calendar Dimension, DAX Measure Architecture (11 Primary + 6 Supporting).
* **Part 3 — Exploratory & Performance Analysis**: Ticket Type & Category Analysis, Priority & Lifecycle Health, Cluster & Similarity Analysis, Support Tier Turnaround, SLA Adherence & CSAT, Geographic Benchmarks.
* **Part 4 — Power BI Dashboard Architecture**: Dedicated documentation and high-resolution figures for all 6 dashboard views (Figures 23–28).
* **Part 5 — Strategic Insights & Roadmap**: Key Findings, 7 Proposed Strategic Recommendations, Limitations, and 5-Pillar Future Enhancements.

---

### 10. Key Insights

1. **Baseline Turnaround Velocity**: Mean resolution duration stands at **61.1032 hours** across the 10,000-ticket log, showing consistent turnaround across priority levels (Critical: 60.98 hrs, Medium: 60.56 hrs, High: 61.41 hrs, Low: 61.48 hrs).
2. **SLA Compliance Distribution**: Exactly **5,039 tickets (50.39%)** met contractual SLA windows, while **4,961 tickets (49.61%)** breached SLA, highlighting opportunities for queue workflow optimization.
3. **Active High-Priority Backlog**: Out of 4,984 total unresolved tickets (Open + In Progress), exactly **2,504 tickets** are classified as High or Critical priority, representing an essential focus area for daily queue triage.
4. **Issue Cluster Cohesion**: Three verified issue clusters (**Network: 3,370**, **Software: 3,346**, **Login: 3,284**) exhibit a high mean similarity index of **0.7446**, demonstrating recurring patterns suitable for standardized knowledge bases.
5. **Support Tier Allocation**: Workload is evenly distributed across **L1 (3,365)**, **L2 (3,358)**, and **Security (3,277)** teams, with L1 achieving 51.62% SLA compliance and L2 averaging 60.80 hours resolution.

---

### 11. Proposed Strategic Recommendations

*Based on empirical data findings (proposed for operational improvement):*

1. **SLA Breach Threshold Alerting**: Configure automated notification triggers when open high-priority tickets reach 75% of their SLA window.
2. **High-Priority Queue Prioritization**: Implement queue routing rules to ensure the 2,504 High and Critical unresolved tickets are triaged ahead of lower-urgency requests.
3. **Targeted Knowledge Base Development**: Develop structured self-service articles and guided troubleshooting for high-similarity Login (0.7435 similarity) and Software (0.7477 similarity) inquiries.
4. **Support Tier Workload Balancing**: Align tier capacity with category demand, ensuring specialized routing for Security and Software cases.
5. **Customer Feedback Follow-Up**: Establish proactive follow-up protocols for low-CSAT resolutions to identify specific service friction points.

---

### 12. Proposed Future Roadmap

*Proposed future technical enhancements:*

* **Automated Cloud Refresh**: Configure scheduled dataset refresh via Power BI Gateway connected directly to enterprise ticketing databases.
* **Predictive Resolution Modeling**: Train regression models to forecast expected resolution duration at ticket creation.
* **SLA Breach Risk Classification**: Develop machine learning models to identify tickets at high risk of SLA breach.
* **Automated NLP Ticket Triage**: Implement natural language processing for automated initial category and priority tagging.

---

### 13. Repository Structure

```
Supportlytics-IT-Support-Analytics/
│
├── Supportlytics_Dashboard.pbix               # Final 6-Page Power BI Dashboard
├── Supportlytics_PowerBI_Data.xlsx            # Authoritative Power BI Excel Data Source (38 Cols)
├── Supportlytics_PowerBI_Data.csv             # Authoritative Power BI CSV Data Source (38 Cols)
├── IT_Support_Tickets.csv                     # Raw IT Support Tickets Dataset (10,000 Records)
├── Supportlytics_DAX_Measures.txt             # Reference DAX Measures Definition File
│
├── docs/                                      # Project Documentation
│   └── Supportlytics_Final_Project_Documentation.pdf   # Complete 30-Page Project Documentation PDF
│
├── images/                                    # Verified Power BI Dashboard Screenshots
│   ├── Executive Overview.png
│   ├── Ticket & Category Analysis.png
│   ├── Cluster & Similarity Analysis.png
│   ├── Performance Analysis.png
│   ├── Geographic Analysis.png
│   └── Ticket Details.png
│
├── notebooks/                                 # Jupyter Analytics Notebooks
│   ├── 01_Project_Initialization.ipynb
│   ├── 02_Data_Cleaning_Feature_Engineering.ipynb
│   ├── 03_Exploratory_Visualization.ipynb
│   ├── 04_Similarity_Cluster_Insights.ipynb
│   ├── 05_Performance_Trend_Analysis.ipynb
│   └── 06_Geographic_Category_Insights.ipynb
│
├── data/                                      # Data Directory
│   ├── IT_Support_Tickets.csv                 # Raw dataset
│   └── processed/
│       └── cleaned_IT_Support_Tickets.csv     # Cleaned and feature-engineered dataset
│
├── reports/                                   # Supplemental Reference Reports & Markdown Notes
│   ├── Data_Dictionary.md
│   ├── Feature_Engineering_Summary.md
│   ├── Performance_Metrics_Summary.md
│   ├── Summary_of_Key_Patterns_and_Problem_Clusters.md
│   └── Supportlytics_Comprehensive_Project_Report.md
│
├── requirements.txt                           # Python Dependencies
├── LICENSE                                    # Project License
├── .gitignore                                 # Git Ignore Rules
└── README.md                                  # Project Readme
```

---

### 14. How to Open & Explore

#### 1. Open the Power BI Dashboard
1. Ensure **Microsoft Power BI Desktop** is installed.
2. Open [`Supportlytics_Dashboard.pbix`](Supportlytics_Dashboard.pbix) directly in Power BI Desktop.
3. Interact with report pages, slicers, and cross-highlighting visual containers.

#### 2. Run the Python Analytics Notebooks
```bash
# Clone the repository
git clone https://github.com/springboardmentor1210a/Supportlytics.git

# Navigate to project directory
cd Supportlytics

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate       # Windows
source .venv/bin/activate    # macOS/Linux

# Install required dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook
```

---

*Supportlytics — IT Support Analytics & Performance Intelligence | Version 1.0 Final Release*
