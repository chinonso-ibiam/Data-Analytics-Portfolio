import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Customer_churn.Csv')
sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Distribution")
plt.show()