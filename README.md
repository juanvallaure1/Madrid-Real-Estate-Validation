# Madrid Real Estate Valuation & Investment Strategy 🏠

**Prepared for:** Fictional Investment Fund | **Context:** Strategic Data Science Assessment

Link to access the dataset: https://drive.google.com/drive/folders/10kagfgpB-VfztGrPkN-u7fwIg9FxiRFL?usp=drive_link

## 📌 Project Overview
This repository contains a comprehensive machine learning analysis of the Madrid housing market. Using a dataset of ~200,000 listings, we developed an **XGBoost** regression model to identify market inefficiencies.

The goal was to detect **"Real Estate Gems"**: properties listed at least **10-15% below their intrinsic AI Fair Value**, offering immediate equity potential.

## 📂 Repository Structure

- **`notebooks/`**: The detailed 3-stage data science pipeline:
  - `01_Data_Cleaning`: Preprocessing, outlier removal, and structural cleaning.
  - `02_EDA_Feature_Engineering`: Geolocation clustering (K-Means), price volatility analysis.
  - `03_Modeling_Evaluation`: Model training (XGBoost), hyperparameter tuning, and test set validation.
- **`reports/`**: 
  - The full strategic PDF report (`main.pdf`) generated in LaTeX.
  - Source `.tex` files.
- **`results/`**: 
  - `RAPADA_PARTNERS_Opportunity_Dossier.xlsx`: The final list of top investment candidates found in both Train and Test sets.

## 🚀 Key Findings
- **Model Accuracy:** Achieved an R² of ~0.84 with a Mean Absolute Error (MAE) consistent with industry valuation standards.
- **Opportunity:** Identified ~500 properties with >10% potential profit margin.
- **Strategy:** Recommendation to focus on "Motivated Sellers" (listings with price drops) combined with our AI undervaluation signal.

## 🛠️ Tech Stack
- **Python:** Pandas, NumPy, Scikit-Learn, XGBoost, Matplotlib/Seaborn.
- **Reporting:** LaTeX for documentation.

---
*For any inquiries regarding the code or the investment dossier, please refer to the notebooks provided.*
