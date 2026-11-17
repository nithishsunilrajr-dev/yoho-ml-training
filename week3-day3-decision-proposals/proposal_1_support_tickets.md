# Proposal 1: Automated Support Ticket Categorisation

## 1. Problem
Support agents spend 15–20 minutes per hour manually reading and routing incoming customer tickets across 8 categories (Billing, Technical Bug, Account Access, Refund, Feature Request, etc.)[cite: 19]. Manual triage delays first-response times and causes misrouted tickets during peak volume[cite: 19].

## 2. Recommended Approach
We recommend a **Supervised Machine Learning Classifier (TF-IDF + Logistic Regression / LinearSVC)** rather than keyword rules or a Generative LLM[cite: 19]:
* **Why not Keyword Rules?** Brittle on phrasing variations (e.g., *"charged twice"* vs. *"duplicate debit"*) and expensive to maintain as ticket volume grows[cite: 19].
* **Why not an LLM?** Overkill for fixed 8-class routing; adds per-ticket API cost and 1–3s latency when a local classifier runs in <5ms[cite: 19].

## 3. Data Requirements
* **Minimum Dataset:** 4,000–8,000 historical resolved tickets (~500–1,000 labelled examples per category)[cite: 14, 19].
* **Required Fields:** `ticket_subject`, `ticket_body`, `created_at`, and verified `category_label`[cite: 19].
* **Client Deliverables:** 12-month historical ticket export and sign-off on the 8-category taxonomy[cite: 19].

## 4. Evaluation Metric
* **Primary Metric:** **Macro F1-Score** (weights rare categories like *Security Incident* equally with high-volume categories like *Billing*)[cite: 19].
* **Secondary Metric:** Per-class Precision and Recall[cite: 19].
* **Target Benchmark:** **Macro F1 ≥ 0.85** and **≥ 90% accuracy** on auto-routed tickets[cite: 19].

## 5. Estimated Build Time
* **Total Effort:** **5 Working Days**[cite: 19]
  * Day 1: Data extraction, PII scrubbing, and label quality audit[cite: 19].
  * Days 2–3: Text cleaning, TF-IDF feature engineering, and baseline vs. tuned classifier training[cite: 19].
  * Day 4: Confidence threshold calibration and error analysis with support leads[cite: 19].
  * Day 5: FastAPI webhook integration and monitoring setup[cite: 19].

## 6. Key Trade-Offs
* **Automation Coverage vs. Precision:** Setting a confidence threshold of `≥ 0.75` auto-routes ~80% of tickets at >92% accuracy while sending ambiguous tickets to a human triage queue, avoiding costly misroutes[cite: 19].

## 7. Risk & Mitigation (Bonus)
* **Failure Case 1 – Multi-issue tickets (e.g., refund request + login bug):** Produces split class probabilities; mitigated by routing tickets with max probability `< 0.70` to a human Tier-1 agent[cite: 19].
* **Failure Case 2 – New product terminology (concept drift):** Unseen feature names cause misrouting; mitigated by logging human overrides weekly and retraining monthly[cite: 19].