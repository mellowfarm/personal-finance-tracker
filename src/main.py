from tracker import FinanceTracker
from utils import save_data, load_data

def print_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("💰 PERSONAL FINANCE TRACKER 💰")
    print("="*50)
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. View Balance")
    print("4. View Spending by Category")
    print("5. Delete Transaction")
    print("6. Exit")
    print("="*50)

def add_transaction_ui(tracker):
    """UI for adding a transaction"""
    print("\n--- Add New Transaction ---")
    try:
        amount = float(input("Amount (use negative for expenses): $"))
        category = input("Category (e.g., Food, Transport, Income): ")
        description = input("Description: ")
        date = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
        
        if not date:
            date = None
        
        transaction = tracker.add_transaction(amount, category, description, date)
        print(f"\n✓ Transaction added: {transaction}")
    except ValueError:
        print("✗ Invalid amount. Please enter a number.")

def view_transactions_ui(tracker):
    """UI for viewing all transactions"""
    transactions = tracker.get_all_transactions()
    if not transactions:
        print("\nNo transactions found.")
        return
    
    print("\n--- All Transactions ---")
    for t in transactions:
        print(f"ID {t.id}: {t}")

def view_balance_ui(tracker):
    """UI for viewing balance"""
    balance = tracker.get_balance()
    print(f"\n💵 Current Balance: ${balance:.2f}")

def view_by_category_ui(tracker):
    """UI for viewing spending by category"""
    totals = tracker.get_total_by_category()
    if not totals:
        print("\nNo transactions found.")
        return
    
    print("\n--- Spending by Category ---")
    for category, total in sorted(totals.items()):
        print(f"{category}: ${total:.2f}")

def delete_transaction_ui(tracker):
    """UI for deleting a transaction"""
    view_transactions_ui(tracker)
    try:
        transaction_id = int(input("\nEnter transaction ID to delete: "))
        deleted = tracker.delete_transaction(transaction_id)
        if deleted:
            print(f"✓ Deleted: {deleted}")
        else:
            print("✗ Transaction not found.")
    except ValueError:
        print("✗ Invalid ID.")

def main():
    """Main application loop"""
    tracker = FinanceTracker()
    load_data(tracker)
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            add_transaction_ui(tracker)
            save_data(tracker)
        elif choice == '2':
            view_transactions_ui(tracker)
        elif choice == '3':
            view_balance_ui(tracker)
        elif choice == '4':
            view_by_category_ui(tracker)
        elif choice == '5':
            delete_transaction_ui(tracker)
            save_data(tracker)
        elif choice == '6':
            print("\n👋 Goodbye! Your data has been saved.")
            break
        else:
            print("\n✗ Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()