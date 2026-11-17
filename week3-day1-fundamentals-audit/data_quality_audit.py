import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ==========================================
# TASK 1: DATA QUALITY AUDIT & CLEANING
# ==========================================
cities = ['Chennai', 'chennai', 'CHENNAI ', 'Madurai', 'madurai', 'Coimbatore ']
base_rows = pd.DataFrame({
    'customer_id': list(range(101, 130)),
    'name': [f'Customer_{i}' for i in range(1, 30)],
    'email': [f'user{i}@mail.com' if i % 6 != 0 else np.nan for i in range(1, 30)],
    'city': [cities[i % len(cities)] for i in range(29)],
    'age': ([28, 34, -5, 45, 29, 250, 31, 40] * 4)[:29],
    'phone': ['9876543210' if i % 7 != 0 else '12345' for i in range(1, 30)]
})

# Add 3 exact duplicate rows so total = 32 rows
df_raw = pd.concat([base_rows, base_rows.iloc[[0, 4, 9]]], ignore_index=True)
df_raw.to_csv('customers_raw.csv', index=False)

rows_before = len(df_raw)
missing_pct = (df_raw.isna().mean() * 100).round(1)
dup_count = df_raw.duplicated().sum()
invalid_ages = ((df_raw['age'] < 18) | (df_raw['age'] > 100)).sum()
invalid_phones = (df_raw['phone'].astype(str).str.len() != 10).sum()

print("=== AUDIT BEFORE ===")
print("Missing % per column:\n", missing_pct)
print(f"Duplicates: {dup_count} | Invalid ages: {invalid_ages} | Invalid phones: {invalid_phones}")

# Clean data
df_clean = df_raw.copy()
df_clean['city'] = df_clean['city'].str.strip().str.title()
df_clean = df_clean.drop_duplicates()

# Flag missing emails and invalid phones instead of dropping valid customers
df_clean['email_missing_flag'] = df_clean['email'].isna().astype(int)
df_clean['email'] = df_clean['email'].fillna('missing@placeholder.com')

# Cast age to float before assigning median so Pandas 3.x allows decimal medians
df_clean['age'] = df_clean['age'].astype(float)
med_age = df_clean.loc[(df_clean['age'] >= 18) & (df_clean['age'] <= 100), 'age'].median()
df_clean.loc[(df_clean['age'] < 18) | (df_clean['age'] > 100), 'age'] = med_age

df_clean['valid_phone_flag'] = (df_clean['phone'].astype(str).str.len() == 10).astype(int)
df_clean.to_csv('customers_clean.csv', index=False)

print("\n=== BEFORE / AFTER SUMMARY ===")
print(f"Rows before: {rows_before} | after: {len(df_clean)}")
print(f"Missing email: {missing_pct['email']}% -> 0% (flagged)")
print(f"Duplicates removed: {dup_count}")
print(f"Invalid ages fixed: {invalid_ages}")

# ==========================================
# TASK 2: SAMPLE SIZE EXPERIMENT PLOT
# ==========================================
X_syn, y_syn = make_classification(n_samples=2500, n_features=20, n_informative=10, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X_syn, y_syn, test_size=0.2, random_state=42)

sample_sizes = [50, 100, 500, len(X_tr)]
accs = [
    accuracy_score(y_te, RandomForestClassifier(random_state=42).fit(X_tr[:n], y_tr[:n]).predict(X_te))
    for n in sample_sizes
]

plt.figure(figsize=(7, 4))
plt.plot(sample_sizes, accs, marker='o')
plt.xlabel("Training Sample Size")
plt.ylabel("Test Accuracy")
plt.title("Learning Curve: Accuracy vs. Sample Size")
plt.grid(True)
plt.savefig("sample_size_curve.png", bbox_inches='tight')
plt.show()

