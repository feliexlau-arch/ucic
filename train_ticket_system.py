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
    print("4. Add tickets (restock)")
    print("5. Cancel reservation")
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


def add_tickets(tickets):
    show_tickets(tickets)
    choice = input("Enter train index to add tickets: ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(tickets):
        print("Index out of range.")
        return
    cnt = input("How many tickets to add: ").strip()
    if not cnt.isdigit():
        print("Invalid input.")
        return
    cnt = int(cnt)
    if cnt <= 0:
        print("Must add at least 1 ticket.")
        return
    tickets[idx]['remaining'] += cnt
    print(f"Added {cnt} tickets to {tickets[idx]['train']}. Now {tickets[idx]['remaining']} remaining.")


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


def main():
    tickets = [
        {"train": "G101", "route": "Beijing - Shanghai", "price": 199, "remaining": 10},
        {"train": "D202", "route": "Guangzhou - Shenzhen", "price": 88, "remaining": 15},
        {"train": "T303", "route": "Chengdu - Chongqing", "price": 55, "remaining": 8},
    ]
    reservations = []
    print("Welcome to the simple train ticket system!")
    while True:
        show_menu()
        choice = input("Choose option (1-6): ").strip()
        if choice == "1":
            show_tickets(tickets)
        elif choice == "2":
            buy_ticket(tickets, reservations)
        elif choice == "3":
            search_tickets(tickets)
        elif choice == "4":
            add_tickets(tickets)
        elif choice == "5":
            cancel_reservation(tickets, reservations)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
