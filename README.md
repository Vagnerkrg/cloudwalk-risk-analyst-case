# CloudWalk Risk Analyst Case

## Overview

This repository contains the analytical work developed for the **CloudWalk Risk Analyst I — External Case**.

The case simulates a real-world risk analysis scenario involving hypothetical payment transactions in a **Card-Not-Present (CNP)** environment.

The objective is not only to analyze the transactional dataset, but to demonstrate the analytical reasoning required to identify suspicious behaviors, understand their potential relationship with fraud and chargebacks, and translate those findings into practical risk-management solutions.

The project is being developed incrementally through GitHub Issues, with each stage addressing a specific analytical or business question.

> **Documentation note:** This README is intentionally concise during development. A final professional and executive-oriented version will be consolidated after the complete case has been analyzed.

---

## Case Objectives

The technical assessment requires addressing four main areas:

### 1. Transactional Analysis

Analyze the provided transaction data to:

* Identify suspicious behaviors.
* Detect relevant patterns associated with chargebacks.
* Explain the evidence supporting each finding.
* Determine what actions could be taken based on those findings.

### 2. Fraud Data Expansion

Identify additional data sources that could improve fraud detection beyond the provided spreadsheet.

Examples may include:

* Historical transaction behavior.
* Device intelligence.
* IP and network information.
* Geolocation.
* Velocity signals.
* Merchant characteristics.
* Card and account history.
* Authentication information.
* Behavioral signals.
* Previous fraud and chargeback history.

These data sources will be evaluated based on their potential analytical value rather than simply being listed.

### 3. Risk Recommendations

Based on the analytical findings, propose measures to:

* Prevent fraudulent transactions.
* Reduce chargebacks.
* Improve transaction monitoring.
* Prioritize transactions for manual review.
* Balance fraud prevention with legitimate customer experience.

### 4. Anti-Fraud Solution

Design a conceptual or technical solution capable of supporting:

* Fraud detection.
* Transaction risk scoring.
* Decisioning.
* Monitoring.
* Investigation.
* Human review when appropriate.

The proposed solution should connect directly to the patterns identified during the analysis.

---

# Industry Understanding

The second part of the case focuses on understanding the payments industry.

The project will address:

## Payment Industry Flows

Explain:

* Money flow.
* Information flow.
* Main participants in a payment transaction.
* The role and responsibilities of each participant.

## Acquirer, Sub-Acquirer and Payment Gateway

Analyze the differences between:

* Acquirer.
* Sub-acquirer.
* Payment gateway.

The analysis will also explain how transaction and information flows change depending on the participant involved.

## Chargebacks

Explain:

* What a chargeback is.
* How a chargeback differs from a cancellation.
* The relationship between chargebacks and fraud.
* The relevance of chargebacks within the acquiring ecosystem.

## Anti-Fraud

Explain:

* What an anti-fraud system is.
* How an acquirer can use anti-fraud capabilities.
* How risk decisions can be integrated into the payment flow.

---

# Dataset Context

The provided dataset contains hypothetical transactional information.

Important business definitions supplied by the case:

| Field       | Meaning                                                               |
| ----------- | --------------------------------------------------------------------- |
| `user_id`   | Identifier of the cardholder                                          |
| `device_id` | Identifier of the device used                                         |
| `has_cbk`   | Indicates whether the transaction received a fraud-related chargeback |

All transactions occurred in a **Card-Not-Present (CNP)** environment.

This context is important because CNP transactions do not provide the same physical-card verification signals available in card-present transactions, increasing the importance of behavioral, transactional, device, and contextual signals.

---

# Analytical Strategy

The analysis follows a progressive workflow designed to move from evidence to decision-making.

```text
Raw Transactions
       │
       ▼
Data Quality Assessment
       │
       ▼
Exploratory Data Analysis
       │
       ▼
Suspicious Behavior Identification
       │
       ▼
Chargeback Pattern Analysis
       │
       ▼
Risk Signal Investigation
       │
       ▼
Risk Scoring / Decision Logic
       │
       ▼
Business Recommendations
       │
       ▼
Anti-Fraud Solution
```

The guiding principle is:

> **Business questions first, analytical techniques second.**

Visualizations and metrics should only be included when they contribute to understanding transaction risk or support a business decision.

---

# Current Analytical Baseline

The current notebook analyzes:

* **3,199 transactions**
* **391 chargebacks**
* **12.22% overall chargeback rate**

An initial risk-scoring analysis was also developed as an exploratory baseline.

| Metric                           |            Result |
| -------------------------------- | ----------------: |
| Transactions analyzed            |             3,199 |
| Chargebacks                      |               391 |
| Chargeback rate                  |            12.22% |
| Review threshold                 | `risk_score >= 2` |
| Transactions selected for review |               354 |
| Review rate                      |            11.07% |
| Chargebacks captured             |               294 |
| Chargebacks not captured         |                97 |
| Precision                        |            83.05% |
| Recall                           |            75.19% |
| Specificity                      |            97.86% |

These results represent an **initial analytical baseline** and should not be interpreted as the final anti-fraud strategy.

Further analysis is required to determine which behavioral and transactional characteristics explain the observed risk.

---

# Analytical Questions

The project is designed around questions such as:

### Transaction Behavior

* How are transactions distributed?
* How are transaction amounts distributed?
* Are chargebacks concentrated in specific transaction-value ranges?
* Are there temporal patterns associated with chargebacks?

### User Behavior

* Are certain users associated with unusually high transaction frequency?
* Are chargebacks concentrated among specific behavioral profiles?
* Are there abnormal relationships between users and cards?

### Merchant Behavior

* Are some merchants associated with significantly different chargeback rates?
* Does transaction concentration by merchant provide useful risk information?

### Card Behavior

* Are cards associated with multiple users?
* Are certain cards involved in unusually frequent transactions?
* Are card-level patterns associated with chargebacks?

### Device Behavior

* Are devices shared by multiple users?
* Are devices associated with multiple cards?
* Do device-sharing patterns provide useful fraud signals?

### Combined Signals

* Do multiple weak signals become meaningful when combined?
* Which signals provide the strongest evidence of suspicious behavior?
* What percentage of transactions could reasonably be sent for additional review?
* What is the trade-off between fraud detection and customer friction?

---

# Project Structure

```text
cloudwalk-risk-analyst-case/
│
├── data/
│   └── raw/
│       └── transactional-sample.csv
│
├── notebooks/
│   └── 01_data_quality_assessment.ipynb
│
├── README.md
│
└── .gitignore
```

The repository intentionally remains lightweight because this is an analytical case rather than a production software system.

---

# Development Workflow

The project is organized through GitHub Issues.

Each issue represents a specific analytical or business milestone.

The current development sequence includes:

1. Data understanding and quality assessment.
2. Exploratory data analysis.
3. Suspicious behavior investigation.
4. Fraud and chargeback pattern analysis.
5. Risk signal development.
6. Recommendations.
7. Anti-fraud solution design.
8. Industry analysis.
9. Final case presentation.

The analysis is developed incrementally so that each conclusion can be traced back to supporting evidence.

---

# Current Issue

## Issue #5 — Build Exploratory Data Analysis

The next analytical milestone is to perform focused exploratory data analysis covering:

* Transaction volume.
* Transaction amounts.
* Chargeback rate.
* Temporal distribution.
* Users.
* Merchants.
* Cards.
* Devices.
* Differences between chargeback and non-chargeback transactions.

The notebook should prioritize analyses capable of answering business questions and identifying potential risk signals.

---

# Validation Principles

The project follows several validation principles:

### Reproducibility

The main notebook must execute successfully from beginning to end.

### Analytical Purpose

Every metric and visualization must have a clear analytical purpose.

### Evidence-Based Reasoning

Suspicious behaviors should be supported by measurable evidence rather than intuition alone.

### Business Relevance

Technical findings should ultimately translate into a risk-management implication or decision.

### Customer Centricity

Fraud prevention should consider both:

* Reduction of fraudulent transactions and chargebacks.
* Preservation of legitimate customer transactions.

### Practicality

Recommendations should consider how they could realistically be incorporated into an acquiring or payment environment.

---

# Scope of the Final Solution

The final case is expected to connect the following elements:

```text
Transaction Data
       │
       ▼
Risk Signals
       │
       ▼
Risk Assessment
       │
       ▼
Decision Engine
       │
 ┌─────┼──────────┐
 ▼     ▼          ▼
Approve Review   Decline
       │
       ▼
Investigation
       │
       ▼
Feedback / Monitoring
```

The final architecture will be refined based on the evidence discovered during the analysis.

---

# Final Deliverable

The completed case will consolidate:

* Data analysis.
* Suspicious behavior findings.
* Supporting evidence.
* Chargeback insights.
* Additional data recommendations.
* Fraud prevention recommendations.
* Anti-fraud solution proposal.
* Payment industry analysis.
* Clear business reasoning.
* Final conclusions.

The final presentation will prioritize **logical reasoning, analytical quality, problem solving, innovation, customer centricity, and solution performance**, consistent with the evaluation criteria described in the case.

---

# Final Documentation Plan

During development, this README will remain focused on project context and progress.

At the end of the case, it will be rewritten into a concise professional portfolio document containing:

* Executive summary.
* Business problem.
* Dataset overview.
* Analytical methodology.
* Key findings.
* Fraud and chargeback insights.
* Recommended actions.
* Anti-fraud solution.
* Industry context.
* Limitations.
* Reproducibility instructions.

The final version will avoid unnecessary implementation detail and focus on the reasoning and evidence that support the proposed solution.

---

## Author

**Vagner Ferreira**

Data Analyst / Data Engineering / Data Science

Brazil
