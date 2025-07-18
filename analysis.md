# Credit Score Analysis (Aave V2 Wallets)

##This analysis is based on the output of the scoring model applied to transaction-level DeFi data.

---

##Score Distribution

```python
# Distribution code snippet from analysis.py(screenshot of graph is alos uploaded in github repo)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('wallet_scores.csv')
plt.hist(df['creditScore'], bins=10, edgecolor='black')
plt.title('Wallet Credit Score Distribution')
plt.xlabel('Credit Score')
plt.ylabel('Number of Wallets')
plt.grid(True)
plt.show()
