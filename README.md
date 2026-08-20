# Supportlytics – IT Support Ticket Analytics

## Project

Supportlytics is an IT support ticket analytics project developed to analyse customer support-ticket data and identify patterns related to ticket categories, priorities, resolution time, customer satisfaction, regions, support queues, similarity, and ticket clusters.

The project was completed through four milestones, starting with data exploration and preparation, followed by data cleaning and feature preparation, advanced analysis including similarity and clustering, and finally the development of an interactive Power BI dashboard.

The overall workflow combines Python, Pandas, Jupyter Notebook, machine learning techniques, similarity analysis, clustering, and Microsoft Power BI.

---

## Project Workflow

The project was completed in four major milestones:

### Milestone 1 – Data Exploration and Initial Analysis

In Milestone 1, I started by loading and exploring the IT support ticket dataset.

The main work completed during this milestone included:

- Loading the dataset using Pandas
- Understanding the dataset structure
- Checking the number of rows and columns
- Inspecting column names
- Examining data types
- Performing initial statistical analysis
- Checking the distribution of important variables
- Analysing categorical and numerical fields
- Exploring ticket-related attributes such as:
  - Product
  - Issue Type
  - Priority
  - Region
  - Channel
  - Customer Sentiment
  - CSAT Score
  - Resolution Time
- Checking the distribution and patterns in the support-ticket data
- Creating exploratory visualizations to understand the dataset

### Milestone 1 Outcome

The outcome of Milestone 1 was an initial understanding of the dataset, its structure, important variables, distributions, and major patterns that could be explored further in the following milestones.

---

## Milestone 2 – Data Cleaning and Feature Preparation

In Milestone 2, I prepared the dataset for further analysis by performing data cleaning and feature preparation.

The main work completed during this milestone included:

- Handling missing values by filling the required missing values
- Checking and handling duplicate records
- Verifying data types
- Preparing categorical and numerical fields
- Creating required encoded features
- Preparing features for further analytical and clustering work
- Creating the required analytical fields
- Preparing the dataset for advanced analysis
- Creating ticket clusters using the prepared features

### Feature Preparation

The required features were prepared for further analysis and visualization.

The important analytical fields included:

- Resolution Duration
- Priority-related encoded features
- Category-related features
- Cluster
- Other required analytical features

### Clustering

Clustering was also performed during Milestone 2.

The purpose of clustering was to group tickets with similar characteristics into different clusters. These clusters were later used for further analysis and visualization.

### Milestone 2 Outcome

The outcome of Milestone 2 was a cleaned and prepared dataset with the required features and clusters, which was then used for the advanced analysis in Milestone 3.

---

## Milestone 3 – Advanced Analysis

In Milestone 3, I performed deeper analysis using the cleaned and prepared dataset from Milestone 2.

The main areas covered in this milestone included:

### Similarity Analysis

- Analysed similarity between support tickets
- Generated similarity scores
- Used ticket-related information to identify similar support issues
- Prepared similarity results for further analysis

### Cluster Analysis

- Analysed the clusters created during the previous milestone
- Compared ticket groups based on their cluster information
- Examined cluster size and performance
- Used clusters to understand patterns among similar support tickets

### Resolution Performance Analysis

- Analysed resolution duration
- Compared resolution time across different priorities
- Compared resolution time across issue types
- Analysed resolution performance across regions
- Analysed support queue performance

### Regional Analysis

- Analysed ticket distribution across regions
- Compared ticket volume between regions
- Compared resolution performance across regions
- Analysed customer satisfaction across regions
- Studied regional issue patterns

### Performance Analysis

- Analysed performance scores
- Compared performance between different groups
- Examined the relationship between resolution time and performance
- Compared customer satisfaction and operational performance

### Milestone 3 Outcome

The outcome of Milestone 3 was a set of advanced analytical results covering ticket similarity, clusters, resolution performance, regional patterns, and support performance. These results were then brought into Power BI for dashboard development.

---

## Milestone 4 – Power BI Dashboard

In Milestone 4, I converted the analysis from the previous milestones into an interactive Power BI dashboard.

The dashboard was organised into different pages, with each page focusing on a specific area of the analysis.

### Page 1 – Executive Overview

The Executive Overview page provides a high-level summary of the support-ticket performance.

The page includes:

- KPI cards
- Average CSAT
- Average Performance Score
- Average Resolution Time
- Average Similarity Score
- Ticket category analysis
- Priority distribution
- Regional ticket volume
- Ticket trends

This page provides a quick overall understanding of the support-ticket workload and performance.

---

### Page 2 – Resolution Time Analysis

This page focuses on ticket resolution performance.

The analysis includes:

- Average resolution time
- Resolution time by priority
- Resolution time by issue type
- Resolution time by region
- Resolution time by support queue
- Resolution trends

This page helps identify which areas require more time to resolve tickets and which queues or regions are resolving tickets faster.

---

### Page 3 – Ticket Categories

This page focuses on understanding the distribution of support tickets.

The analysis includes:

- Ticket category distribution
- Ticket status
- Support queue distribution
- Priority distribution
- Category trends

This page helps identify the categories generating higher ticket volumes and understand how the support workload is distributed.

---

### Page 4 – Geographic Insights

This page focuses on the geographic distribution of support tickets.

The analysis includes:

- Regional ticket volume
- Geographic ticket distribution
- Region-wise issue categories
- Regional workload comparison

This page helps identify regions with higher support-ticket volumes and understand regional issue patterns.

---

### Page 5 – Cluster and Similarity Analysis

This page presents the cluster and similarity results generated during the previous analysis.

The analysis includes:

- Cluster distribution
- Similarity scores
- Cluster size
- Cluster performance
- Resolution duration comparison
- Ticket group comparison

This page helps understand how similar support tickets are grouped and how different ticket clusters perform.

---

### Page 6 – Regional Performance

This page focuses on comparing the performance of different regions.

The analysis includes:

- Regional ticket volume
- Average resolution time
- Average CSAT
- Average performance score
- Regional performance comparison

This page helps identify differences in workload, customer satisfaction, resolution time, and overall performance between regions.

---

### Page 7 – Insights and Recommendations

The final page summarises the major findings obtained from the complete dashboard analysis.

The key areas covered include:

- High-volume ticket categories
- Resolution-time differences
- Regional workload differences
- Cluster performance differences
- Support queue performance
- Customer satisfaction patterns

Based on these findings, recommendations were provided for:

- Focusing resources on high-volume regions
- Improving categories with longer resolution times
- Monitoring low-performing clusters
- Optimising support queue distribution
- Improving overall support performance

---

## Overall Project Outcome

The project progressed from initial data exploration to data preparation, advanced analysis, and finally dashboard development.

The complete workflow was:

**Dataset → Data Exploration → Data Cleaning → Feature Preparation → Clustering → Similarity Analysis → Performance Analysis → Regional Analysis → Power BI Dashboard → Insights & Recommendations**

The final Power BI dashboard brings together the results from all four milestones and provides an interactive way to analyse support-ticket workload, resolution performance, categories, geographic distribution, clusters, similarity, and regional performance.

---

## Technologies Used

### Programming and Data Analysis

- Python
- Pandas
- NumPy

### Machine Learning and Analysis

- Scikit-learn
- TF-IDF
- K-Means Clustering

### Visualization

- Matplotlib
- Seaborn
- Microsoft Power BI

### Development Environment

- Jupyter Notebook

---

## Final Deliverables

### Milestone 1

- Initial dataset exploration
- Data understanding
- Exploratory analysis
- Initial visualizations

### Milestone 2

- Cleaned dataset
- Missing-value handling
- Feature preparation
- Encoded features
- Cluster creation

### Milestone 3

- Similarity analysis
- Similarity scores
- Cluster analysis
- Resolution performance analysis
- Regional analysis
- Performance analysis

### Milestone 4

- Interactive Power BI dashboard
- Executive Overview
- Resolution Time Analysis
- Ticket Category Analysis
- Geographic Insights
- Cluster and Similarity Analysis
- Regional Performance
- Insights and Recommendations

---

## Final Project Flow

```text
IT Support Ticket Dataset
          ↓
Milestone 1
Data Exploration & Initial Analysis
          ↓
Milestone 2
Data Cleaning & Feature Preparation
          ↓
Cluster Creation
          ↓
Milestone 3
Similarity + Cluster + Performance + Regional Analysis
          ↓
Milestone 4
Power BI Dashboard Development
          ↓
Insights & Recommendations
          ↓
Final Supportlytics Dashboard
