[README.md](https://github.com/user-attachments/files/27099297/README.md)
## links
github: https://github.com/neeeo102/financial-risk-bankruptcy-warning-tool

video:  https://video.xjtlu.edu.cn/Mediasite/MyMediasite/embedded/presentations/c657294ae08444e5a1350f59a17b605c1d

## 1.Project Title

# Financial Risk Analysis and Bankruptcy Early Warning Tool

*A Python and Streamlit-based interactive prototype for bankruptcy risk screening using financial indicators.*

## Problem

This project investigates whether financial indicators can help identify patterns associated with corporate bankruptcy risk and support the development of an interpretable early warning tool.

### target users
The target users are students, beginner financial analysts, and non-technical users who want to explore bankruptcy-related financial patterns through a simple interactive interface. The product is designed for preliminary risk screening and educational analysis rather than formal investment, lending, or regulatory decision-making.

---

## 2. Data

This project uses a public firm-level bankruptcy dataset containing financial indicators and a binary bankruptcy label.

- **Dataset source**: Kaggle, *Company Bankruptcy Prediction*, https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction
- **Access date**: 22 April 2026
- **Target variable**: `Bankrupt`
- **Dataset type**: Enterprise financial ratio and accounting indicator data

### Repository data files
- `data.csv` – original dataset used for the notebook workflow
- `outputs/cleaned_data.csv` – cleaned dataset after column standardisation
- `outputs/tables/` – exported summary tables
- `outputs/figures/` – exported figures used in the Streamlit application

### Main feature categories
The analysis focuses on financially meaningful feature groups, including:

- **Profitability**  
  e.g. ROA-related variables, operating profit measures, net income ratios

- **Liquidity**  
  e.g. current ratio, quick ratio, cash-to-liability measures

- **Solvency / Leverage**  
  e.g. debt ratio, liability-to-equity, borrowing dependency

- **Efficiency**  
  e.g. asset turnover, receivables turnover, inventory turnover

- **Cash Flow**  
  e.g. cash flow to liability, cash flow to assets, CFO-based indicators

### Why this dataset was selected
This dataset was chosen because it is directly relevant to **financial distress and bankruptcy analysis** and contains a broad set of enterprise financial indicators suitable for exploratory analysis, statistical comparison, and interactive early warning design.

### If the raw data file is missing
If `data.csv` is not included in the repository due to file size or source restrictions:

1. Visit the Kaggle dataset page above
2. Download the dataset manually
3. Rename the file as `data.csv`
4. Place it in the project root directory（Don't put it in a subdirectory）

---

## 3. Methods

This project combines a Python-based exploratory analysis workflow with a Streamlit interactive application.

### Notebook workflow
The notebook performs the following tasks:

1. **Data loading**
   - Read the original dataset from `data.csv`

2. **Column cleaning and standardisation**
   - Remove spacing inconsistencies
   - Rename long or corrupted financial feature names
   - Standardise column naming for easier downstream analysis

3. **Dataset overview and quality checking**
   - Inspect shape, data types, missing values, and duplicates
   - Export data quality summary tables

4. **Target variable analysis**
   - Analyse the distribution of `Bankrupt`
   - Check whether class imbalance is present

5. **Financial feature grouping**
   - Organise variables into:
     - profitability
     - liquidity
     - solvency / leverage
     - efficiency
     - cash flow

6. **Descriptive analysis**
   - Produce summary statistics for key financial indicators

7. **Group comparison by bankruptcy status**
   - Compare mean values between bankrupt and non-bankrupt firms
   - Identify variables with larger group differences

8. **Visual analysis**
   - Count plots
   - Boxplots
   - KDE / distribution plots
   - Correlation heatmaps
   - Category comparison charts
   - Outlier ratio charts

9. **Outlier analysis**
   - Use the IQR rule to estimate outlier ratios across numerical variables

10. **Statistical testing**
    - Apply the **Mann–Whitney U test** to compare feature distributions between groups
    - Export significance results for interpretation

11. **Export outputs**
    - Save cleaned data, tables, and figures to the `outputs/` folder
    - Reuse these outputs in the Streamlit product


### Streamlit application

The Streamlit app transforms the analytical outputs into an accessible interface with the following modules:

- **Home**
- **Dataset Overview**
- **EDA Visualisations**
- **Statistical Results**
- **Risk Checker**
- **Conclusion**

### Risk checker design
The **Risk Checker** is a rule-based, interpretable early warning prototype.

It uses selected financial indicators to evaluate user input across four dimensions:

- **Profitability**
- **Liquidity**
- **Leverage**
- **Cash Flow & Coverage**

Users can:

- choose preset company profiles
- manually enter financial indicators
- observe changes in:
  - risk score
  - risk level
  - primary risk driver
  - warning indicators

This design allows users to test different financial scenarios and observe how selected accounting indicators may change the overall preliminary risk profile.

---

## 4. Key Findings

The analysis suggests that financial indicators contain meaningful differences between bankrupt and non-bankrupt firms and can support preliminary early warning analysis.

### Main findings

1. **Profitability-related indicators show clear differences between groups.**  
   Variables such as ROA-related measures and income-based ratios help distinguish financially weaker firms.

2. **Liquidity and leverage variables provide strong warning signals.**  
   Indicators such as current ratio, quick ratio, debt ratio, and liability-to-equity are useful for bankruptcy-related screening.

3. **Cash flow and repayment capacity add important information.**  
   Cash-flow-based indicators and coverage-related measures strengthen the interpretation of financial distress risk.

4. **Several financial variables are statistically significant.**  
   Mann–Whitney U test results suggest that multiple indicators differ meaningfully between bankrupt and non-bankrupt groups.

5. **Financial ratio data contains many outliers.**  
   This supports the use of robust analysis methods and cautious interpretation when applying threshold-based warning logic.

---

## 5. How to Run

### Run the Streamlit app locally

1. Option A:Clone this repository:
   ```bash
   git clone https://github.com/neeeo102/financial-risk-bankruptcy-warning-tool.git
   cd financial-risk-bankruptcy-warning-tool
   


   Option B: Download ZIP from GitHub
   Go to the link: https://github.com/neeeo102/financial-risk-bankruptcy-warning-tool
   press: code → download zip
   
2. Install the required packages:
   ```bash
   pip install -r requirements.txt

3. Launch the program

   1. Open Command Prompt or PowerShell.  
   2. Navigate to the project folder:

   ```bash
   cd financial-risk-bankruptcy-warning-tool
   streamlit run app.py

## 6. Limitations

This project has several limitations that should be acknowledged:

1. **Dataset dependency**  
   The analysis and warning results are highly dependent on the quality, completeness, and representativeness of the dataset used. If the input data contains noise, missing values, or sampling bias, the results may be affected.

2. **Limited generalisability**  
   The system is developed based on a specific bankruptcy dataset, so its findings may not fully generalise to companies from different industries, countries, or time periods.

3. **Rule-based risk checker**  
   The early warning tool currently uses a simplified rule-based scoring approach rather than a fully trained predictive model. Therefore, it should be viewed as a prototype for risk indication rather than a definitive bankruptcy prediction system.

4. **Static analysis**  
   The project mainly analyses historical financial indicators and does not incorporate real-time updates or dynamic market conditions. As a result, it cannot fully capture sudden changes in a company’s financial health.

5. **Limited feature scope**  
   Only the variables available in the dataset are included in the analysis. Other important factors, such as macroeconomic conditions, corporate governance, industry competition, or qualitative business information, are not considered.

6. **Visualisation and interpretation constraints**  
   While the dashboard helps users explore the data, the interpretation of results still requires financial knowledge. The visualisations provide descriptive insights, but they do not replace professional financial judgement.

## 7. notes（one more reminder）
   ### If the raw data file is missing
   If `data.csv` is not included in the repository due to file size or source restrictions:

   1. Visit the Kaggle dataset page above
   2. Download the dataset manually
   3. Rename the file as `data.csv`
   4. Place it in the project root directory (Don't put it in a subdirectory)
