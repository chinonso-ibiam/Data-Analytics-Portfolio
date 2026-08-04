import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
df = pd.read_csv('Customer_churn.Csv')

plt.figure(figsize=(6,5))

sns.boxplot(
x='Churn',
y='MonthlyCharges',
data=df,
palette=['#70AD47','#C55A11']
)

plt.title(
"Monthly Charges vs Churn",
fontsize=14,
fontweight='bold'
)

plt.show()