# Week 3 – Day 1 (Second Half): Data Quality Report & Decision Table

## Task 1: Client-Readable Data Quality Report (5 Lines)
1. We audited 32 customer records and found 3 exact duplicate entries, inconsistent city spellings (`CHENNAI `, `chennai`), and 12.5% missing email addresses[cite: 13].
2. Validation rules also flagged impossible age values (`-5` and `250`) and malformed phone numbers that did not match the standard 10-digit format[cite: 13].
3. All duplicate rows were removed, city names were standardized to clean Title Case, and invalid ages were replaced with the median valid customer age[cite: 13].
4. Rather than deleting customers with missing emails or invalid phone lengths, we added binary quality flags (`email_missing_flag`, `valid_phone_flag`) so outreach teams can filter records safely[cite: 13].
5. The cleaned 29-row `customers_clean.csv` dataset is now 100% schema-compliant and ready for CRM ingestion or predictive modeling[cite: 13].

## Task 2: When ML Is the Wrong Choice (Decision Table)

| Problem | Recommended Tool | One-Line Justification |
| :--- | :--- | :--- |
| **(a) Calculate GST on an invoice** | **Python rule** | Tax calculation follows a deterministic mathematical formula (`amount * rate`) where probabilistic ML would introduce compliance errors[cite: 14]. |
| **(b) Find the order status for order 1042** | **SQL** | Looking up a specific record by primary key from a structured database requires an exact `SELECT` query, not prediction[cite: 14]. |
| **(c) Predict which customers will leave next month** | **ML model** | Customer churn depends on subtle non-linear patterns across historical usage, billing, and tenure that require statistical learning[cite: 14]. |
| **(d) Answer questions from a 60-page policy PDF** | **LLM (with RAG)** | Extracting and synthesizing answers from unstructured natural language documents requires semantic retrieval and language comprehension[cite: 14]. |
| **(e) Flag invoices above 1 lakh for approval** | **Python rule** | A fixed monetary threshold (`invoice_amount > 100000`) is an explicit business policy best enforced by a deterministic `if/else` rule[cite: 14]. |

## What the Sample-Size Plot Says About Data Requirements (3 Lines)
1. At very small sample sizes (50–100 rows), test accuracy is low and unstable because the model memorizes noise instead of learning generalizable patterns[cite: 14].
2. Performance improves sharply between 100 and 500 samples and begins to stabilize once training data approaches ~1,000+ labelled examples per class[cite: 14].
3. Before committing to custom supervised ML on a client project, we must confirm ~1,000+ clean labelled examples per class exist—otherwise deterministic rules or pre-trained models are better choices[cite: 14].

## Bonus Challenge: Real Process Better Solved with SQL/Rules
* **Leave Balance & Eligibility Validation:** Employees often ask an AI chatbot whether they can take 4 days of earned leave next week, which looks like an AI problem; however, checking remaining leave quota and overlapping company holidays is 100% governed by structured HR database balances and deterministic `if/else` rules—making SQL + Python rules faster, zero-cost, and 100% accurate without hallucination risk[cite: 14].