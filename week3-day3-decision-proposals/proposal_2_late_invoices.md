# Proposal 2: Predictive Late Invoice Payment Alert System

## 1. Problem
Delayed B2B invoice payments tie up working capital and force finance teams into reactive collections only *after* due dates pass[cite: 18, 20]. Flagging high-risk invoices at creation enables proactive follow-up before delinquency occurs[cite: 18, 20].

## 2. Recommended Approach
We recommend **Gradient Boosted Decision Trees (`XGBoost` or `Random Forest`) trained on structured historical billing data**, paired with SHAP feature attributions so finance collectors see *why* an invoice is flagged[cite: 20].

## 3. Data Requirements
* **Required Features:** `invoice_amount`, `payment_terms` (Net 15/30/60), `issue_date`, `due_date`, `customer_industry`, `historical_late_rate`, `avg_days_past_due`,