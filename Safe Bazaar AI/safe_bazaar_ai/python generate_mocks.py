# generate_mocks.py - Quick Mock Data for Safe Bazaar AI
import pandas as pd
from faker import Faker
import random
import numpy as np

fake = Faker('en_US')  # Base, but we'll Kenyan-ize
fake_enhance = lambda: fake  # For now; pip faker-locales if you want Swahili

# Kenyan flavor lists
locations = ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret', 'Kitale', 'Nyeri']
ethics_flags = ['fair-trade', 'eco-friendly', 'women-owned', 'organic', 'vegan', None]
items = ['coffee beans', 'handmade baskets', 'organic veggies', 'beaded jewelry', 'maize flour', 'kitenge fabric', 'honey']
fraud_types = [None, 'deepfake_photo', 'fake_rating', 'phishing_link']  # For sim

def generate_buyers(n=250):
    data = {
        'id': range(1, n+1),
        'name': [fake.name() for _ in range(n)],  # e.g., "Aisha Mwangi"
        'location': [random.choice(locations) for _ in range(n)],
        'budget': [round(random.uniform(100, 5000), 2) for _ in range(n)],  # KSh
        'preferences': [random.sample(ethics_flags, random.randint(1,3)) for _ in range(n)],  # List as str
        'trust_score': [round(random.uniform(0.6, 1.0), 2) for _ in range(n)]  # High for buyers
    }
    df = pd.DataFrame(data)
    df['preferences'] = df['preferences'].apply(lambda x: '|'.join(x))  # Pipe-sep for CSV
    return df

def generate_sellers(n=250):
    data = {
        'id': [f'S{str(i).zfill(3)}' for i in range(1, n+1)],  # e.g., S001
        'name': [fake.name() for _ in range(n)],
        'location': [random.choice(locations) for _ in range(n)],
        'item': [random.choice(items) for _ in range(n)],
        'price': [round(random.uniform(50, 2000), 2) for _ in range(n)],
        'ethics_flags': [random.choice(ethics_flags) for _ in range(n)],
        'rating': [round(random.uniform(1, 5), 1) for _ in range(n)],
        'fraud_flag': [random.choices(fraud_types, weights=[0.9, 0.025, 0.025, 0.05])[0] for _ in range(n)],  # 10% fraud
        'trust_score': []  # We'll compute later; placeholder
    }
    df = pd.DataFrame(data)
    # Sim trust: Lower if fraud
    df['trust_score'] = df.apply(lambda row: round(random.uniform(0.4, 0.9) if row['fraud_flag'] else random.uniform(0.7, 1.0), 2), axis=1)
    return df

# Generate & Save
buyers = generate_buyers(250)
sellers = generate_sellers(250)
buyers.to_csv('data/raw/buyers.csv', index=False)
sellers.to_csv('data/raw/sellers.csv', index=False)

# Quick Stats
print("Buyers Generated:", len(buyers))
print("Sellers Generated:", len(sellers))
print("\nSample Buyer:\n", buyers.head(1))
print("\nSample Seller:\n", sellers.head(1))
print("\nFraud Rate in Sellers:", (sellers['fraud_flag'].notna().sum() / len(sellers)) * 100, "%")
print("\nAvg Trust Scores - Buyers:", buyers['trust_score'].mean())
print("Avg Trust Scores - Sellers:", sellers['trust_score'].mean())