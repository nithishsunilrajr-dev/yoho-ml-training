# Proposal 3: Internal HR Policy Q&A Assistant

## 1. Problem
Employees repeatedly message HR with routine questions on leave encashment, parental leave, travel reimbursements, and appraisal rules buried across lengthy PDF handbooks, slowing down HR operations.

## 2. Recommended Approach
We recommend **Retrieval-Augmented Generation (`RAG + LLM`)** using hybrid semantic + keyword search with strict citation guardrails:
* **Why not Fine-Tuning?** Fine-tuning cannot reliably memorize exact policy figures, cannot enforce per-user document permissions, and requires retraining whenever policies change.
* **Why not Plain Keyword Search?** Fails when employees use natural phrasing (e.g., *"carry forward unused leaves"*) that differs from exact policy terminology (*"Privilege Leave Accumulation"*).

## 3. Data Requirements
* **Source Documents:** Official HR Policy PDFs/DOCX files (Leave, Travel, POSH, Benefits, IT Security) with clean section headings and effective dates.
* **Update Frequency:** Automated re-indexing whenever HR publishes revised policy documents (monthly/quarterly), archiving outdated versions.
* **Access Control (RBAC):** Vector metadata filtering by `employee_grade`, `department`, and `location` so restricted policies are only retrieved for eligible employees.

## 4. Evaluation Metric
* **Retrieval Precision@3:** **≥ 85%** (relevant policy clause appears in top 3 retrieved chunks).
* **Faithfulness:** **≥ 95%** (zero unsupported claims outside retrieved chunks, evaluated via RAGAS).
* **Answer Relevancy:** **≥ 90%** with mandatory document/page citations.

## 5. Estimated Build Time
* **Total Effort:** **7 Working Days** (Days 1–2: Document chunking & RBAC metadata tagging; Days 3–4: Vector DB indexing & hybrid retrieval; Day 5: Prompt guardrails & citation formatting; Days 6–7: RAGAS evaluation on 50 golden HR Q&A pairs & Slack/Teams rollout).

## 6. Key Trade-Offs
* **Hallucination Risk vs. Speed:** Adding a faithfulness verification check and strict *"I don't know—contact HR"* fallback increases latency from ~1.5s to ~3s, which is essential to avoid fabricated policy promises.
* **Human-in-the-Loop:** Queries involving disciplinary actions, medical exemptions, termination, or low retrieval confidence (`< 0.65`) automatically escalate to a human HR Business Partner.

## 7. Monthly Cost Estimate (Bonus: 200 Employees × 5 Questions/Month = 1,000 Queries/Month)
* **LLM API Tokens:** ~2,500 input tokens + ~300 output tokens per query = 2.5M input + 0.3M output tokens/month ≈ **$1.00 – $3.50/month** (using GPT-4o-mini / Gemini Flash).
* **Embeddings & Vector DB:** 1,000 query embeddings + ~500 policy chunks = **<$0.10/month** (free tier on Qdrant/pgvector).
* **Total Estimated Running Cost:** **~$2 to $5 per month**.