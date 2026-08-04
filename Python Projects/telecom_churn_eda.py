
# =====================================
# Telecom Customer Churn Analysis
# Author: Chinonso Ibiam
# =====================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# Load Data

df = pd.read_csv("Customer_churn.csv")

# Dataset Inspection

print(df.head())
print(df.info())

# Churn Distribution

plt.figure(figsize=(5,5))
sns.countplot( x='Churn', data=df, palette= ['#70AD47','#C55A11'] )
plt.title("Customer Churn Distribution", fontsize=14, fontweight='bold')
plt.show()

# Churn by Contract Type

plt.figure(figsize=(6,6))
sns.countplot(x='Contract', hue='Churn', data=df,palette=['#70AD47','#1F4E79'] )
plt.title("Churn by Contract Type", fontsize=14, fontweight='bold'
 )
plt.xticks(rotation=15)
plt.show()

# Monthly charges vs Churn

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

# Tenure Distribution
plt.figure(figsize=(6,5))
sns.histplot(df['tenure'], bins=20,color="#1F4E79")
plt.title("Customer Tenure Distribution", fontsize=14, fontweight='bold')

plt.show()

# Monthly charges distribution 

plt.figure(figsize=(6,5))

sns.histplot(df['MonthlyCharges'], bins=30, color="#2E75B6")

plt.title("Monthly Charges Distribution", fontsize=14, fontweight='bold')

plt.show()

# Churn by Internet Service

plt.figure(figsize=(6,5))

sns.countplot(x='InternetService', hue='Churn', data=df,palette=['#70AD47','#1F4E79'] )

plt.title("Churn by Internet Service", fontsize=14, fontweight='bold')

plt.show()

# Churn by Gender

plt.figure(figsize=(6,5))
sns.countplot(x='gender', hue='Churn', data=df, palette=['#70AD47','#1F4E79'])

plt.title("Churn by Gender", fontsize=14, fontweight='bold')

plt.show()
