import pandas as pd

df = pd.read_csv(r"C:\Users\Lenovo\Desktop\inf intership\customer_support_tickets_200k.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())


print("Duplicate Rows :", df.duplicated().sum())

df = df.drop_duplicates()

print(df.shape)

print(df.dtypes)

df.select_dtypes(include='object')

print(df['priority'].value_counts())

print(df['customer_segment'].value_counts())

import matplotlib.pyplot as plt

df['priority'].value_counts().plot(kind='bar')

plt.title("Priority Distribution")
plt.xlabel("Priority")
plt.ylabel("Count")
plt.show()

df.isnull().sum()

df.fillna("Unknown", inplace=True)


print(df.corr(numeric_only=True))

df['issue_complexity_score'].describe()

print(df.groupby('customer_segment').size())

df.to_csv("cleaned_dataset.csv", index=False)

