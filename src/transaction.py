from datetime import datetime

class Transaction:
    """Represents a single financial transaction"""
    
    def __init__(self, amount, category, description, date=None):
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        self.id = None  # Will be set by tracker
    
    def to_dict(self):
        """Convert transaction to dictionary for JSON storage"""
        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date
        }
    
    @staticmethod
    def from_dict(data):
        """Create transaction from dictionary"""
        transaction = Transaction(
            data['amount'],
            data['category'],
            data['description'],
            data['date']
        )
        transaction.id = data['id']
        return transaction
    
    def __str__(self):
        return f"[{self.date}] ${self.amount:.2f} - {self.category}: {self.description}"