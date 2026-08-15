# Supportlytics – IT Support Performance Analytics

## Infosys SpringBoard 7.0 – Data Visualization Virtual Internship

### Project Title

**Optimizing IT Support Team Performance Using Analytics (Supportlytics)**

---

## 1. Project Overview

Supportlytics is an IT support analytics project developed as part of the Infosys SpringBoard 7.0 Data Visualization Virtual Internship.

The project analyzes IT support ticket data to understand ticket patterns, resolution performance, ticket clusters, customer satisfaction, and geographic trends. The analysis was performed using Python-based data analysis and visualization techniques, followed by the development of an interactive Power BI dashboard.

---

## 2. Problem Statement

IT support teams generate a large volume of tickets across different categories, priorities, teams, and regions. Without systematic analysis, it can be difficult to identify performance gaps, recurring issue clusters, unresolved high-priority tickets, and regional workload patterns.

Supportlytics aims to transform raw support-ticket data into meaningful insights that can support data-driven IT support management.

---

## 3. Objectives

- Analyze IT support ticket patterns.
- Identify frequently occurring categories and clusters.
- Analyze ticket priority and type distributions.
- Evaluate resolution-time performance.
- Analyze similarity scores within clusters.
- Identify high-priority unresolved tickets.
- Analyze geographic and regional ticket patterns.
- Evaluate cluster size versus performance score.
- Develop an interactive Power BI dashboard.
- Generate actionable recommendations.

---

## 4. Dataset

The project uses a simulated IT Support Ticket Dataset created for internship analysis.

### Dataset Summary

- **Total Records:** 5,000
- **Columns:** 30
- **Countries:** 5
- **KPIs:** 13
- **Ticket Types:** Incident, Request, Problem
- **Priority Levels:** Low, Medium, High, Critical

### Important Fields

- `Ticket_ID`
- `Created_Date`
- `Resolution_Date`
- `Status`
- `Priority`
- `Ticket_Type`
- `Category`
- `Country`
- `Region`
- `Cluster_ID`
- `Cluster_Name`
- `Similarity_Score`
- `Team`
- `SLA_Status`
- `Customer_Satisfaction`

---

## 5. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook
- Power BI
- Microsoft Excel
- GitHub

---

## 6. Project Workflow
```text
Dataset
   ↓
Data Inspection
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Exploratory Data Analysis
   ↓
Cluster & Similarity Analysis
   ↓
Performance Analysis
   ↓
Geographic Analysis
   ↓
Power BI Dashboard
   ↓
Insights & Recommendation
```
### 7. Modules

### Module 1 – Project Initialization & Dataset Setup

**Highlights:**
- Defined project objectives and KPIs.
- Loaded the dataset using Pandas.
- Explored schema, data types, and missing values.
- Performed initial ticket distribution analysis.

### Module 2 – Data Cleaning & Feature Engineering

**Highlights:**
- Handled missing and incorrect text values.
- Removed duplicate records.
- Standardized text fields.
- Created `Resolution_Duration`.
- Created `Priority_Score`.
- Saved the processed dataset.

### Module 3 – Exploratory Visualization

**Highlights:**
- Analyzed Ticket Type Distribution.
- Identified Top Categories and Clusters.
- Analyzed Resolution Time and Similarity Score distributions.
- Visualized Priority and Queue distributions.
- Compared Priority vs Queue.

### Module 4 – Cluster & Similarity Analysis

**Highlights:**
- Analyzed average similarity scores by cluster.
- Compared cluster size with issue type.
- Visualized resolution-time distributions using boxplots.
- Analyzed Resolution Time vs Similarity Score using scatter plots.
- Identified important problem clusters.

### Module 5 – Performance Trend Analysis

**Highlights:**
- Analyzed average resolution time by priority.
- Compared resolution time across ticket types.
- Identified fastest and slowest countries.
- Compared team-level resolution performance.
- Identified high-priority unresolved tickets.
- Analyzed unresolved backlog by team.

### Module 6 – Geographic & Category-Level Insights

**Highlights:**
- Analyzed regional ticket distribution.
- Created ticket concentration heatmaps.
- Analyzed issue categories across regions.
- Evaluated cluster size vs performance score.
- Identified regional workload patterns.

**Geographic Limitation:**
- The original dataset did not contain Latitude and Longitude columns.
- Region and Category fields were used for regional-level geographic analysis.
- The analysis represents regional patterns rather than exact ticket locations.

### Module 7 – Power BI Dashboard

**Highlights:**
- Developed an interactive Power BI dashboard.
- Created KPI cards for key performance metrics.
- Visualized ticket, category, priority, and cluster insights.
- Added geographic and performance analysis.
- Added interactive slicers and filters.
- Implemented page navigation between dashboard sections.
- Presented key insights and recommendations.

---

## 8. Key Findings

**Highlights:**
- Incident, Request, and Problem tickets were relatively balanced.
- Network and Hardware were among the highest-volume categories.
- Software had the highest average cluster similarity score.
- Email was the largest cluster but had comparatively lower similarity.
- Medium-priority tickets had the longest average resolution time.
- Australia had the fastest average resolution time among the analyzed countries.
- High and Critical priority tickets represented a significant unresolved backlog.
- Europe and APAC had the highest regional ticket volumes.
- Cluster size did not show a clear relationship with performance score.

---

## 9. Recommendations

**Highlights:**
- Prioritize High and Critical unresolved tickets.
- Investigate longer resolution times for Medium-priority tickets.
- Review high-volume issue categories and clusters.
- Improve workload allocation across teams and regions.
- Monitor regional ticket concentration.
- Use Power BI KPIs for continuous performance monitoring.

---

## 10. Expected Business Impact

**Highlights:**
- Faster ticket resolution
- Improved customer satisfaction
- Better regional resource allocation
- Reduced operational workload
- More proactive support management
- Improved SLA compliance
- Better prioritization of critical support issues

---

## 11. Project Files

**Repository Structure:**

```text
Supportlytics/
    │
    ├── Dataset/
    │       ├── Supportlytics_Complete_Dataset.xlsx
    │       └── Supportlytics_Cleaned_Dataset.xlsx
    │
    ├── Notebooks/
    │       └── Supportlytics_Analysis.ipynb
    │
    ├── Visualizations/
    │       
    ├── PowerBI/
    │       └── Supportlytics_Dashboard.pbix
    │
    ├── Documentation/
    │       └── Supportlytics_Project_Documentation.pdf
    │
    └── README.md
```

## 12. Project Outcome

**Highlights:**
- Completed an end-to-end IT support analytics workflow.
- Transformed raw support ticket data into meaningful analytical insights.
- Identified important patterns in ticket volume, resolution performance, clusters, and regional distribution.
- Evaluated support performance using key analytical metrics.
- Developed an interactive Power BI dashboard for performance monitoring.
- Generated actionable insights and recommendations to support data-driven decision-making.

---

## 13. Author

**Highlights:**
- **Name:** Yona Gochipathala
- **Internship:** Infosys SpringBoard 7.0 – Data Visualization Virtual Internship
- **Project:** Optimizing IT Support Team Performance Using Analytics (Supportlytics)
- **Mentor:** Shanmukha Priya
