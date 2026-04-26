import os
import pandas as pd
import streamlit as st

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Financial Risk Analysis and Bankruptcy Early Warning Tool",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Simple CSS styling
# ---------------------------
st.markdown("""
<style>
    .main {
        padding-top: 1rem;
    }
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }
    h1, h2, h3 {
        color: #1f3b73;
    }
    .stMetric {
        background-color: #f7f9fc;
        border: 1px solid #e6ecf5;
        padding: 12px;
        border-radius: 12px;
    }
    div[data-testid="stSidebar"] {
        background-color: #f8fafc;
    }
    .caption-box {
        background-color: #f4f7fb;
        padding: 0.8rem 1rem;
        border-left: 5px solid #4f81bd;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Paths
# ---------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "outputs", "cleaned_data.csv")
TABLE_DIR = os.path.join(BASE_DIR, "outputs", "tables")
FIG_DIR = os.path.join(BASE_DIR, "outputs", "figures")

# ---------------------------
# Helpers
# ---------------------------
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

@st.cache_data
def load_table(path):
    return pd.read_csv(path)

def table_path(filename):
    return os.path.join(TABLE_DIR, filename)

def fig_path(filename):
    return os.path.join(FIG_DIR, filename)

def show_image_if_exists(filename, caption=None, use_column_width=True):
    path = fig_path(filename)
    if os.path.exists(path):
        st.image(path, caption=caption, use_container_width=use_column_width)
    else:
        st.info(f"Figure not found: {filename}")

def show_table_if_exists(filename, title=None):
    path = table_path(filename)
    if os.path.exists(path):
        if title:
            st.subheader(title)
        df_table = load_table(path)
        st.dataframe(df_table, use_container_width=True)
    else:
        st.info(f"Table not found: {filename}")

def risk_level_from_score(score):
    if score <= 1:
        return "Low", "success"
    elif score <= 3:
        return "Medium", "warning"
    else:
        return "High", "error"

# ---------------------------
# Load main dataset
# ---------------------------
if not os.path.exists(DATA_PATH):
    st.error("Cannot find outputs/cleaned_data.csv. Please run your notebook first.")
    st.stop()

df = load_data(DATA_PATH)

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Select a module",
    [
        "Home",
        "Dataset Overview",
        "EDA Visualisations",
        "Statistical Results",
        "Risk Checker",
        "Conclusion"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Project Snapshot")
st.sidebar.write(f"**Dataset shape:** {df.shape[0]} rows × {df.shape[1]} columns")

if "Bankrupt" in df.columns:
    counts = df["Bankrupt"].value_counts().to_dict()
    st.sidebar.write(f"**Target counts:** {counts}")

st.sidebar.markdown("---")
st.sidebar.info(
    "This Streamlit app summarises the EDA, statistical findings, and a simple "
    "rule-based early warning prototype for enterprise bankruptcy analysis."
)

# ---------------------------
# Home
# ---------------------------
if page == "Home":
    st.title("Financial Risk Analysis and Bankruptcy Early Warning Tool")

    st.markdown(
        """
        <div class="caption-box">
        This application presents a structured exploration of enterprise financial data,
        with a focus on bankruptcy-related patterns, statistical insights, and a simple
        interactive early warning demonstration.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Rows", f"{df.shape[0]:,}")
    with col2:
        st.metric("Columns", f"{df.shape[1]}")
    with col3:
        if "Bankrupt" in df.columns:
            bankrupt_ratio = df["Bankrupt"].mean() * 100
            st.metric("Bankrupt Ratio", f"{bankrupt_ratio:.2f}%")

    st.markdown("---")

    c1, c2 = st.columns([1.2, 1])
    with c1:
        st.subheader("Project Objectives")
        st.markdown("""
- Understand the structure and quality of enterprise financial data  
- Compare bankrupt and non-bankrupt firms across key financial indicators  
- Identify financial patterns associated with bankruptcy risk  
- Demonstrate a simple early warning prototype in an interactive application  
        """)

        st.subheader("Main App Modules")
        st.markdown("""
- **Dataset Overview** — inspect the cleaned dataset and target structure  
- **EDA Visualisations** — review charts generated from the notebook workflow  
- **Statistical Results** — check correlations, significance tests, and summaries  
- **Risk Checker** — try a simple rule-based bankruptcy warning demo  
- **Conclusion** — review overall findings and possible future improvements  
        """)

    with c2:
        st.subheader("Target Users")
        st.write(
            "This application is designed for finance students, beginner analysts, and non-technical users who want to explore bankruptcy-related financial patterns through a simple and interpretable interface."
        )

        st.subheader("Why This App Matters")
        st.write(
            "Instead of presenting only static notebook results, this dashboard makes the analysis easier to navigate, explain, and assess."
        )

    st.markdown("---")
    st.subheader("Quick Start")
    st.success(
        "Use the sidebar on the left to navigate through the dataset overview, EDA results, "
        "statistical findings, and the interactive risk checker."
    )

# ---------------------------
# Dataset Overview
# ---------------------------
elif page == "Dataset Overview":
    st.title("Dataset Overview")

    st.markdown("""
    This section provides a quick inspection of the cleaned dataset, including preview rows,
    feature data types, missing values, and the target distribution.
    """)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Total Observations", f"{df.shape[0]:,}")
    with c2:
        st.metric("Total Features", f"{df.shape[1]}")
    with c3:
        missing_cells = int(df.isnull().sum().sum())
        st.metric("Missing Cells", f"{missing_cells:,}")

    st.markdown("---")

    st.subheader("1. Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.markdown("---")

    st.subheader("2. Basic Information")
    info_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str).values,
        "Missing Count": df.isnull().sum().values
    })
    st.dataframe(info_df, use_container_width=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("3. Missing Values Summary")
        missing_df = df.isnull().sum().reset_index()
        missing_df.columns = ["Feature", "Missing_Count"]
        missing_df["Missing_Ratio"] = missing_df["Missing_Count"] / len(df)
        st.dataframe(
            missing_df.sort_values("Missing_Count", ascending=False),
            use_container_width=True
        )

    with col2:
        st.subheader("4. Target Distribution Table")
        if "Bankrupt" in df.columns:
            target_dist = df["Bankrupt"].value_counts().reset_index()
            target_dist.columns = ["Bankrupt", "Count"]
            target_dist["Proportion"] = target_dist["Count"] / len(df)
            st.dataframe(target_dist, use_container_width=True)
        else:
            st.info("Target column 'Bankrupt' not found.")

    st.markdown("---")
    st.subheader("5. Saved Target Distribution Figure")
    show_image_if_exists("target_distribution.png", "Distribution of Bankruptcy Status")

# ---------------------------
# EDA Visualisations
# ---------------------------
elif page == "EDA Visualisations":
    st.title("EDA Visualisations")

    st.markdown("""
    This page presents the main visual outputs generated during exploratory data analysis (EDA),
    including target distribution, feature comparisons, correlation analysis, outlier inspection,
    and additional boxplots/distribution charts for selected variables.
    """)

    st.markdown("---")

    st.subheader("1. Target Distribution")
    st.caption("This figure shows the class balance between bankrupt and non-bankrupt firms.")
    show_image_if_exists("target_distribution.png", "Distribution of Bankruptcy Labels")

    st.markdown("---")

    st.subheader("2. Key Feature Mean Comparison by Target")
    st.caption("This chart compares the average values of selected financial indicators across target groups.")
    show_image_if_exists("key_feature_mean_comparison.png", "Mean Comparison of Key Financial Features")

    st.markdown("---")

    st.subheader("3. Correlation Heatmap")
    st.caption("This heatmap helps identify feature relationships and possible multicollinearity.")
    show_image_if_exists("correlation_heatmap.png", "Correlation Heatmap of Selected Features")

    st.markdown("---")

    st.subheader("4. Financial Category Comparison")
    st.caption("This figure summarises average values across broader financial indicator categories.")
    show_image_if_exists("financial_category_comparison.png", "Average Feature Values by Financial Category")

    st.markdown("---")

    st.subheader("5. Outliers and Statistical Significance")
    st.caption("These visualisations highlight variables with strong outlier behaviour and statistical importance.")
    col1, col2 = st.columns(2)
    with col1:
        show_image_if_exists("top15_outlier_ratio.png", "Top 15 Features by Outlier Ratio")
    with col2:
        show_image_if_exists("statistical_significance_features.png", "Top Significant Features by -log10(p-value)")

    st.markdown("---")

    st.subheader("6. Optional Boxplots and Distributions")
    st.caption("All optional visualisations are displayed directly below to avoid being overlooked during assessment.")

    available_files = sorted(os.listdir(FIG_DIR)) if os.path.exists(FIG_DIR) else []
    boxplot_files = [f for f in available_files if f.startswith("boxplot_")]
    dist_files = [f for f in available_files if f.startswith("distribution_")]
    flag_files = [f for f in available_files if f.startswith("flag_")]

    st.markdown("### 6.1 Boxplots")
    if boxplot_files:
        default_boxplots = boxplot_files[:3] if len(boxplot_files) >= 3 else boxplot_files
        selected_boxplots = st.multiselect(
            "Select boxplots to display",
            boxplot_files,
            default=default_boxplots,
            key="boxplots_select"
        )
        for f in selected_boxplots:
            show_image_if_exists(f, f)
    else:
        st.info("No boxplot figures found.")

    st.markdown("### 6.2 Distribution Plots")
    if dist_files:
        default_dists = dist_files[:3] if len(dist_files) >= 3 else dist_files
        selected_dists = st.multiselect(
            "Select distribution plots to display",
            dist_files,
            default=default_dists,
            key="dists_select"
        )
        for f in selected_dists:
            show_image_if_exists(f, f)
    else:
        st.info("No distribution figures found.")

    st.markdown("### 6.3 Flag Plots")
    if flag_files:
        default_flags = flag_files[:3] if len(flag_files) >= 3 else flag_files
        selected_flags = st.multiselect(
            "Select flag plots to display",
            flag_files,
            default=default_flags,
            key="flags_select"
        )
        for f in selected_flags:
            show_image_if_exists(f, f)
    else:
        st.info("No flag figures found.")

# ---------------------------
# Statistical Results
# ---------------------------
elif page == "Statistical Results":
    st.title("Statistical Results")

    st.markdown("""
    This section summarises the main statistical outputs produced during analysis,
    including target correlations, significance testing, category-level comparisons,
    and outlier summaries.
    """)

    st.markdown("---")

    show_table_if_exists("target_correlation.csv", "1. Correlation with Bankruptcy Target")
    show_table_if_exists("top_target_correlations.csv", "2. Top Positive and Negative Correlations")
    show_table_if_exists("mannwhitney_test_results.csv", "3. Mann–Whitney U Test Results")
    show_table_if_exists("financial_category_comparison.csv", "4. Financial Category Comparison")
    show_table_if_exists("outlier_summary.csv", "5. Outlier Summary")

    st.markdown("---")
    st.subheader("Quick Statistical Insight")

    mw_path = table_path("mannwhitney_test_results.csv")
    if os.path.exists(mw_path):
        mw_df = load_table(mw_path)
        if "Significant_at_0_05" in mw_df.columns:
            sig_count = int(mw_df["Significant_at_0_05"].sum())
            st.success(f"Number of statistically significant features at the 5% level: {sig_count}")
        else:
            st.info("Significance column not found in Mann–Whitney result table.")
    else:
        st.info("Mann–Whitney results table not found.")

# ---------------------------
# Risk Checker
# ---------------------------
elif page == "Risk Checker":
    st.title("Bankruptcy Risk Checker")

    st.markdown("""
    This module implements an interpretable multi-indicator early warning framework for
    preliminary bankruptcy risk screening. It evaluates a firm's financial condition across
    four key dimensions: **profitability**, **liquidity**, **leverage**, and
    **cash flow & debt servicing capacity**.
    """)

    st.info(
        "This prototype demonstrates how financial indicators can be translated into a structured "
        "and interactive risk assessment tool within an enterprise financial risk analysis system."
    )

    st.markdown("---")
    st.subheader("1. Select an Input Mode")

    preset = st.radio(
        "Choose a company profile or enter values manually:",
        ["Manual Input", "Healthy Profile", "Watchlist Profile", "Distressed Profile"],
        horizontal=True
    )

    # Preset values
    if preset == "Healthy Profile":
        default_values = {
            "roa_a": 0.10,
            "current_ratio": 1.80,
            "debt_ratio": 0.35,
            "cashflow_to_liability": 0.12,
            "net_income_to_assets": 0.08,
            "quick_ratio": 1.20,
            "liability_to_equity": 0.70,
            "interest_coverage": 3.00,
        }
    elif preset == "Watchlist Profile":
        default_values = {
            "roa_a": 0.04,
            "current_ratio": 1.10,
            "debt_ratio": 0.65,
            "cashflow_to_liability": 0.04,
            "net_income_to_assets": 0.025,
            "quick_ratio": 0.95,
            "liability_to_equity": 1.60,
            "interest_coverage": 1.30,
        }
    elif preset == "Distressed Profile":
        default_values = {
            "roa_a": 0.01,
            "current_ratio": 0.75,
            "debt_ratio": 0.82,
            "cashflow_to_liability": 0.02,
            "net_income_to_assets": 0.005,
            "quick_ratio": 0.60,
            "liability_to_equity": 2.40,
            "interest_coverage": 0.80,
        }
    else:
        default_values = {
            "roa_a": 0.10,
            "current_ratio": 1.50,
            "debt_ratio": 0.40,
            "cashflow_to_liability": 0.12,
            "net_income_to_assets": 0.08,
            "quick_ratio": 1.10,
            "liability_to_equity": 0.80,
            "interest_coverage": 2.00,
        }

    st.markdown("---")
    st.subheader("2. Input Financial Indicators")

    c1, c2 = st.columns(2)

    with c1:
        roa_a = st.number_input(
            "ROA_A",
            value=default_values["roa_a"],
            step=0.01,
            format="%.4f",
            help="Return on Assets. Lower profitability may indicate weaker operating performance."
        )
        current_ratio = st.number_input(
            "Current_Ratio",
            value=default_values["current_ratio"],
            step=0.10,
            format="%.4f",
            help="Measures short-term liquidity. Lower values suggest weaker ability to cover current liabilities."
        )
        debt_ratio = st.number_input(
            "Debt_Ratio",
            value=default_values["debt_ratio"],
            step=0.01,
            format="%.4f",
            help="A higher debt ratio indicates greater reliance on liabilities."
        )
        cashflow_to_liability = st.number_input(
            "CashFlow_to_Liability",
            value=default_values["cashflow_to_liability"],
            step=0.01,
            format="%.4f",
            help="Shows how well operating cash flow supports liabilities."
        )

    with c2:
        net_income_to_assets = st.number_input(
            "Net_Income_to_Total_Assets",
            value=default_values["net_income_to_assets"],
            step=0.01,
            format="%.4f",
            help="Profit generated from the asset base. Lower values may indicate financial weakness."
        )
        quick_ratio = st.number_input(
            "Quick_Ratio",
            value=default_values["quick_ratio"],
            step=0.10,
            format="%.4f",
            help="A stricter liquidity measure than the current ratio."
        )
        liability_to_equity = st.number_input(
            "Liability_to_Equity",
            value=default_values["liability_to_equity"],
            step=0.05,
            format="%.4f",
            help="Higher values suggest stronger leverage pressure."
        )
        interest_coverage = st.number_input(
            "Interest_Coverage_Ratio",
            value=default_values["interest_coverage"],
            step=0.10,
            format="%.4f",
            help="Measures the firm’s ability to meet interest obligations."
        )

    st.markdown("---")
    st.subheader("3. Risk Evaluation Framework")

    with st.expander("View scoring framework"):
        st.markdown("""
        Each indicator is scored on a **three-level scale**:

        - **0 points** = relatively healthy  
        - **1 point** = warning signal  
        - **2 points** = strong risk signal  

        The final result combines eight indicators into four dimensions:

        - **Profitability**
        - **Liquidity**
        - **Leverage**
        - **Cash Flow & Coverage**
        """)

    def classify_status(score):
        if score == 0:
            return "Healthy"
        elif score == 1:
            return "Warning"
        else:
            return "High Risk"

    def score_roa(x):
        if x < 0.02:
            return 2, "ROA_A is critically low (< 0.02)"
        elif x < 0.05:
            return 1, "ROA_A is below the healthy range (< 0.05)"
        return 0, "ROA_A is within a relatively healthy range"

    def score_ni_to_assets(x):
        if x < 0.01:
            return 2, "Net Income / Total Assets is critically low (< 0.01)"
        elif x < 0.03:
            return 1, "Net Income / Total Assets is weak (< 0.03)"
        return 0, "Net Income / Total Assets is within a relatively healthy range"

    def score_current_ratio(x):
        if x < 1.00:
            return 2, "Current Ratio indicates weak short-term liquidity (< 1.00)"
        elif x < 1.50:
            return 1, "Current Ratio is below the preferred level (< 1.50)"
        return 0, "Current Ratio is within a relatively healthy range"

    def score_quick_ratio(x):
        if x < 0.80:
            return 2, "Quick Ratio is critically low (< 0.80)"
        elif x < 1.00:
            return 1, "Quick Ratio is slightly weak (< 1.00)"
        return 0, "Quick Ratio is within a relatively healthy range"

    def score_debt_ratio(x):
        if x > 0.75:
            return 2, "Debt Ratio is very high (> 0.75)"
        elif x > 0.60:
            return 1, "Debt Ratio is moderately high (> 0.60)"
        return 0, "Debt Ratio is within a relatively acceptable range"

    def score_liability_to_equity(x):
        if x > 2.00:
            return 2, "Liability-to-Equity ratio is critically high (> 2.00)"
        elif x > 1.50:
            return 1, "Liability-to-Equity ratio is elevated (> 1.50)"
        return 0, "Liability-to-Equity ratio is within a relatively acceptable range"

    def score_cashflow_to_liability(x):
        if x < 0.03:
            return 2, "Cash Flow / Liability is critically weak (< 0.03)"
        elif x < 0.05:
            return 1, "Cash Flow / Liability is below the preferred level (< 0.05)"
        return 0, "Cash Flow / Liability is within a relatively healthy range"

    def score_interest_coverage(x):
        if x < 1.00:
            return 2, "Interest Coverage Ratio is critically low (< 1.00)"
        elif x < 1.50:
            return 1, "Interest Coverage Ratio is below the safe range (< 1.50)"
        return 0, "Interest Coverage Ratio is within a relatively healthy range"

    # Score indicators
    roa_score, roa_msg = score_roa(roa_a)
    ni_score, ni_msg = score_ni_to_assets(net_income_to_assets)
    cr_score, cr_msg = score_current_ratio(current_ratio)
    qr_score, qr_msg = score_quick_ratio(quick_ratio)
    dr_score, dr_msg = score_debt_ratio(debt_ratio)
    le_score, le_msg = score_liability_to_equity(liability_to_equity)
    cf_score, cf_msg = score_cashflow_to_liability(cashflow_to_liability)
    ic_score, ic_msg = score_interest_coverage(interest_coverage)

    # Dimension scores
    profitability_score = roa_score + ni_score
    liquidity_score = cr_score + qr_score
    leverage_score = dr_score + le_score
    cashflow_score = cf_score + ic_score

    total_score = profitability_score + liquidity_score + leverage_score + cashflow_score
    max_score = 16

    # Overall risk level
    if total_score <= 2:
        level = "Low"
        msg_type = "success"
    elif total_score <= 5:
        level = "Moderate"
        msg_type = "info"
    elif total_score <= 8:
        level = "Elevated"
        msg_type = "warning"
    else:
        level = "High"
        msg_type = "error"

    risk_ratio = total_score / max_score

    st.markdown("---")
    st.subheader("4. Assessment Result")

    r1, r2, r3 = st.columns(3)
    with r1:
        st.metric("Overall Risk Score", f"{total_score} / {max_score}")
    with r2:
        st.metric("Risk Level", level)
    with r3:
        st.metric("Selected Scenario", preset)

    st.progress(risk_ratio)

    if msg_type == "success":
        st.success("The company shows a relatively healthy financial profile under this early warning screening framework.")
    elif msg_type == "info":
        st.info("The company shows some warning signals, but the overall risk profile remains moderate.")
    elif msg_type == "warning":
        st.warning("The company shows several material warning signals and may require closer monitoring.")
    else:
        st.error("The company shows substantial financial stress signals and may face elevated bankruptcy risk.")

    st.markdown("---")
    st.subheader("5. Dimension-Level Summary")

    d1, d2, d3, d4 = st.columns(4)
    with d1:
        st.metric("Profitability", f"{profitability_score} / 4")
    with d2:
        st.metric("Liquidity", f"{liquidity_score} / 4")
    with d3:
        st.metric("Leverage", f"{leverage_score} / 4")
    with d4:
        st.metric("Cash Flow & Coverage", f"{cashflow_score} / 4")

    st.markdown("---")
    st.subheader("6. Indicator-Level Interpretation")

    indicator_results = pd.DataFrame({
        "Indicator": [
            "ROA_A",
            "Net_Income_to_Total_Assets",
            "Current_Ratio",
            "Quick_Ratio",
            "Debt_Ratio",
            "Liability_to_Equity",
            "CashFlow_to_Liability",
            "Interest_Coverage_Ratio"
        ],
        "Input Value": [
            roa_a,
            net_income_to_assets,
            current_ratio,
            quick_ratio,
            debt_ratio,
            liability_to_equity,
            cashflow_to_liability,
            interest_coverage
        ],
        "Score": [
            roa_score,
            ni_score,
            cr_score,
            qr_score,
            dr_score,
            le_score,
            cf_score,
            ic_score
        ],
        "Status": [
            classify_status(roa_score),
            classify_status(ni_score),
            classify_status(cr_score),
            classify_status(qr_score),
            classify_status(dr_score),
            classify_status(le_score),
            classify_status(cf_score),
            classify_status(ic_score)
        ],
        "Interpretation": [
            roa_msg,
            ni_msg,
            cr_msg,
            qr_msg,
            dr_msg,
            le_msg,
            cf_msg,
            ic_msg
        ]
    })
    st.dataframe(indicator_results, use_container_width=True)

    st.markdown("---")
    st.subheader("7. Key Findings")

    dimension_map = {
        "Profitability": profitability_score,
        "Liquidity": liquidity_score,
        "Leverage": leverage_score,
        "Cash Flow & Coverage": cashflow_score
    }
    sorted_dimensions = sorted(dimension_map.items(), key=lambda x: x[1], reverse=True)

    top_dimension, top_score = sorted_dimensions[0]

    if total_score <= 2:
        st.success(
            "Overall, the assessed indicators suggest a relatively stable financial condition, "
            "with no major risk concentration observed across the four dimensions."
        )
    else:
        if top_score > 0:
            st.write(f"**Primary risk driver:** {top_dimension} ({top_score} / 4)")
        if len(sorted_dimensions) > 1 and sorted_dimensions[1][1] > 0:
            st.write(f"**Secondary concern:** {sorted_dimensions[1][0]} ({sorted_dimensions[1][1]} / 4)")

        high_risk_indicators = indicator_results[indicator_results["Score"] == 2]["Indicator"].tolist()
        warning_indicators = indicator_results[indicator_results["Score"] == 1]["Indicator"].tolist()

        if high_risk_indicators:
            st.write("**High-risk indicators identified:** " + ", ".join(high_risk_indicators))
        if warning_indicators:
            st.write("**Warning-level indicators identified:** " + ", ".join(warning_indicators))

    st.markdown("---")
    st.subheader("8. Interpretation Note")
    st.info("""
    This interactive checker uses a structured multi-indicator scoring framework to support
    preliminary bankruptcy risk assessment in an interpretable way. It is intended to show how
    financial ratios can be organised into a practical early warning module. In future development,
    this framework could be further strengthened using data-driven calibration or machine learning models.
    """)

# ---------------------------
# Conclusion
# ---------------------------
elif page == "Conclusion":
    st.title("Conclusion")

    st.markdown("""
    This final section summarises the key insights, project value, and possible future directions.
    """)

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Key Findings")
        st.markdown("""
- Financial indicators show measurable differences between bankrupt and non-bankrupt firms  
- Profitability, solvency, liquidity, efficiency, and cash-flow variables all provide useful signals  
- Several indicators are statistically significant in distinguishing the two groups  
- Outliers are common in financial ratio data, so robust analysis methods are important  
        """)

        st.subheader("Project Value")
        st.write(
            "This application demonstrates how exploratory financial analysis can support the design "
            "of a bankruptcy early warning system."
        )

    with c2:
        st.subheader("Next Step Suggestions")
        st.markdown("""
- Add machine learning models such as Logistic Regression or Random Forest  
- Replace the rule-based risk checker with a predictive model  
- Add user upload functionality for custom company data  
- Improve interactivity with dynamic charts and richer explanations  
        """)

        st.subheader("Available Outputs")
        st.markdown("""
- Cleaned dataset  
- Summary tables  
- EDA figures  
- Statistical test results  
- Rule-based early warning prototype  
        """)

    st.markdown("---")
    st.success("The project provides a clear foundation for extending from exploratory analysis to predictive financial risk modelling.")