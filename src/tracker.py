from transaction import Transaction

class FinanceTracker:
    """Manages all financial transactions"""
    
    def __init__(self):
        self.transactions = []
        self.next_id = 1
    
    def add_transaction(self, amount, category, description, date=None):
        """Add a new transaction"""
        transaction = Transaction(amount, category, description, date)
        transaction.id = self.next_id
        self.next_id += 1
        self.transactions.append(transaction)
        return transaction
    
    def delete_transaction(self, transaction_id):
        """Delete a transaction by ID"""
        for i, transaction in enumerate(self.transactions):
            if transaction.id == transaction_id:
                deleted = self.transactions.pop(i)
                return deleted
        return None
    
    def get_all_transactions(self):
        """Get all transactions sorted by date"""
        return sorted(self.transactions, key=lambda t: t.date, reverse=True)
    
    def get_transactions_by_category(self, category):
        """Get all transactions in a specific category"""
        return [t for t in self.transactions if t.category.lower() == category.lower()]
    
    def get_balance(self):
        """Calculate total balance (income - expenses)"""
        return sum(t.amount for t in self.transactions)
    
    def get_total_by_category(self):
        """Get spending totals grouped by category"""
        totals = {}
        for transaction in self.transactions:
            if transaction.category in totals:
                totals[transaction.category] += transaction.amount
            else:
                totals[transaction.category] = transaction.amount
        return totals
    
    def to_dict(self):
        """Convert tracker data to dictionary for JSON storage"""
        return {
            'next_id': self.next_id,
            'transactions': [t.to_dict() for t in self.transactions]
        }
    
    def from_dict(self, data):
        """Load tracker data from dictionary"""
        self.next_id = data['next_id']
        self.transactions = [Transaction.from_dict(t) for t in data['transactions']]