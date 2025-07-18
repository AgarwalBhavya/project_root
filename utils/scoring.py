import pandas as pd

def score_wallets(df):
    # Basic heuristic model
    def heuristic_score(row):
        score = 500

        if row['repayment_ratio'] >= 0.95:
            score += 200
        elif row['repayment_ratio'] >= 0.75:
            score += 100
        else:
            score -= 100

        if row['liquidation_ratio'] > 0.3:
            score -= 200
        elif row['liquidation_ratio'] > 0:
            score -= 100

        if row['num_repays'] > row['num_borrows']:
            score += 50

        if row['active_days'] > 10:
            score += 50

        return max(0, min(1000, score))

    df['creditScore'] = df.apply(heuristic_score, axis=1)
    return df[['userWallet', 'creditScore']]
