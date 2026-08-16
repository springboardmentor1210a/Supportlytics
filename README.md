# Supportlytics – IT Support Team Performance Analytics

## Project

Supportlytics is an IT support analytics platform designed to transform raw customer support ticket data into meaningful operational insights. The project analyzes over 200,000 IT support tickets across categories, priorities, products, channels, regions, support queues, clusters, resolution performance, SLA compliance, escalation, and customer satisfaction.

The solution combines Python data analysis, NLP-based similarity analysis, clustering, performance analysis, geographic analysis, and Power BI to enable data-driven decision-making for IT support teams.

## Problem

IT support teams handle large volumes of tickets across different categories, priorities, regions, and support teams. Without centralized analytics, it can be difficult to identify:

- High-volume support issues
- Critical and unresolved tickets
- Teams or queues with performance gaps
- SLA breaches
- Recurring issue patterns
- Regional workload differences
- Resolution-time problems
- Customer satisfaction trends

Supportlytics addresses these challenges by converting raw ticket data into structured analytical insights and interactive dashboards.

## Objectives

The main objectives of the project are:

1. Analyze IT support ticket volume and workload patterns
2. Clean and prepare the raw dataset for analysis
3. Perform feature engineering for operational analysis
4. Analyze tickets by category, priority, type, product, channel, and status
5. Identify similar support issues using NLP and similarity analysis
6. Group related issues using clustering techniques
7. Analyze resolution performance across teams, queues, and regions
8. Identify high-priority unresolved tickets and SLA breaches
9. Analyze geographic and category-level ticket distribution
10. Develop performance metrics for comparing support operations
11. Build an interactive Power BI dashboard
12. Generate actionable insights for improving IT support operations


## Dataset

The project uses an IT customer support ticket dataset containing approximately **200,000 records**.

**Dataset contains information related to:**

- Ticket ID
- Customer details
- Product
- Category
- Issue description
- Resolution notes
- Priority
- Status
- Channel
- Region
- Customer satisfaction
- First response time
- Resolution time
- Ticket dates
- SLA breach
- Escalation
- Operating system
- Payment method
- Language
- Customer segment
- Issue complexity

**Additional analytical fields created during the project:**

- Resolution Duration
- Priority Score
- Queue
- Latitude
- Longitude
- Cluster
- Similarity Score
- Performance Score


**Data Preparation:**
- Loaded the dataset using Pandas
- Examined dataset structure and data types
- Checked missing values and data quality
- Converted date fields into appropriate formats
- Created additional analytical features

**Feature Engineering:**
- Created fields: Resolution_Duration, Priority_Score, Queue, Latitude, Longitude, Performance_Score

**NLP and Similarity Analysis:**
- Applied TF-IDF to the issue_description field
- Converted text descriptions into numerical representations
- Used cosine similarity to measure the similarity between support issues

**Clustering:**
- Applied K-Means clustering to identify groups of similar support issues
- Used analytical and text-related features
- Used resulting clusters for issue grouping, workload analysis, and recurring issue identification

**Performance Analysis:**
- Analyzed average resolution time
- First response time
- SLA breaches
- Customer satisfaction
- Performance score
- Priority-level performance
- Team and queue performance

**Geographic Analysis:**
- Analyzed regional ticket data using latitude and longitude
- Visualized ticket concentration by region
- Analyzed regional performance and category distribution across regions

## Technologies

**Programming and Data Analysis**
- Python
- Pandas
- NumPy

**Visualization**
- Matplotlib
- Seaborn

**Machine Learning and NLP**
- Scikit-learn
- TF-IDF
- Cosine Similarity
- K-Means Clustering

**Business Intelligence**
- Microsoft Power BI

**Development Environment**
- Jupyter Notebook

## Dashboard

The final Power BI dashboard contains the following pages:

- Overview
- Tickets
- Clusters
- Geography
- Performance
- Reports

The dashboard provides interactive analysis of ticket volume, support queues, clusters, geographic distribution, performance, priorities, statuses, and other operational metrics.


## Key Results

The analysis provided several important operational insights:

- **200,000** IT support tickets were analyzed
- **Average resolution time**: approximately 120.54 hours
- **Average customer satisfaction**: approximately 3.00 / 5
- **SLA compliance**: approximately 49.98%
- **Escalation rate**: approximately 50.21%
- High and urgent tickets were analyzed to identify unresolved priority issues
- Support queues and regions were compared based on resolution and performance metrics
- NLP-based similarity analysis helped identify related support issues
- Clustering provided a structured way to analyze recurring issue patterns
- Geographic analysis highlighted ticket distribution across regions
- Power BI converted analytical results into an interactive decision-support dashboard

## Google Drive Link
Access the project dataset and Jupyter Notebook files here:
https://drive.google.com/drive/folders/11CRr6wVRi5ihtV8bTGXsFtUf0uAq0BEr?usp=sharing


