import pandas as pd
telco = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

print(telco.head())
telco['TotalCharges'] = pd.to_numeric(telco['TotalCharges'], errors='coerce')
telco['TotalCharges'] = telco['TotalCharges'].fillna(0)
telco['TotalCharges'] = telco['TotalCharges'].astype(float)
print(telco['TotalCharges'].dtype)

print(telco.groupby('Contract')['Churn'].value_counts(normalize=True))
# (a) monthly spend by churn group
print(telco.groupby('Churn')['MonthlyCharges'].mean())

# (b) total spend by churn group
print(telco.groupby('Churn')['TotalCharges'].mean())

# (c) churn rate by price band — answers "do higher payers churn more?"
telco['price_band'] = pd.cut(telco['MonthlyCharges'],
                             bins=[0, 35, 70, 120],
                             labels=['Low', 'Mid', 'High'])
print(telco.groupby('price_band')['Churn'].value_counts(normalize=True).unstack()['Yes'])

addons = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
# (d) churn rate by number of add-ons
for col in addons:
    rates = telco.groupby(col)['Churn'].value_counts(normalize=True).unstack()['Yes']
    print(f"Churn rate by {col}: with {rates['Yes']:.0%}   without = {rates['No']:.0%}")
