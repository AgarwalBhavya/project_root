import json
import argparse
import pandas as pd
from utils.features import extract_features
from utils.scoring import score_wallets

def load_json(input_path):
    with open(input_path, 'r') as f:
        data = json.load(f)
    return data

def main(input_path, output_path):
    raw_data = load_json(input_path)
    df = pd.DataFrame(raw_data)
    features_df = extract_features(df)
    scored_df = score_wallets(features_df)
    scored_df.to_csv(output_path, index=False)
    print(f"Scoring complete. Output saved to: {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to input sample.json')
    parser.add_argument('--output', required=True, help='Path to output CSV file')
    args = parser.parse_args()
    main(args.input, args.output)
