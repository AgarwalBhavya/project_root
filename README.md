# DeFi Wallet Credit Scoring - Aave V2

This project assigns a **credit score (0–1000)** to DeFi wallets based on their transaction behavior on the Aave V2 protocol using historical, transaction-level data.
---

## Overview

We analyze wallet interactions (deposit, borrow, repay, liquidation, etc.) with Aave V2 and apply engineered features with a rule-based model to generate scores that reflect user reliability.
---

##Features Extracted
- `total_transactions`: Number of actions
- `num_borrows`, `num_repays`, `num_liquidations`, etc.
- `total_borrowed_usd`, `total_repaid_usd`
- `repayment_ratio`: repaid / borrowed
- `liquidation_ratio`: liquidations / borrows
- `avg_borrow_rate`
- `active_days`, `asset_diversity`

---

## Score Scale

| Score Range | Meaning |
|-------------|---------|
| 800–1000    | Excellent behavior |
| 600–800     | Good |
| 400–600     | Moderate |
| 200–400     | Risky |
| 0–200       | Bot-like / exploit-prone |

---

Project Structure
project_root/
├── score_wallets.py
├── utils/
│   ├── features.py
│   └── scoring.py
├── sample.json
├── wallet_scores.csv
├── README.md
└── analysis.md

## How to Run

Install requirements:

```bash
pip install -r requirements.txt

Run scoring:
python score_wallets.py --input sample.json --output wallet_scores.csv

Output:
wallet_scores.csv – contains wallet addresses and their credit scores.

Methodology
We use heuristics based on repayment consistency, liquidation history, and activity patterns. More advanced models (e.g., LightGBM) can be trained with labeled data in future versions.


