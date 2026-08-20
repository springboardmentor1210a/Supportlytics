"""
SUPPORTLYTICS — IT Support Performance Dashboard
Milestone 4 / Module 7 deliverable

Organized around the four required performance KPIs:
  1. Average Resolution Time
  2. Most Frequent Categories
  3. Cluster Similarity Index
  4. Top Performing Regions

Run with:  streamlit run app.py

Accepts either:
  - the RAW dataset (customer_support_tickets_200k.csv), in which case this
    script re-creates the same feature engineering used in the analysis
    notebook (Resolution_Duration, Priority_Score, Performance_Bucket,
    KMeans Cluster, Similarity_Score, SLA_Compliant), OR
  - the PROCESSED dataset already saved from the notebook
    (processed_customer_support_tickets.csv), in which case it uses those
    columns directly and skips re-computation.
"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Supportlytics Dashboard", page_icon="🎧", layout="wide")

SLA_LIMIT_HOURS = 72
DEFAULT_PATH = "processed_customer_support_tickets.csv"
PLOTLY_TEMPLATE = "plotly_white"
COLOR_SEQUENCE = ["#0E35A8", "#0EA5E9", "#7C3AED", "#F59E0B", "#10B981", "#EF4444", "#EC4899", "#14B8A6"]
px.defaults.template = PLOTLY_TEMPLATE
px.defaults.color_discrete_sequence = COLOR_SEQUENCE

# ----------------------------------------------------------------------
# Global styling
# ----------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; height: 0; }

.block-container { padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1300px; }

/* Hero banner */
.hero {
    background: linear-gradient(120deg, #1E3A8A 0%, #2563EB 55%, #0EA5E9 100%);
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 6px;
    box-shadow: 0 8px 24px rgba(37, 99, 235, 0.18);
}
.hero h1 { color: #FFFFFF; font-size: 1.9rem; font-weight: 800; margin: 0; letter-spacing: -0.02em; }
.hero p { color: #DBEAFE; font-size: 0.95rem; margin: 6px 0 0 0; font-weight: 400; }

/* KPI cards */
.kpi-card {
    background: #FFFFFF;
    border: 1px solid #E5E9F2;
    border-left: 4px solid #2563EB;
    border-radius: 12px;
    padding: 16px 18px;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
    height: 100%;
}
.kpi-card .kpi-label { font-size: 0.78rem; font-weight: 600; color: #64748B; text-transform: uppercase; letter-spacing: 0.04em; }
.kpi-card .kpi-value { font-size: 1.6rem; font-weight: 800; color: #0F172A; margin-top: 4px; }
.kpi-card .kpi-icon { font-size: 1.3rem; margin-bottom: 6px; display: block; }

/* Section subheaders */
h3 { font-weight: 700 !important; color: #0F172A !important; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] { gap: 4px; border-bottom: 1px solid #E5E9F2; }
.stTabs [data-baseweb="tab"] {
    height: 44px; background-color: transparent; border-radius: 8px 8px 0 0;
    font-weight: 600; color: #64748B; padding: 0 18px;
}
.stTabs [aria-selected="true"] { background-color: #EFF6FF; color: #2563EB !important; }

/* Sidebar */
section[data-testid="stSidebar"] { background-color: #F8FAFC; border-right: 1px solid #E5E9F2; }

[data-testid="stMetricValue"] { font-weight: 700; }
</style>
""", unsafe_allow_html=True)


def kpi_card(col, icon, label, value):
    col.markdown(f"""
    <div class="kpi-card">
        <span class="kpi-icon">{icon}</span>
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)


# ----------------------------------------------------------------------
# Data loading + feature engineering (mirrors the analysis notebook)
# ----------------------------------------------------------------------
@st.cache_data
def load_and_prepare(file) -> pd.DataFrame:
    df = pd.read_csv(file)

    if "Resolution_Duration" not in df.columns:
        df["ticket_created_date"] = pd.to_datetime(df["ticket_created_date"], errors="coerce")
        df["ticket_resolved_date"] = pd.to_datetime(df["ticket_resolved_date"], errors="coerce")
        df["Resolution_Duration"] = (
            (df["ticket_resolved_date"] - df["ticket_created_date"]).dt.total_seconds() / 3600
        ).round(2)

    if "Priority_Score" not in df.columns:
        priority_map = {"Low": 1, "Medium": 2, "High": 3, "Urgent": 4}
        df["Priority_Score"] = df["priority"].map(priority_map)

    if "Performance_Bucket" not in df.columns:
        def bucket(hours):
            if pd.isna(hours):
                return "Unknown"
            if hours <= 24:
                return "Fast (<24h)"
            elif hours <= 72:
                return "Normal (24-72h)"
            return "Slow (>72h)"
        df["Performance_Bucket"] = df["Resolution_Duration"].apply(bucket)

    if "Cluster" not in df.columns or "Similarity_Score" not in df.columns:
        cluster_features = ["Resolution_Duration", "issue_complexity_score",
                             "customer_satisfaction_score", "Priority_Score"]
        valid = df[cluster_features].dropna()
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(valid)
        kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(X_scaled)

        df.loc[valid.index, "Cluster"] = clusters
        distances = np.linalg.norm(X_scaled - kmeans.cluster_centers_[clusters], axis=1)
        df.loc[valid.index, "Similarity_Score"] = 1 / (1 + distances)

    df["SLA_Compliant"] = df["Resolution_Duration"] <= SLA_LIMIT_HOURS
    return df


# ----------------------------------------------------------------------
# Sidebar — data source + filters
# ----------------------------------------------------------------------
st.sidebar.markdown("## 🎧 Supportlytics")
st.sidebar.caption("IT Support Performance Analytics")
st.sidebar.divider()
uploaded = st.sidebar.file_uploader("📁 Upload dataset (CSV)", type="csv")

if uploaded is not None:
    df = load_and_prepare(uploaded)
else:
    try:
        df = load_and_prepare(DEFAULT_PATH)
        st.sidebar.caption(f"Loaded default: {DEFAULT_PATH}")
    except FileNotFoundError:
        st.warning("Upload your dataset CSV in the sidebar to begin.")
        st.stop()

st.sidebar.divider()
st.sidebar.markdown("### 🔍 Filters")
regions = st.sidebar.multiselect("Region", sorted(df["region"].dropna().unique()))
priorities = st.sidebar.multiselect("Priority", ["Low", "Medium", "High", "Urgent"])
categories = st.sidebar.multiselect("Category", sorted(df["category"].dropna().unique()))

filtered = df.copy()
if regions:
    filtered = filtered[filtered["region"].isin(regions)]
if priorities:
    filtered = filtered[filtered["priority"].isin(priorities)]
if categories:
    filtered = filtered[filtered["category"].isin(categories)]

st.markdown(f"""
<div class="hero">
    <h1>IT Support Team Performance Dashboard</h1>
    <p>Showing {len(filtered):,} of {len(df):,} tickets · Supportlytics analytics suite</p>
</div>
""", unsafe_allow_html=True)

critical_backlog = filtered[
    filtered["status"].isin(["Open", "Pending", "In Progress"])
    & filtered["priority"].isin(["High", "Urgent"])
]

cluster_metrics = filtered.groupby("Cluster").agg(
    Cluster_Size=("ticket_id", "count"),
    SLA_Compliance_Rate=("SLA_Compliant", lambda x: x.mean() * 100),
    Avg_CSAT=("customer_satisfaction_score", "mean"),
    Avg_Similarity=("Similarity_Score", "mean"),
).reset_index()
cluster_metrics["Performance_Score"] = (
    cluster_metrics["SLA_Compliance_Rate"] + (cluster_metrics["Avg_CSAT"] / 5 * 100)
) / 2

region_perf = filtered.groupby("region")["Resolution_Duration"].mean().sort_values()
region_sla = (filtered.groupby("region")["SLA_Compliant"].mean() * 100).sort_values(ascending=False)

st.write("")

# ----------------------------------------------------------------------
# Top-line KPI strip — one headline number per required KPI
# ----------------------------------------------------------------------
top_category = filtered["category"].value_counts().idxmax()

k1, k2, k3, k4 = st.columns(4)
kpi_card(k1, "⏱️", "Avg Resolution Time", f"{filtered['Resolution_Duration'].mean():.1f} hrs")
kpi_card(k2, "📋", "Most Frequent Category", top_category)
kpi_card(k3, "🧩", "Avg Cluster Similarity Index", f"{filtered['Similarity_Score'].mean():.3f}")
kpi_card(k4, "🌍", "Top Performing Region", region_sla.index[0])

st.write("")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "⏱️  Average Resolution Time",
        "📋  Most Frequent Categories",
        "🧩  Cluster Similarity Index",
        "🌍  Top Performing Regions",
    ]
)

# ----------------------------------------------------------------------
# KPI 1 — Average Resolution Time
# ----------------------------------------------------------------------
with tab1:
    st.subheader("Average Resolution Time")
    c1, c2, c3 = st.columns(3)
    c1.metric("Overall Avg Resolution Time (hrs)", f"{filtered['Resolution_Duration'].mean():.1f}")
    c2.metric("SLA Compliance Rate", f"{filtered['SLA_Compliant'].mean() * 100:.1f}%")
    c3.metric("Slowest Category (hrs)",
              f"{filtered.groupby('category')['Resolution_Duration'].mean().max():.1f}")

    c1, c2 = st.columns(2)
    with c1:
        cat_time = filtered.groupby("category")["Resolution_Duration"].mean().sort_values(ascending=False)
        fig = px.bar(cat_time, orientation="h", title="Avg Resolution Time by Category (hrs)",
                     labels={"value": "Hours", "index": "Category"})
        st.plotly_chart(fig, width="stretch")
    with c2:
        fig = px.box(filtered, x="priority", y="Resolution_Duration",
                     category_orders={"priority": ["Low", "Medium", "High", "Urgent"]},
                     title="Resolution Time Distribution by Priority")
        st.plotly_chart(fig, width="stretch")

    pivot = filtered.pivot_table(index="region", columns="category",
                                  values="Resolution_Duration", aggfunc="mean")
    fig = px.imshow(pivot, aspect="auto", color_continuous_scale="YlOrRd",
                     title="Avg Resolution Duration: Region x Category (hrs)")
    st.plotly_chart(fig, width="stretch")

    perf_bucket = filtered["Performance_Bucket"].value_counts()
    fig = px.pie(values=perf_bucket.values, names=perf_bucket.index,
                 title="Ticket Share by Resolution Speed Bucket")
    st.plotly_chart(fig, width="stretch")

# ----------------------------------------------------------------------
# KPI 2 — Most Frequent Categories
# ----------------------------------------------------------------------
with tab2:
    st.subheader("Most Frequent Categories")
    cat_counts_full = filtered["category"].value_counts()
    c1, c2, c3 = st.columns(3)
    c1.metric("#1 Category", cat_counts_full.index[0], f"{cat_counts_full.iloc[0]:,} tickets")
    c2.metric("#2 Category", cat_counts_full.index[1] if len(cat_counts_full) > 1 else "-")
    c3.metric("Unique Categories", f"{filtered['category'].nunique()}")

    c1, c2 = st.columns(2)
    with c1:
        top10 = cat_counts_full.head(10)
        fig = px.bar(top10, orientation="h", title="Top 10 Ticket Categories by Volume",
                     labels={"value": "Tickets", "index": "Category"})
        st.plotly_chart(fig, width="stretch")
    with c2:
        pri_counts = filtered["priority"].value_counts().reindex(["Low", "Medium", "High", "Urgent"])
        fig = px.bar(pri_counts, title="Ticket Volume by Priority",
                     labels={"value": "Tickets", "index": "Priority"})
        st.plotly_chart(fig, width="stretch")

    st.subheader("Unresolved High-Priority Backlog by Category")
    backlog_by_cat = critical_backlog["category"].value_counts().reset_index()
    backlog_by_cat.columns = ["Category", "Unresolved_Count"]
    fig = px.bar(backlog_by_cat, x="Unresolved_Count", y="Category", orientation="h")
    st.plotly_chart(fig, width="stretch")

    region_cat_matrix = pd.crosstab(filtered["region"], filtered["category"])
    fig = px.imshow(region_cat_matrix, aspect="auto", color_continuous_scale="YlOrBr",
                     title="Ticket Concentration: Region x Category")
    st.plotly_chart(fig, width="stretch")

# ----------------------------------------------------------------------
# KPI 3 — Cluster Similarity Index
# ----------------------------------------------------------------------
with tab3:
    st.subheader("Cluster Similarity Index")
    c1, c2, c3 = st.columns(3)
    c1.metric("Avg Similarity Index", f"{filtered['Similarity_Score'].mean():.3f}")
    best_cluster = cluster_metrics.loc[cluster_metrics["Avg_Similarity"].idxmax(), "Cluster"]
    c2.metric("Most Cohesive Cluster", f"Cluster {int(best_cluster)}")
    c3.metric("Number of Clusters", f"{filtered['Cluster'].nunique()}")

    c1, c2 = st.columns(2)
    with c1:
        cluster_counts = filtered["Cluster"].value_counts().sort_index()
        fig = px.bar(cluster_counts, title="Ticket Volume by Cluster",
                     labels={"value": "Tickets", "index": "Cluster"})
        st.plotly_chart(fig, width="stretch")
    with c2:
        sim_avg = filtered.groupby("Cluster")["Similarity_Score"].mean().sort_index()
        fig = px.bar(sim_avg, title="Avg Similarity Score by Cluster",
                     labels={"value": "Similarity Score", "index": "Cluster"})
        st.plotly_chart(fig, width="stretch")

    st.subheader("Cluster Performance Profile")
    st.dataframe(cluster_metrics.round(2), width="stretch")

    fig, ax1 = plt.subplots(figsize=(10, 5))
    ax1.bar(cluster_metrics["Cluster"].astype(str), cluster_metrics["Cluster_Size"],
            color="#4c72b0", alpha=0.7)
    ax1.set_xlabel("Cluster")
    ax1.set_ylabel("Cluster Size (Ticket Volume)", color="#4c72b0")
    ax2 = ax1.twinx()
    ax2.plot(cluster_metrics["Cluster"].astype(str), cluster_metrics["Performance_Score"],
             color="#d95f02", marker="o", linewidth=3, markersize=8)
    ax2.set_ylabel("Performance Score (0-100)", color="#d95f02")
    ax2.set_ylim(0, 100)
    plt.title("Cluster Size vs. Operational Performance Score")
    st.pyplot(fig)

# ----------------------------------------------------------------------
# KPI 4 — Top Performing Regions
# ----------------------------------------------------------------------
with tab4:
    st.subheader("Top Performing Regions")
    c1, c2, c3 = st.columns(3)
    c1.metric("Best Region (SLA)", region_sla.index[0], f"{region_sla.iloc[0]:.1f}%")
    c2.metric("Fastest Region (hrs)", region_perf.index[0], f"{region_perf.iloc[0]:.1f} hrs")
    c3.metric("Regions Tracked", f"{filtered['region'].nunique()}")

    c1, c2 = st.columns(2)
    with c1:
        fig = px.bar(region_sla, title="SLA Compliance Rate by Region (%)",
                     labels={"value": "% Compliant", "index": "Region"})
        st.plotly_chart(fig, width="stretch")
    with c2:
        fig = px.bar(region_perf, orientation="h", title="Avg Resolution Time by Region (hrs)",
                     labels={"value": "Hours", "index": "Region"})
        st.plotly_chart(fig, width="stretch")

    coordinate_mapping = {
        "North America": (37.09, -95.71), "United States": (37.09, -95.71),
        "Europe": (51.17, 10.45), "United Kingdom": (55.38, -3.44),
        "Asia": (34.05, 100.62), "India": (20.59, 78.96),
        "South America": (-14.24, -51.93), "Australia": (-25.27, 133.78),
        "Africa": (-8.78, -55.49),
    }
    geo_data = filtered.groupby(["region", "category"]).size().reset_index(name="Ticket_Volume")
    geo_data["latitude"] = geo_data["region"].map(lambda r: coordinate_mapping.get(r, (0, 0))[0])
    geo_data["longitude"] = geo_data["region"].map(lambda r: coordinate_mapping.get(r, (0, 0))[1])

    fig = px.scatter_geo(
        geo_data, lat="latitude", lon="longitude", color="category", size="Ticket_Volume",
        hover_name="region", projection="natural earth",
        title="Geographic Distribution of Issue Categories", size_max=40,
    )
    st.plotly_chart(fig, width="stretch")