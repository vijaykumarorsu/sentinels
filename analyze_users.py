import pandas as pd
from datetime import datetime

def analyze_random_users(user_data):
    results = []
    for index, row in user_data.iterrows():
        analysis = {
            "username": row['username'],
            "suspicious_followers_count": row['followers_count'] < 10,
            "suspicious_following_count": row['following_count'] > 5000,
            "suspicious_tweet_activity": row['tweet_count'] < 20,
            "suspicious_account_age": (datetime.now() - pd.to_datetime(row['account_created_at'])).days < 30,
            "suspicious_verified_status": not row['verified'] and row['followers_count'] > 1000
        }
        results.append(analysis)
    return results

if __name__ == "__main__":
    # Load random user data (replace with actual data loading logic as needed)
    user_data = pd.read_csv('random_users.csv')  # Assume you save generated data here
    analysis_results = analyze_random_users(user_data)
    print(analysis_results)
