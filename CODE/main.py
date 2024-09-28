# Simple Ticket Booking System in Python

# In-memory list to store ticket bookings
tickets = []

# Function to display the menu
def display_menu():
    print("\n--- Virtual Ticketing System ---")
    print("1. Book a Ticket")
    print("2. View All Bookings")
    print("3. Exit")

# Function to book a ticket
def book_ticket():
    print("\n--- Book a Ticket ---")
    customer_name = input("Enter Customer Name: ")
    event_name = input("Enter Event Name: ")
    try:
        ticket_quantity = int(input("Enter Number of Tickets: "))
    except ValueError:
        print("Invalid number. Please enter a valid integer.")
        return

    # Store ticket details in the tickets list
    ticket = {
        'Customer Name': customer_name,
        'Event Name': event_name,
        'Number of Tickets': ticket_quantity
    }
    tickets.append(ticket)
    print("Ticket booked successfully!")

# Function to view all bookings
def view_bookings():
    print("\n--- All Ticket Bookings ---")
    if len(tickets) == 0:
        print("fully booked.")
    else:
        for index, ticket in enumerate(tickets):
            print(f"\nBooking {index + 1}:")
            print(f"Customer Name: {ticket['Customer Name']}")
            print(f"Event Name: {ticket['Event Name']}")
            print(f"Number of Tickets: {ticket['Number of Tickets']}")

# Main function to run the ticketing system
def run_ticketing_system():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            book_ticket()
        elif choice == '2':
            view_bookings()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the ticketing system
if __name__ == "__main__":
    run_ticketing_system()