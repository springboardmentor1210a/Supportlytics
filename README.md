# Supportlytics: Optimizing IT Support Team Performance Using Analytics

## Problem Statement
The objective of this project is to analyze IT support ticket data to identify key performance trends, optimize resolution times, and enhance service efficiency through data analysis and visualization. 

The core goal is to uncover hidden patterns in customer requests, technical system issues, and support performance metrics. Ultimately, these insights will be used to recommend concrete, data-backed improvements in operational workflows and team resource allocation.

---

## Milestone 1: Week 1-2

### Module 1: Project Initialization and Dataset Setup
The objective of this module was to establish the analytical framework and conduct an initial structural audit of the incoming IT support ticketing dataset.

**Key Achievements & Steps:**
* **Strategic Definition**: Outlined key project objectives, operational KPIs, and the end-to-end data analysis workflow.
* **Data Ingestion**: Programmatically loaded the core CSV support ticket dataset into Python utilizing the `pandas` library.
* **Schema Audit**: Explored the dataset schema, validated feature data types, and isolated structural missing values.
* **Baseline Profiling**: Calculated the initial volume and percentage distributions of tickets segmented by **Type**, **Priority**, and **Category**.

---

### Module 2: Data Cleaning and Feature Engineering
This module focused on correcting data quality anomalies and synthesizing downstream operational metrics to measure support efficiency.

**Key Achievements & Steps:**
* **Text Fields Scrubbing**: Identified and handled missing, corrupted, or incorrect string entries across descriptive text fields.
* **Feature Synthesis (`Resolution_Duration`)**: Engineered a time-delta feature calculating the chronological gap between ticket creation and ticket resolution.
* **Feature Synthesis (`Priority_Score`)**: Created a quantitative priority matrix calculation to score and rank ticket urgency dynamically.
* **Data Serialization**: Saved and exported the resulting structured datasets to ensure reproducible analysis states.

**Module Deliverables:**
1. **Cleaned Dataset**: Ready-to-use CSV pipeline artifact.
2. **Feature Engineering Summary**: Documented logic for new feature creations (`feature_engineering_summary.txt`).
3. **Data Dictionary**: Field descriptions, semantic mappings, and data type specifications (`data_dictionary.csv`).
