import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X['TotalCharges'] = pd.to_numeric(X['TotalCharges'], errors='coerce').fillna(0)

        # 1. Tenure groups
        X['tenure_group'] = pd.cut(
            X['tenure'], bins=[-1, 12, 24, 48, 72],
            labels=['0-1yr', '1-2yr', '2-4yr', '4-6yr']
        ).astype(str)

        # 2. Average spend per month
        X['avg_spend_per_month'] = np.where(
            X['tenure'] > 0, X['TotalCharges'] / X['tenure'], X['MonthlyCharges']
        )

        # 3. Monthly charge difference
        X['charge_diff'] = X['MonthlyCharges'] - X['avg_spend_per_month']

        # 4. Total add-on services count
        services = [
            'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
            'TechSupport', 'StreamingTV', 'StreamingMovies'
        ]
        X['total_services'] = (X[services] == 'Yes').sum(axis=1)
        return X