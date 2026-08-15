# CloudWalk Risk Analyst I — External Case

![Python](https://img.shields.io/badge/Python-3.12.3-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-3.0-150458?logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Final%20Delivery-brightgreen)
![License](https://img.shields.io/badge/License-Case%20Study-lightgrey)

Fraud and chargeback risk analysis on a hypothetical card-not-present (CNP) transaction dataset, developed as the technical deliverable for the **Risk Analyst I — External Case**.

## Executive Summary

The dataset contains 3,199 CNP transactions, of which 391 (12.22%) show a fraud-related chargeback outcome. The analysis identifies four evidence-based risk signals — elevated transaction amounts, merchant-level chargeback concentration, repeated user × merchant chargeback relationships, and payment cards shared across users combined with short temporal proximity between their transactions. Device sharing was tested and found not to be a useful signal in this sample. These findings support prioritized business recommendations and a conceptual anti-fraud decision flow, followed by the payment-industry context required by the case and the limitations of the analysis.

## 1. Business Problem

Card-not-present transactions lack physical-card verification, which increases reliance on behavioral, transactional, and relationship signals to detect fraud. Undetected fraud results in chargebacks, which carry direct financial loss, fees, and operational cost for acquirers and merchants. The business problem addressed here is: **given a sample of transactions, which behavioral patterns are associated with fraud-related chargeback outcomes, and how can that evidence inform a risk-management response?**

## 2. Case Objectives

1. Analyze the provided transactional data and identify suspicious behaviors, explaining the evidence and the recommended actions.
2. Identify additional data sources that would strengthen fraud detection beyond the provided dataset.
3. Provide recommendations to prevent fraud and reduce chargebacks.
4. Design a conceptual or technical anti-fraud solution.
5. Explain the payment-industry context: money and information flow, acquirer vs. sub-acquirer vs. payment gateway, chargebacks vs. cancellations, and the role of anti-fraud systems for an acquirer.

## 3. Dataset

**File:** `data/raw/transactional-sample.csv`
**Observation period:** 2019-11-01 to 2019-12-01
**Environment:** Card-Not-Present (CNP)

| Field | Description |
|---|---|
| `transaction_id` | Unique transaction identifier |
| `merchant_id` | Merchant where the transaction occurred |
| `user_id` | Identifier of the cardholder |
| `card_number` | Payment card used |
| `transaction_date` | Timestamp of the transaction |
| `transaction_amount` | Transaction value |
| `device_id` | Identifier of the device used |
| `has_cbk` | Whether the transaction shows a fraud-related chargeback outcome |

**Baseline:**

| Metric | Value |
|---|---|
| Total transactions | 3,199 |
| Chargeback-related transactions | 391 |
| Non-chargeback transactions | 2,808 |
| Overall chargeback rate | 12.22% |

## 4. Methodology

The analysis followed a business-question-first approach: metrics and visualizations were included only where they addressed a specific risk question.

```
Raw Transactions
      │
      ▼
Data Quality Assessment
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Chargeback vs. Non-Chargeback Comparison
      │
      ▼
Behavioral Analysis (amount, time, user, merchant, card, device)
      │
      ▼
Relationship Analysis (user × merchant, shared cards, temporal proximity)
      │
      ▼
Risk Signal Prioritization
      │
      ▼
Recommendations & Conceptual Anti-Fraud Solution
```

## 5. Data Quality

[`notebooks/01_data_quality_assessment.ipynb`](notebooks/01_data_quality_assessment.ipynb) evaluates whether the available dataset is sufficiently consistent for exploratory analysis: column structure and types, missing values, duplicate records, and overall consistency.

## 6. Key Analytical Findings

Full detail, code, and charts are in [`notebooks/02_exploratory_data_analysis.ipynb`](notebooks/02_exploratory_data_analysis.ipynb).

### 6.1 Transaction Amount

Transactions with a fraud-related chargeback outcome carry substantially higher values than non-chargeback transactions.

| | Non-chargeback | Chargeback |
|---|---|---|
| Mean | R$ 672.32 | R$ 1,453.57 |
| Median | R$ 360.32 | R$ 999.47 |

Chargeback rate by transaction-value range:

| Range | Chargeback rate |
|---|---|
| R$ 0 – 100 | 2.97% |
| R$ 100 – 500 | 4.21% |
| R$ 500 – 1,000 | 19.84% |
| R$ 1,000 – 2,000 | 17.73% |
| R$ 2,000 – 3,000 | 31.16% |
| R$ 3,000 – 5,000 | 37.32% |

Higher transaction values are associated with higher chargeback incidence in this sample. This is an association, not proof that high-value transactions are fraudulent.

### 6.2 Temporal Behavior

Chargeback rate varies across the observation period: 13 of 31 days exceeded the 12.22% baseline, including 2019-11-27 (30.12%), 2019-11-25 (20.83%), 2019-11-30 (19.01%), 2019-11-08 (18.46%), 2019-12-01 (17.76%), and 2019-11-29 (17.70%). Temporal variation exists, but the dataset does not establish that these peaks reflect fraud-specific behavior.

### 6.3 User Behavior

A subset of users shows meaningful transaction volume combined with very high chargeback rates, e.g. user 96025 (14 transactions, 13 chargebacks, 92.86%), user 78262 (13 transactions, 12 chargebacks, 92.31%), user 79054 (17 transactions, 15 chargebacks, 88.24%), user 91637 (22 transactions, 19 chargebacks, 86.36%), and user 11750 (31 transactions, 25 chargebacks, 80.65%). A filtered high-risk group of 15 users accounts for 156 transactions, 141 chargebacks, and 36.06% of all chargebacks in the sample. Users with only a single transaction and a single chargeback were deliberately excluded as insufficient evidence.

### 6.4 Merchant Behavior

Chargebacks are strongly concentrated in a subset of merchants, e.g. merchant 1308 (15/15, 100%), merchant 44927 (11/11, 100%), and merchant 73271 (10/10, 100%). Using a threshold of ≥5 transactions and ≥80% chargeback rate, 23 merchants account for 193 transactions, 176 chargebacks, and 45.01% of all chargebacks. These are risk concentrations that warrant investigation, not evidence that the merchants are fraudulent.

### 6.5 User × Merchant Relationships

Several user–merchant pairs show repeated transactions with consistent chargeback outcomes, e.g. user 96025 × merchant 1308 (10/10), user 75710 × merchant 77130 (10/10), user 7725 × merchant 73271 (7/7), user 28218 × merchant 53041 (5/5), user 71424 × merchant 29214 (5/5), and user 79054 × merchant 1308 (5/5).

### 6.6 Shared Payment Cards

Cards used by more than one user show a markedly higher chargeback rate than cards used by a single user:

| Card type | Transactions | Chargebacks | Chargeback rate |
|---|---|---|---|
| Non-shared cards | 3,128 | 367 | 11.73% |
| Shared cards | 71 | 24 | 33.80% |

Examples of merchant × shared-card relationships with 100% chargeback outcomes: merchant 1308 + card ending ...7343 (2 users, 3 transactions), merchant 1308 + card ending ...5763 (2 users, 2 transactions), merchant 29214 + card ending ...3386 (2 users, 3 transactions), merchant 42356 + card ending ...4290 (2 users, 3 transactions), and merchant 63050 + card ending ...4880 (2 users, 2 transactions).

This is one of the strongest cross-dimensional findings in the analysis. Shared payment instruments are not inherently fraudulent — they may have legitimate explanations — but the elevated rate justifies further review.

### 6.7 Temporal Proximity of Shared Cards

Among investigated shared-card relationships, transactions occurred as little as ~3.1, ~42.9, and ~55.6 minutes apart (e.g. users 96025 and 79054 sharing a card at merchant 1308, ~55.6 minutes apart). Temporal proximity alone is not proof of fraud, but it strengthens the signal when combined with a shared instrument, multiple users, the same merchant, and chargeback outcomes.

### 6.8 Device Behavior

No device in the sample was associated with more than one user (maximum users per device: 1). `device_shared` did not provide a useful signal in this dataset and was excluded from prioritization — a relevant negative finding.

## 7. Prioritized Risk Signals

1. Higher transaction amounts
2. Merchant-level chargeback concentration
3. Repeated user × merchant chargeback behavior
4. Shared payment cards across users, particularly combined with temporal proximity

Device sharing was evaluated and ruled out as a signal for this dataset.

## 8. Business Recommendations

- Apply greater review priority to unusually high-value transactions.
- Monitor merchants with sustained abnormal chargeback concentrations.
- Use historical user × merchant chargeback behavior as review context.
- Monitor payment instruments reused by multiple users.
- Combine relationship and temporal signals rather than relying on a single rule.
- Introduce review or step-up authentication for selected medium-risk transactions.
- Continuously monitor outcomes and recalibrate thresholds as new data arrives.

These are recommendations derived from the analysis, not implemented production controls.

## 9. Additional Data for Fraud Detection

Beyond the fields provided, the following would materially strengthen fraud detection:

- Historical transaction behavior per user, card, and merchant
- IP address and network information
- Geolocation
- Device fingerprinting
- Authentication / 3DS data
- Account age and history
- Payment-instrument history
- Merchant profile and category
- Merchant historical risk performance
- Velocity across users, cards, devices, and merchants
- Historical fraud and chargeback history
- Behavioral and session-level signals

## 10. Payment Industry Context

**Money and information flow.** In a typical card transaction, the cardholder initiates a payment through a merchant. The merchant (often via a payment gateway) sends the transaction to an acquirer, which routes it through the card network (e.g. Visa, Mastercard) to the issuer — the cardholder's bank. The issuer authorizes or declines the transaction based on funds and risk checks; the response flows back through the same chain. Funds move in the opposite direction on settlement: from issuer to acquirer to merchant, net of interchange and scheme fees.

**Acquirer, sub-acquirer, and payment gateway.**
- An **acquirer** is a licensed financial institution that holds a direct relationship with the card networks, contracts merchants, and is ultimately responsible for settlement and risk exposure on the transactions it processes.
- A **sub-acquirer** (or payment facilitator) is not directly licensed by the card networks; it operates under an acquirer's infrastructure and license, onboarding and settling smaller merchants who would not qualify for a direct acquirer relationship on their own.
- A **payment gateway** is the technical layer that captures and encrypts transaction data at checkout and routes it to the acquirer or sub-acquirer; it does not hold settlement risk itself, unlike acquirers and sub-acquirers.

**Chargebacks vs. cancellations.** A **cancellation** is a transaction reversal initiated cooperatively, typically before or shortly after settlement, usually at the request of the customer or merchant. A **chargeback** is a forced reversal initiated by the cardholder's issuer, outside the merchant's control, usually because the cardholder disputes the transaction (including as unauthorized or fraudulent). Chargebacks carry additional fees and, at volume, can jeopardize a merchant's ability to keep processing with an acquirer.

**Chargebacks and fraud.** Not every chargeback is fraud — some result from service disputes or buyer's remorse — but a meaningful share of chargebacks in CNP environments are fraud-related, since fraudulent purchases are typically disputed by the legitimate cardholder once identified. This is why acquirers track chargeback rate as a core risk metric, and why the `has_cbk` field in this dataset (a fraud-related chargeback flag) is used as the primary indicator for this analysis.

**Anti-fraud in acquiring.** An anti-fraud system evaluates transactions — using rules, statistical models, or machine learning — to estimate the likelihood that a transaction is fraudulent, typically before authorization. Acquirers use anti-fraud systems to decide whether to approve, hold for manual review, or decline a transaction, balancing fraud loss against the friction imposed on legitimate customers. This balance is the same one addressed by the conceptual solution proposed in Section 11.

## 11. Conceptual Anti-Fraud Solution

The case allows for a conceptual or technical solution; this project proposes a conceptual decision flow rather than a production implementation, ML model, or scoring service:

```
Transaction
     │
     ▼
Risk Signals (amount, merchant history, user history,
              user × merchant history, card relationships,
              temporal/velocity behavior, prior chargebacks)
     │
     ▼
Risk Evaluation
     │
     ▼
APPROVE  /  REVIEW  /  DENY
     │
     ▼
Investigation
     │
     ▼
Feedback / Monitoring (recalibrate thresholds over time)
```

Transactions with few or no risk signals proceed normally (APPROVE). Transactions matching one or more prioritized signals — e.g. high value combined with a shared card and short temporal proximity — are routed to REVIEW for manual or step-up verification. Transactions matching multiple strong, corroborating signals could be subject to denial or additional verification depending on the operational risk policy. Outcomes feed back into the monitoring layer to keep thresholds current.

## 12. Limitations

- The dataset is hypothetical and may not reflect real-world transaction distributions.
- The observation window (one month) is limited.
- The `has_cbk` field indicates a fraud-related chargeback outcome; it is a business/operational signal, not a legal determination of fraud.
- Some extreme rates (e.g. 100% chargeback rate for a merchant or user) are computed from relatively small transaction counts and should be treated cautiously.
- No merchant category or business-context data was available.
- No IP, geolocation, authentication, or session data was available.
- The analysis identifies associations, not causal relationships.
- All risk signals require validation against a larger, labeled dataset before any production use.

## 13. Reproducibility

**Requirements:** Python environment with the packages listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

**Structure:**

```
cloudwalk-risk-analyst-case/
├── data/
│   └── raw/
│       └── transactional-sample.csv
├── notebooks/
│   ├── 01_data_quality_assessment.ipynb
│   └── 02_exploratory_data_analysis.ipynb
├── README.md
└── requirements.txt
```

**Execution order:**

1. [`notebooks/01_data_quality_assessment.ipynb`](notebooks/01_data_quality_assessment.ipynb) — validates structure, types, missing values, and duplicates.
2. [`notebooks/02_exploratory_data_analysis.ipynb`](notebooks/02_exploratory_data_analysis.ipynb) — runs the full exploratory and risk-signal analysis described above; executes end to end from the raw CSV.

## 14. Conclusion

The analysis of 3,199 CNP transactions identified four evidence-based risk signals — transaction amount, merchant concentration, repeated user × merchant relationships, and shared payment cards combined with temporal proximity — while ruling out device sharing as a useful signal for this dataset. These findings support a set of prioritized, proportionate business recommendations and a conceptual APPROVE / REVIEW / DENY decision flow, framed within the payment-industry context required by the case, and provide a defensible starting point for risk management that would need to be validated against a larger dataset before production use.

## Author

**Vagner Ferreira**
Data Analyst | Data Engineering | Data Science