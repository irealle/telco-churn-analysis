import pandas as pd
telco = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

#print(telco.info)
telco['TotalCharges'] = pd.to_numeric(telco['TotalCharges'], errors='coerce')
telco['TotalCharges'] = telco['TotalCharges'].fillna(0)
telco['TotalCharges'] = telco['TotalCharges'].astype(float)
print(telco['TotalCharges'].dtype)