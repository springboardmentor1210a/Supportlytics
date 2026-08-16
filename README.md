

> **Optimizing IT Support Team Performance Using Advanced Analytics**

Supportlytics is an end-to-end IT support analytics project that analyzes ticket data to identify performance trends, optimize resolution times, understand recurring issue patterns, compare regional performance, and support better resource allocation.

## 📌 Project Objective

The project analyzes IT support ticket data to uncover patterns in:
- Ticket volume
- Issue types and categories
- Priority and status
- Resolution time
- Customer satisfaction
- Support queues
- Geographic distribution
- Similar issue clusters

The final insights are presented through an interactive Power BI dashboard and used to recommend improvements in IT support workflow and resource allocation. The project requirements explicitly cover data acquisition, cleaning, EDA, cluster/similarity analysis, performance analysis, geographic insights, dashboard development, documentation and presentation. 

## 🎯 Project Scope

- **Data Preprocessing** – Clean and prepare IT support ticket data.
- **Exploratory Analysis** – Analyze ticket trends, priorities and categories.
- **Cluster Analysis** – Identify similar issues and problem clusters.
- **Geographic Analysis** – Analyze regional ticket distribution and performance.
- **Performance Analysis** – Evaluate resolution time, priority and CSAT.
- **Interactive Visualization** – Develop interconnected Power BI dashboards.
- **Executive Reporting** – Present key insights and recommendations.

## 📊 Dataset

The project uses a synthetic IT support ticket dataset containing **100,000 rows and 20 original columns**.

Important columns include:

| Column | Description |
|---|---|
| `ticket_id` | Unique ticket identifier |
| `created_at` | Ticket creation timestamp |
| `customer_id` | Customer identifier |
| `customer_segment` | Customer segment |
| `channel` | Support channel |
| `product_area` | Product/functional area |
| `issue_type` | Issue category |
| `priority` | Low, Medium, High or Urgent |
| `status` | Ticket status |
| `sla_plan` | Service-level plan |
| `resolution_time_hours` | Resolution duration |
| `reopened` | Reopened-ticket indicator |
| `customer_sentiment` | Customer sentiment |
| `csat_score` | Customer satisfaction |
| `platform` | Customer platform |
| `region` | Geographic region |

## 🛠️ Tech Stack

**Data Analysis:** Python, Pandas, NumPy, Jupyter Notebook

**Visualization:** Matplotlib, Seaborn, Plotly, Power BI

**Documentation:** Markdown, Jupyter Notebook, Word/PDF

**Version Control:** GitHub

## 🔄 Project Workflow

<img width="1611" height="720" alt="image" src="https://github.com/user-attachments/assets/a0ebfa23-8531-4575-b6f4-3b4b3064eac6" />


# 📅 Week-Wise Progress

## Week 1–2: Project Initialization & Data Preparation

### Module 1 – Project Initialization and Dataset Setup
- Defined objectives, KPIs and workflow.
- Loaded the CSV dataset using Pandas.
- Inspected schema, data types and missing values.
- Calculated initial ticket distributions.

### Module 2 – Data Cleaning and Feature Engineering
- Handled missing text fields.
- Standardized text values.
- Checked duplicate records.
- Created `Resolution_Duration`.
- Created `Priority_Score`.
- Created queue and analytical cluster mappings.
- Saved processed data.

## Week 3–4: Exploratory & Cluster Analysis

### Module 3 – Exploratory Data Analysis
Analyzed:
- Ticket distribution by issue type
- Ticket distribution by priority
- Ticket status
- Customer segment
- Support channel
- Queue workload

### Module 4 – Similarity & Cluster Insights
Analyzed:
- Cluster size
- Issue concentration by cluster
- Priority mix
- Similarity scores
- Resolution performance
- Customer satisfaction
- Performance gaps

The internship requirements call for a minimum of eight visualizations and summary of key patterns/problem clusters.

## Week 5–6: Performance & Geographic Analysis

### Module 5 – Performance Trend Analysis
Analyzed:
- Average resolution time by priority
- Average resolution time by issue type
- Average resolution time by region
- Average resolution time by queue
- High-priority unresolved tickets
- Reopened tickets
- Customer satisfaction

### Module 6 – Geographic & Category-Level Insights
Analyzed:
- Regional ticket concentration
- Issue categories by region
- Geographic ticket distribution
- Regional resolution performance
- Regional customer satisfaction
- Cluster size vs performance/similarity

## Week 7–8: Dashboard, Documentation & Presentation

### Module 7 – Dashboard / Report Preparation
Developed six Power BI pages:
1. Overview
2. Tickets Analysis
3. Cluster Intelligence
4. Geographical Insights
5. Performance Analysis
6. Executive Report

### Module 8 – Documentation & Presentation
Completed:
- Final report
- README
- Dashboard
- Presentation
- Key insights
- Recommendations
- GitHub-ready project structure

# 🧹 Data Preprocessing

Missing values identified in the project include:

| Column | Missing Values |
|---|---:|
| `resolution_summary` | 39,887 |
| `resolution_time_hours` | 39,887 |
| `region` | 19,997 |

Text fields were standardized and missing text values were handled using `Unknown` where appropriate. Duplicate records were checked; the initial dataset contained no duplicate rows.

# ⚙️ Feature Engineering

### Resolution Duration
`Resolution_Duration` was created from the available resolution-time field.

### Priority Score

| Priority | Score |
|---|---:|
| Low | 1 |
| Medium | 2 |
| High | 3 |
| Urgent | 4 |

### Analytical Clusters

| Cluster | Main Issue Group |
|---|---|
| Cluster 0 | Billing |
| Cluster 1 | Security |
| Cluster 2 | Account access / How-to |
| Cluster 3 | Performance / Bug |
| Cluster 4 | Feature requests |
| Cluster 5 | Other |

> Cluster and similarity values are based on the mappings implemented in the project notebook.

# 📈 Exploratory Data Analysis

Important visualizations include:
- Ticket distribution by issue type
- Ticket distribution by priority
- Tickets by status
- Tickets by customer segment
- Tickets by support channel
- Tickets by queue
- Ticket distribution by cluster

# 🔬 Cluster & Similarity Analysis

The dashboard reports:
- **Total Clusters:** 6
- **Largest Cluster:** Cluster 2
- **Highest Resolution Cluster:** Cluster 4
- **Average Similarity Index:** 0.81

The analysis compares cluster size, issue concentration, priority mix, resolution time and customer satisfaction.

# 🌍 Geographic Analysis

The geographic analysis compares:
- Regional ticket volume
- Issue categories by region
- Resolution performance
- Customer satisfaction
- Geographic issue distribution

Representative regional coordinates are used for visualization and should not be interpreted as precise customer locations.

# ⏱️ Performance Analysis

| KPI | Value |
|---|---:|
| Total Tickets | 100,000 |
| Average Resolution Time | 45.01 hours |
| Average CSAT | 2.24 |
| Reopened Tickets | 5,045 |
| Reopened Rate | 0.05 |
| Total Clusters | 6 |
| Average Similarity Index | 0.81 |

The dashboard also highlights approximately **13K high-priority unresolved tickets**, requiring closer monitoring.

# 📊 Power BI Dashboard

### 1. Overview
High-level KPIs, issue distribution, priority mix, queue workload, similarity index and regional CSAT.
<img width="1335" height="743" alt="Overview" src="https://github.com/user-attachments/assets/43d6dfa4-10f5-4f9d-b35e-858a390c09ae" />




### 2. Tickets Analysis
Tickets by channel, status, queue, customer segment, issue type and priority, plus reopened and total-ticket KPIs.
<img width="1340" height="741" alt="Tickets Analysis" src="https://github.com/user-attachments/assets/3690d6f1-da1c-4ced-b41a-179036ead898" />



### 3. Cluster Intelligence
Largest cluster, highest-resolution cluster, cluster size, similarity score, priority mix and issue concentration.
<img width="1342" height="752" alt="Cluster Intelligence" src="https://github.com/user-attachments/assets/fb7aeff3-923b-4d6e-bf1d-41317d559da9" />



### 4. Geographical Insights
Regional ticket distribution, maps, regional CSAT and geographic issue distribution.
<img width="1341" height="748" alt="Geographical Insights" src="https://github.com/user-attachments/assets/f303f6c7-3b19-4c7c-86d6-e83a718bf955" />



### 5. Performance Analysis
Resolution time by priority, high-priority unresolved issues, reopened rate, CSAT, queue performance and regional performance.
<img width="1332" height="741" alt="Performance Analysis" src="https://github.com/user-attachments/assets/2e154109-d5b8-49f4-b187-b0eb92f4758c" />



### 6. Executive Report
Management-level KPIs, regional performance, critical ticket overview, performance gaps, key insights and recommendations.
<img width="1328" height="744" alt="Executive Report" src="https://github.com/user-attachments/assets/4bbbdbab-7d61-4dc1-b93e-d27bc29f6f06" />



# 💡 Key Insights

1. **MEA has the highest ticket volume**, indicating greater support demand in the region.
2. **EU has the fastest average resolution time**, indicating comparatively efficient ticket handling.
3. **APAC has the highest cluster similarity/performance score** in the final reporting view.
4. **High and urgent tickets require closer monitoring** because they represent critical support cases.
5. **Cluster-level analysis reveals different issue concentrations**, helping identify recurring support patterns.
6. **5,045 tickets were reopened**, highlighting an opportunity to improve first-time resolution.
7. **Average CSAT is 2.24**, indicating an opportunity to improve customer experience.

# 🎯 Recommendations

- Review staffing and workload allocation for **MEA**.
- Strengthen escalation and monitoring for **High/Urgent** tickets.
- Study efficient workflows in **EU** and replicate suitable practices.
- Use cluster-based knowledge bases and routing.
- Investigate root causes of reopened tickets.
- Improve resolution quality and customer experience to raise CSAT.
- Balance workloads across support queues.

# 📁 Recommended GitHub Structure

```text
Supportlytics/
│
├── README.md
├── data/
│   ├── synthetic_it_support_tickets.csv
│   └── processed_it_support_tickets.csv
├── notebooks/
│   └── internDV.ipynb
├── dashboard/
│   └── Supportlytics.pbix
├── visuals/
│   ├── overview.png
│   ├── tickets_analysis.png
│   ├── cluster_intelligence.png
│   ├── geographical_insights.png
│   ├── performance_analysis.png
│   └── executive_report.png
├── report/
│   └── Supportlytics_Final_Internship_Report.pdf
└── presentation/
    └── Supportlytics_Final_Presentation.pptx
```

> **Important:** If the dataset cannot be publicly shared, do not upload the raw dataset to GitHub. Upload only permitted files or a sample/data dictionary.

# ▶️ How to Run

```bash
git clone https://github.com/<your-username>/Supportlytics.git
cd Supportlytics
pip install pandas numpy matplotlib seaborn plotly
```

Open:

```text
notebooks/internDV.ipynb
```

For the dashboard, open:

```text
dashboard/Supportlytics.pbix
```

Refresh the data source if required.

# 📦 Deliverables

- Cleaned/processed dataset
- Feature engineering
- Exploratory analysis
- Cluster and similarity analysis
- Geographic analysis
- Performance analysis
- Interactive Power BI dashboard
- Executive report
- Final documentation
- Presentation
- GitHub repository

# 🚀 Future Scope

- Real-time IT support monitoring
- Automated critical-ticket alerts
- Predictive resolution-time modeling
- Ticket escalation prediction
- Sentiment-based prioritization
- Automated periodic reports
- Integration with live IT service-management systems

# 🏁 Conclusion

Supportlytics demonstrates an end-to-end approach to IT support analytics. The project transforms raw ticket data into structured insights covering workload, issue categories, priorities, clusters, regions, resolution performance and customer satisfaction.

The final Power BI dashboard provides an interactive way to explore these dimensions and supports data-driven recommendations for improving IT support efficiency, resource allocation and customer experience.

## 👩‍💻 Author

**Varsha B O**  
B.E. – Data Science  
BIET Davangere, Karnataka

