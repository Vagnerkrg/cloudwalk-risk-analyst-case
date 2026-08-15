# CloudWalk Risk Analyst I — External Case

Fraud and chargeback risk analysis on a hypothetical card-not-present (CNP) transaction dataset, developed as the technical deliverable for the **Risk Analyst I — External Case**.

## Executive Summary

The dataset contains 3,199 CNP transactions, of which 391 (12.22%) resulted in a fraud-related chargeback. The analysis identifies four evidence-based risk signals — elevated transaction amounts, merchant-level chargeback concentration, repeated user × merchant chargeback relationships, and payment cards shared across users combined with short temporal proximity between their transactions. Device sharing was tested and found not to be a useful signal in this sample. These findings are translated into prioritized business recommendations and a conceptual anti-fraud decision flow, followed by a discussion of the payment industry context and the limitations of the analysis.

## 1. Business Problem

Card-not-present transactions lack physical-card verification, which increases reliance on behavioral, transactional, and relationship signals to detect fraud. Undetected fraud results in chargebacks, which carry direct financial loss, fees, and operational cost for acquirers and merchants. The business problem addressed here is: **given a sample of transactions, which behavioral patterns are associated with fraud-related chargebacks, and how can that evidence inform a risk-management response?**

## 2. Case Objectives

1. Analyze the provided transactional data and identify suspicious behaviors, explaining the evidence and the recommended actions.
2. Identify additional data sources that would strengthen fraud detection beyond the provided dataset.
3. Provide recommendations to prevent fraud and reduce chargebacks.
4. Design a conceptual or technical anti-fraud solution.
5. Present the payment-industry context: money and information flow, acquirer vs. sub-acquirer vs. payment gateway, chargebacks, and the role of anti-fraud systems.

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
| `has_cbk` | Whether the transaction received a fraud-related chargeback |

**Baseline:**

| Metric | Value |
|---|---|
| Total transactions | 3,199 |
| Chargebacks | 391 |
| Non-chargebacks | 2,808 |
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

`notebooks/01_data_quality_assessment.ipynb` validates the dataset before analysis: column structure and types, missing values, duplicate records, and overall consistency. This step establishes that the dataset is analytically reliable and ready for exploratory analysis.

## 6. Key Analytical Findings

Full detail, code, and charts are in `notebooks/02_exploratory_data_analysis.ipynb`.

### 6.1 Transaction Amount

Chargeback transactions carry substantially higher values than non-chargeback transactions.

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

A subset of users shows meaningful transaction volume combined with very high chargeback rates, e.g. user 96025 (14 transactions, 13 chargebacks, 92.86%), user 91637 (22 transactions, 19 chargebacks, 86.36%), and user 11750 (31 transactions, 25 chargebacks, 80.65%). A filtered high-risk group of 15 users accounts for 156 transactions, 141 chargebacks, and 36.06% of all chargebacks in the sample. Users with only a single transaction and a single chargeback were deliberately excluded as insufficient evidence.

### 6.4 Merchant Behavior

Chargebacks are strongly concentrated in a subset of merchants, e.g. merchant 1308 (15/15, 100%), merchant 44927 (11/11, 100%), and merchant 73271 (10/10, 100%). Using a threshold of ≥5 transactions and ≥80% chargeback rate, 23 merchants account for 193 transactions, 176 chargebacks, and 45.01% of all chargebacks. These are risk concentrations that warrant investigation, not evidence that the merchants are fraudulent.

### 6.5 User × Merchant Relationships

Several user–merchant pairs show repeated transactions with consistent chargeback outcomes, e.g. user 96025 × merchant 1308 (10/10), user 75710 × merchant 77130 (10/10), and user 7725 × merchant 73271 (7/7).

### 6.6 Card Behavior — Shared Payment Cards

Cards used by more than one user show a markedly higher chargeback rate than cards used by a single user:

| Card type | Transactions | Chargebacks | Chargeback rate |
|---|---|---|---|
| Non-shared cards | 3,128 | 367 | 11.73% |
| Shared cards | 71 | 24 | 33.80% |

This is one of the strongest cross-dimensional findings in the analysis. Shared payment instruments are not inherently fraudulent — they may have legitimate explanations — but the elevated rate justifies further review.

### 6.7 Temporal Proximity of Shared Cards

Among investigated shared-card relationships, transactions occurred as little as ~3.1, ~42.9, and ~55.6 minutes apart (e.g. users 96025 and 79054 sharing a card at merchant 1308, ~55.6 minutes apart). Temporal proximity alone is not proof of fraud, but it strengthens the signal when combined with a shared instrument, multiple users, the same merchant, and chargeback outcomes.

### 6.8 Device Behavior

No device in the sample was associated with more than one user (maximum users per device: 1). `device_shared` did not provide a useful signal in this dataset and was not prioritized — a relevant negative finding.

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
- Introduce review / step-up authentication for selected medium-risk transactions.
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

## 10. Conceptual Anti-Fraud Solution

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

Transactions with few or no risk signals proceed normally (APPROVE). Transactions matching one or more prioritized signals — e.g. high value combined with a shared card and short temporal proximity — are routed to REVIEW for manual or step-up verification. Transactions matching multiple strong, corroborating signals may be routed to DENY. Outcomes feed back into the monitoring layer to keep thresholds current.

## 11. Limitations

- The dataset is hypothetical and may not reflect real-world transaction distributions.
- The observation window (one month) is limited.
- A chargeback outcome (`has_cbk`) indicates a fraud-related chargeback but is not equivalent to legal proof of fraud.
- Some extreme rates (e.g. 100% chargeback rate for a merchant or user) are computed from relatively small transaction counts and should be treated cautiously.
- No merchant category or business-context data was available.
- No IP, geolocation, authentication, or session data was available.
- The analysis identifies associations, not causal relationships.
- All risk signals require validation against a larger, labeled dataset before any production use.

## 12. Reproducibility

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

1. `notebooks/01_data_quality_assessment.ipynb` — validates structure, types, missing values, and duplicates.
2. `notebooks/02_exploratory_data_analysis.ipynb` — runs the full exploratory and risk-signal analysis described above; executes end to end from the raw CSV.

## 13. Conclusion

The analysis of 3,199 CNP transactions identified four evidence-based risk signals — transaction amount, merchant concentration, repeated user × merchant relationships, and shared payment cards combined with temporal proximity — while ruling out device sharing as a useful signal for this dataset. These findings support a set of prioritized, proportionate business recommendations and a conceptual APPROVE / REVIEW / DENY decision flow, providing a defensible starting point for risk management that would need to be validated against a larger dataset before production use.

## Author

**Vagner Ferreira**
Data Analyst / Data Engineering / Data Science