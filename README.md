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

---

## Milestone 2: Week 3-4

### Module 3: Exploratory Data Analysis & Operational Profiling
The objective of this module was to perform deep-dive exploratory data analysis (EDA) to map workload distributions, identify high-volume pain points, and uncover early performance patterns across support channels.

**Key Achievements & Steps:**
* **Team Queue Mapping**: Engineered a business-informed organizational routing layer (`Queue`) to map the 10 incoming raw categories into 7 functional support teams.
* **Volumetric Profiling**: Visualized macro ticket volume trends segmented by **Ticket Type**, **Raw Category**, and **Urgency Priority Tiers** using optimized Seaborn color ramps (`Blues_d`, `Greens_d`, `Oranges_d`).
* **Operational Queue Auditing**: Evaluated resource distribution across functional silos (`Queue`) to pinpoint the heaviest operational backlogs and team delivery pressures.
* **Asset Export Integration**: Rendered, formatted, and committed early operational charts directly to disk as high-resolution PNG assets (`viz1`, `viz2`, `viz4`, `viz5`).

---

### Module 4: Clustering & Text Similarity Analysis
This module bypassed statistical cluster discovery noise by implementing a rigid, business-informed 6-cluster grouping structure combined with Natural Language Processing (NLP) similarity calculations.

**Key Achievements & Steps:**
* **Text Feature Extraction**: Configured a `TfidfVectorizer` pipeline restricted to the top 300 terms, filtering out English stop words and low-frequency text to normalize 200,000 text descriptions.
* **Unsupervised Validation Audit**: Executed statistical validations (Elbow Method and Silhouette Scoring) from k = 2 to k = 12 on both text matrices and behavioral metrics, proving statistical text clustering was ineffective due to templated ticket formatting.
* **Business-Informed Consolidation**: Injected custom business logic to merge sparse, overlapping categories into 6 highly functional target domains (e.g., merging `Login Issue` + `Security Concern` into **Security & Access**).
* **Centroid Proximity Calculation**: Programmatically mapped records to their respective custom cluster IDs and calculated cosine similarity vectors against the group’s textual mean (`Similarity_Score`).
* **Statistical Spread Visualization**: Generated advanced analytical diagnostics—including cluster frequency profiles (`viz3`), cluster size vs. average resolution scatters (`viz6`), similarity score distribution boxplots (`viz7`), and cross-tab heatmaps (`viz8`).
* **Enriched Serialization**: Exported the finalized 200,000-row production dataset, fully appended with the custom operational tracking vectors.

**Module Deliverables:**
1. **Enriched Clustering Dataset**: Master CSV artifact appended with engineered tracking fields (`customer_support_tickets_200k_with_clusters.csv`).
2. **Analytical Visualization Suite**: A comprehensive deck of 8 sequential, high-resolution chart assets matching pipeline steps (`viz1_*.png` through `viz8_*.png`).
3. **Clustering & Similarity Pipeline**: Standardized, end-to-end Python source file integrating textual engineering and matrix mathematics.
