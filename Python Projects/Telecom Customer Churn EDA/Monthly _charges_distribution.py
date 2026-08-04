import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
df = pd.read_csv('Customer_churn.Csv')

plt.figure(figsize=(6,5))

sns.histplot(df['MonthlyCharges'], bins=30, color="#2E75B6")

plt.title("Monthly Charges Distribution", fontsize=14, fontweight='bold')

plt.show()