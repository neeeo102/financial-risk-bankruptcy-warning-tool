[README.md](https://github.com/user-attachments/files/27099297/README.md)
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
4. Place it in the project root directory

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

### Option A: Run the Streamlit app locally

1. Clone this repository:
   ```bash
   git clone [Insert your GitHub repository link here]
   cd [Insert repository folder name here]
