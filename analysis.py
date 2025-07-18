import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('wallet_scores.csv')
plt.hist(df['creditScore'], bins=10, edgecolor='black')
plt.title('Wallet Credit Score Distribution')
plt.xlabel('Credit Score')
plt.ylabel('Number of Wallets')
plt.grid(True)
plt.show()

