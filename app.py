from flask import Flask, render_template, jsonify
import pandas as pd
import random

app = Flask(__name__)

# List of real usernames
usernames = ['ramu', 'ravi_02', 'sita', 'john_doe', 'alice', 'bob', 'charlie', 'dave', 'eve', 'frank']

# Simulated user data
# Simulated user data with unique usernames
def generate_random_users(n):
    users = []
    available_usernames = usernames.copy()  # Copy to keep original list intact
    random.shuffle(available_usernames)  # Shuffle to randomize the order
    
    for i in range(min(n, len(available_usernames))):  # Ensure not to exceed available usernames
        username = available_usernames[i]
        users.append({
            'username': username,
            'followers_count': random.randint(10, 5000),
            'following_count': random.randint(5, 3000),
            'tweet_count': random.randint(0, 1000),
            'account_created_at': f'2023-09-{random.randint(1, 30):02d}',
            'verified': random.choice([True, False]),
            'suspicious_flags': random.sample(['spammy tweets', 'sudden follower spikes', 'unverified account'], random.randint(0, 2)),
            'reasons': random.sample(['repetitive content', 'high engagement in a short time', 'bot-like behavior'], random.randint(1, 3))
        })
    return pd.DataFrame(users)


# Store all generated users for later retrieval
users_data = generate_random_users(100)  # Generate a larger set of users



@app.route('/get-user-details/<username>', methods=['GET'])
def get_user_details(username):
    # Sample user details - replace these with real user data
    user_details = {
        "username": username,
        "bio": f"This is the bio of {username}.",
        "location": f"{username}'s location",
        "followers_count": random.randint(100, 5000),  # Simulated realistic value
        "following_count": random.randint(50, 3000),  # Simulated realistic value
        "tweet_count": random.randint(0, 1000),  # Simulated realistic value
        "account_created_at": f"2023-09-{random.randint(1, 30):02d}",  # Simulated date
        "verified": random.choice([True, False]),  # Simulated verified status
        "website": f"http://{username}.com",  # Simulated website
        "suspicious_flags": random.sample(['Fake Profile', 'Suspicious Activity', 'None'], random.randint(0, 2)),
        "reasons": random.sample(['bot-like behavior', 'high engagement in a short time', 'repetitive content'], random.randint(1, 3))
    }

    return jsonify(user_details)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/analyze/<platform>')
def analyze(platform):
    return render_template('analysis.html')

@app.route('/get-analysis', methods=['GET'])
def get_analysis():
    users_data = generate_random_users(20)
    suspicious_users = users_data[users_data['suspicious_flags'].map(lambda x: len(x) > 0)]
    
    print("Suspicious Users Data:", suspicious_users)  # Log the suspicious users
    return suspicious_users.to_json(orient='records')



if __name__ == '__main__':
    app.run(debug=True)