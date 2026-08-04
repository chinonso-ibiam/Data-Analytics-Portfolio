import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
df = pd.read_csv('Customer_churn.Csv')

plt.figure(figsize=(6,5))

sns.histplot(df['tenure'], bins=20,color="#1F4E79")

plt.title("Customer Tenure Distribution", fontsize=14, fontweight='bold')

plt.show()