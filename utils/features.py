import pandas as pd
import numpy as np

def extract_features(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df['date'] = df['timestamp'].dt.date

    features = []
    grouped = df.groupby('userWallet')

    for wallet, group in grouped:
        f = {}
        f['userWallet'] = wallet
        f['total_transactions'] = len(group)
        f['num_borrows'] = (group['action'] == 'borrow').sum()
        f['num_repays'] = (group['action'] == 'repay').sum()
        f['num_deposits'] = (group['action'] == 'deposit').sum()
        f['num_liquidations'] = (group['action'] == 'liquidationcall').sum()

        group['usd_value'] = group.apply(lambda row: float(row['actionData'].get('amount', 0)) * float(row['actionData'].get('assetPriceUSD', 1)), axis=1)

        f['total_borrowed_usd'] = group[group['action'] == 'borrow']['usd_value'].sum()
        f['total_repaid_usd'] = group[group['action'] == 'repay']['usd_value'].sum()

        f['repayment_ratio'] = (
            f['total_repaid_usd'] / f['total_borrowed_usd']
            if f['total_borrowed_usd'] > 0 else 0
        )
        f['liquidation_ratio'] = (
            f['num_liquidations'] / f['num_borrows']
            if f['num_borrows'] > 0 else 0
        )

        borrow_rates = []
        for _, row in group.iterrows():
            if row['action'] == 'borrow':
                try:
                    rate = float(row['actionData'].get('borrowRate', 0))
                    borrow_rates.append(rate)
                except:
                    continue
        f['avg_borrow_rate'] = np.mean(borrow_rates) if borrow_rates else 0

        f['asset_diversity'] = len(set([a['assetSymbol'] for a in group['actionData'] if 'assetSymbol' in a]))
        f['active_days'] = len(group['date'].unique())

        features.append(f)

    return pd.DataFrame(features)
