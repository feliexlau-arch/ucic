"""Simple train ticket system.

This program is a simple train ticket system for beginners learning Python.
It supports viewing available trains, buying tickets, and exiting the menu.

Run with:
    python train_ticket_system.py
"""


def show_menu():
    """Show the main menu"""
    print("\n===== Train Ticket System =====")
    print("1. View available tickets")
    print("2. Buy a ticket")
    print("3. Exit")
    print("============================")


def show_tickets(tickets):
    """Show all trains and remaining tickets"""
    print("\nAvailable trains:")
    for index, ticket in enumerate(tickets, start=1):
        print(
            f"{index}. {ticket['train']} Route: {ticket['route']} "
            f"Price: {ticket['price']} yuan Remaining: {ticket['remaining']} tickets"
        )


def buy_ticket(tickets):
    """Buy a ticket based on user input"""
    show_tickets(tickets)

    choice = input("Enter the train number you want to buy: ")
    if not choice.isdigit():
        print("Invalid input. Please enter a number.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(tickets):
        print("Invalid number. Please choose again.")
        return

    ticket = tickets[index]
    if ticket['remaining'] <= 0:
        print("This train is sold out.")
        return

    count = input("Enter how many tickets you want to buy: ")
    if not count.isdigit():
        print("Invalid input. Please enter a number.")
        return

    count = int(count)
    if count <= 0:
        print("The number of tickets must be greater than 0.")
        return

    if count > ticket['remaining']:
        print(f"Not enough tickets. You can buy at most {ticket['remaining']} tickets.")
        return

    ticket['remaining'] -= count
    total_price = ticket['price'] * count
    print(f"Purchase successful! You bought {count} ticket(s) for {ticket['train']}.")
    print(f"Total price: {total_price} yuan")


def main():
    """Main program function"""
    tickets = [
        {"train": "G101", "route": "Beijing - Shanghai", "price": 199, "remaining": 10},
        {"train": "D202", "route": "Guangzhou - Shenzhen", "price": 88, "remaining": 15},
        {"train": "T303", "route": "Chengdu - Chongqing", "price": 55, "remaining": 8},
    ]

    print("Welcome to the train ticket system!")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            show_tickets(tickets)
        elif choice == "2":
            buy_ticket(tickets)
        elif choice == "3":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
