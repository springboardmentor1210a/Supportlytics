# **Optimizing IT Support Team Performance Using Advanced Analytics (Supportlytics)** 

## **📌 Project Overview**  
The primary objective of this project is to analyze IT support ticket data to identify performance trends, improve ticket resolution efficiency, and optimize IT support operations using data analytics and visualization techniques.
The project aims to:
- **Analyze historical IT support ticket data.**
- **Measure support team performance using key metrics.**
- **Identify recurring technical issues and support ticket patterns.**
- **Discover similar issues using clustering and similarity analysis.**
- **Improve resource allocation and workflow efficiency.**
- **Build an interactive Power BI dashboard for decision-making.**
- **Provide data-driven recommendations to reduce ticket resolution time and improve customer satisfaction.**

---

## **🛠️ Tools Used**  
| **Tool**       | **Purpose**                          |
|----------------|--------------------------------------|
| Python (Pandas) | Data cleaning, text mining, and statistical analysis |
| Google Colab   | Cloud-based Python execution         |
| Power BI        | Interactive dashboard visualization  |
| Excel          | Supplemental data validation         |

---

## **📂 Repository Structure**  
```
📂 customer-support-analysis/
├── 📄 raw_data/                     # Original dataset
│   └── customer_support_tickets.csv  
├── 📄 processed_data/               # Cleaned data for Tableau
│   └── cleaned_support_tickets.csv  
├── 📄 notebooks/                    # Colab notebooks
│   └── support_ticket_analysis.ipynb  
├── 📄 Power BI/                      # Power BI workbook & exports
│   ├── support_dashboard.twbx  
│   └── dashboard_screenshots/  
└── 📄 README.md
                  
```

## **🔍 Key Insights from Analysis**  

### **1. Most Common Issues**  

- **Top 3 Problem Categories**:  
  1. **Technical Issues (38%)**  
     - Frequent keywords: "not turning on", "network problem", "setup failed"  
     - Worst-affected products: Microsoft Office, HP Pavilion  
  2. **Billing Inquiries (22%)**  
  3. **Refund Requests (18%)**  

### **2. Response Time Metrics**  
| Metric                  | Average Time |  
|-------------------------|--------------|  
| First Response Time     | 4.2 hours    |  
| Resolution Time         | 8.7 hours    |  
- **Critical tickets** take 12+ hours (needs prioritization).  

### **3. Customer Satisfaction (CSAT)**  
- **Average Rating: 3.1/5**  
- **Lowest-rated areas**:  
  - Slow resolution for hardware issues  
  - Unclear refund processes  

---

## **📊 Power BI Dashboard Features**  
![customer support dashborad main](https://github.com/springboardmentor1210a/Supportlytics/blob/JagannathReddy/Supportlytics/Dashboard1.png?raw=true)
![](https://github.com/springboardmentor1210a/Supportlytics/blob/JagannathReddy/Supportlytics/Dashboard2.png?raw=true)
![](https://github.com/springboardmentor1210a/Supportlytics/blob/JagannathReddy/Supportlytics/Dashboard3.png?raw=true)
![](https://github.com/springboardmentor1210a/Supportlytics/blob/JagannathReddy/Supportlytics/Dashboard4.png?raw=true)
![](https://github.com/springboardmentor1210a/Supportlytics/blob/JagannathReddy/Supportlytics/Dashboard5.png?raw=true)
![](https://github.com/springboardmentor1210a/Supportlytics/blob/JagannathReddy/Supportlytics/dashboard6.png?raw=true)

---

**Key Visualizations**:  
1. **Ticket Volume Trends** (by product/month)  
2. **Response Time Distribution** (priority-wise)  
3. **CSAT Score Distribution**
4. **Resolution Time Distribution**
5. **Tickets Over Time**


---
