import json
import os

DATA_FILE = 'data/transactions.json'

def save_data(tracker):
    """Save tracker data to JSON file"""
    os.makedirs('data', exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(tracker.to_dict(), f, indent=2)
    print("✓ Data saved successfully!")

def load_data(tracker):
    """Load tracker data from JSON file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                tracker.from_dict(data)
            print("✓ Data loaded successfully!")
            return True
        except Exception as e:
            print(f"✗ Error loading data: {e}")
            return False
    return False