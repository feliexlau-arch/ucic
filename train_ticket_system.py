"""Simple train ticket system (basic English version)

Small, easy-to-read code. Features:
- view tickets
- buy tickets (records simple in-memory reservation)
- search by train number or route
- add tickets (restock)
- cancel reservation (partial or full)
"""

def show_menu():
    print("\n===== Train Ticket System =====")
    print("1. View available tickets")
    print("2. Buy a ticket")
    print("3. Search by train or route")
    print("4. Cancel reservation")
    print("5. Show summary report")
    print("6. Exit")
    print("===============================")


def show_tickets(tickets):
    print("\nAvailable trains:")
    for i, t in enumerate(tickets, start=1):
        print(f"{i}. {t['train']}  Route: {t['route']}  Price: {t['price']}  Remaining: {t['remaining']}")


def buy_ticket(tickets, reservations):
    show_tickets(tickets)
    choice = input("Enter train number to buy (index): ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(tickets):
        print("Index out of range.")
        return
    t = tickets[idx]
    if t['remaining'] <= 0:
        print("Sold out.")
        return
    cnt = input("Enter how many tickets: ").strip()
    if not cnt.isdigit():
        print("Invalid input.")
        return
    cnt = int(cnt)
    if cnt <= 0:
        print("Must buy at least 1 ticket.")
        return
    if cnt > t['remaining']:
        print(f"Not enough tickets. Max {t['remaining']}.")
        return
    t['remaining'] -= cnt
    total = t['price'] * cnt
    reservations.append({
        'train_index': idx,
        'train': t['train'],
        'route': t['route'],
        'count': cnt,
        'price': t['price']
    })
    print(f"Bought {cnt} ticket(s) for {t['train']}. Total: {total}.")


def search_tickets(tickets):
    key = input("Enter train number or route keyword: ").strip().lower()
    if key == "":
        print("Empty keyword.")
        return
    found = []
    for i, t in enumerate(tickets, start=1):
        if key in t['train'].lower() or key in t['route'].lower():
            found.append((i, t))
    if not found:
        print("No matches.")
        return
    print("\nSearch results:")
    for i, t in found:
        print(f"{i}. {t['train']}  Route: {t['route']}  Price: {t['price']}  Remaining: {t['remaining']}")



def cancel_reservation(tickets, reservations):
    if not reservations:
        print("No reservations to cancel.")
        return
    print("\nReservations:")
    for i, r in enumerate(reservations, start=1):
        print(f"{i}. {r['train']}  Route: {r['route']}  Count: {r['count']}")
    choice = input("Enter reservation index to cancel (0 to return): ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return
    num = int(choice)
    if num == 0:
        return
    if num < 1 or num > len(reservations):
        print("Index out of range.")
        return
    res = reservations[num - 1]
    while True:
        part = input(f"How many to cancel (max {res['count']}): ").strip()
        if not part.isdigit():
            print("Invalid input.")
            continue
        part = int(part)
        if part <= 0 or part > res['count']:
            print("Invalid number.")
            continue
        break
    tickets[res['train_index']]['remaining'] += part
    res['count'] -= part
    print(f"Canceled {part} ticket(s) for {res['train']}.")
    if res['count'] == 0:
        reservations.pop(num - 1)


def show_summary_report(tickets, reservations):
    print("\n===== Summary Report =====")
    show_tickets(tickets)
    if reservations:
        print("\nCurrent reservations:")
        total_tickets = 0
        total_spent = 0
        for r in reservations:
            subtotal = r['price'] * r['count']
            total_tickets += r['count']
            total_spent += subtotal
            print(f"- {r['train']}  Route: {r['route']}  Count: {r['count']}  Subtotal: {subtotal}")
        print(f"\nTotal reserved tickets: {total_tickets}")
        print(f"Total price of reserved tickets: {total_spent}")
    else:
        print("\nNo current reservations.")
    print("==========================")


def process_choice(choice, tickets, reservations):
    if choice == "1":
        show_tickets(tickets)
    elif choice == "2":
        buy_ticket(tickets, reservations)
    elif choice == "3":
        search_tickets(tickets)
    elif choice == "4":
        cancel_reservation(tickets, reservations)
    elif choice == "5":
        show_summary_report(tickets, reservations)
    elif choice == "6":
        print("Goodbye!")
        show_summary_report(tickets, reservations)
        return False
    else:
        print("Invalid choice.")
    input("\nPress Enter to continue...")
    return True


def main():
    tickets = [
        {"train": "LOL-007", "route": "Kabul - New York", "price": 199, "remaining": 10},
        {"train": "XD-404", "route": "Beijing - Los Angeles", "price": 88, "remaining": 15},
        {"train": "WTF-911", "route": "Istanbul - Dubai", "price": 55, "remaining": 8},
        {"train": "OMG-666", "route": "Moscow - Rio de Janeiro", "price": 120, "remaining": 12},
        {"train": "Zzz-1000", "route": "Lagos - Sydney", "price": 65, "remaining": 20},
        {"train": "GG-999", "route": "Cairo - San Francisco", "price": 45, "remaining": 18},
    ]
    reservations = []
    print("Welcome to the simple train ticket system!")
    show_menu()
    while process_choice(input("Choose option (1-6): ").strip(), tickets, reservations):
        show_menu()


if __name__ == "__main__":
    main()
