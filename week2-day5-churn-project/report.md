# Customer Churn Prediction – One-Page Executive Report

## 1. Problem
Telecom subscriber churn directly reduces monthly recurring revenue (MRR), and acquiring new customers costs significantly more than retaining existing ones[cite: 2]. The goal of this project is to predict which customers are likely to churn so the retention team can intervene proactively with targeted offers[cite: 2].

## 2. Data
* **Dataset:** IBM Telco Customer Churn (`7,043` customer records, `20` features, `26.5%` churn rate)[cite: 3].
* **Splitting Strategy:** Immediately held out a stratified **20% test set (`1,409` rows)** prior to EDA, feature engineering, or scaling to eliminate data leakage[cite: 3].

## 3. Method
* **Feature Engineering:** Created 4 domain features inside a custom `FeatureEngineer` transformer: `tenure_group`, `avg_spend_per_month`, `charge_diff`, and `total_services`[cite: 3].
* **Preprocessing & Modeling:** Built a leak-free `ColumnTransformer` + `Pipeline` (`SimpleImputer`, `StandardScaler`, `OneHotEncoder`) and evaluated Dummy, Logistic Regression, Random Forest, and XGBoost (`scale_pos_weight`) using 5-fold stratified cross-validation[cite: 2, 3].
* **Tuning & Threshold Calibration:** Tuned the top 2 models via `RandomizedSearchCV` (`scoring='roc_auc'`) and calibrated the decision threshold on out-of-fold probabilities to capture **≥ 75% of churners**[cite: 2].

## 4. Results (Final Held-Out Test Set)
* **Selected Model:** Tuned XGBoost Classifier[cite: 2]
* **Chosen Business Threshold:** `[Paste your printed threshold, e.g., 0.4125]`[cite: 2]
* **Test ROC-AUC:** `[Paste your printed Test ROC-AUC, e.g., 0.8442]`[cite: 2]
* **Test F1-Score:** `[Paste your printed Test F1, e.g., 0.6318]`[cite: 2]
* **Confusion Matrix:** `[[TN, FP], [FN, TP]]` → `[Paste your printed confusion matrix]`[cite: 2]

## 5. Limitations
* **Static Snapshot Data:** The dataset captures a single point-in-time profile without temporal usage decay, billing complaints, or customer support call sentiment.
* **Calibration Drift:** Promotional pricing changes or competitor launches can shift churn probabilities over time, requiring quarterly monitoring.

## 6. Recommendations
1. **Target Month-to-Month Fiber Subscribers:** Offer discounted 12-month contract upgrades to high-risk month-to-month customers (`churn_probability >= threshold`) within their first 12 months[cite: 2].
2. **Bundle Security & Tech Support:** Provide a 3-month free trial of `OnlineSecurity` and `TechSupport` to single-service users to increase product stickiness[cite: 2].
3. **Automated Weekly Scoring:** Run `src/predict_new.py` weekly to export top at-risk customer lists into CRM retention campaigns[cite: 2].