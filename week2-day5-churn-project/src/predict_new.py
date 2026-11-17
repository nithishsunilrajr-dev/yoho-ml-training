import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import joblib
import pandas as pd

def main(input_csv, output_csv='predictions.csv'):
    artifact = joblib.load('models/churn_model.joblib')
    model = artifact['model']
    threshold = artifact['threshold']

    new_data = pd.read_csv(input_csv)
    if 'Churn' in new_data.columns:
        new_data = new_data.drop(columns=['Churn'])
    if 'customerID' in new_data.columns:
        ids = new_data['customerID']
        features_df = new_data.drop(columns=['customerID'])
    else:
        ids = None
        features_df = new_data

    probs = model.predict_proba(features_df)[:, 1]
    preds = (probs >= threshold).astype(int)

    output = pd.DataFrame()
    if ids is not None:
        output['customerID'] = ids
    output['churn_probability'] = probs.round(4)
    output['churn_prediction'] = preds
    output.to_csv(output_csv, index=False)
    print(f"Saved {len(output)} predictions to {output_csv}")

if __name__ == '__main__':
    input_path = sys.argv[1] if len(sys.argv) > 1 else 'data/WA_Fn-UseC_-Telco-Customer-Churn.csv'
    main(input_path)